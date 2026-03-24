'use strict';

// ═══════════════════════════════════════════════════════════════════
// CONSTANTS
// ═══════════════════════════════════════════════════════════════════

const MAX_DIM = 480;

const GROUP_HEX = {
    vtl:        '#7c7cff',
    cone:       '#5dff91',
    opponent:   '#ffd45a',
    deficiency: '#ff8066',
    combined:   '#c8a0ff',
};

// Matplotlib inferno, 10 stops
const INFERNO = [
    [0,   0,   4  ],
    [25,  10,  60 ],
    [72,  12,  106],
    [120, 28,  109],
    [166, 48,  97 ],
    [207, 80,  64 ],
    [237, 121, 26 ],
    [249, 163, 7  ],
    [251, 210, 78 ],
    [252, 255, 164],
];

function infernoRGB(t) {
    t = Math.max(0, Math.min(1, t));
    const i = t * (INFERNO.length - 1);
    const lo = Math.floor(i), hi = Math.min(lo + 1, INFERNO.length - 1);
    const f = i - lo;
    return [
        INFERNO[lo][0] + f * (INFERNO[hi][0] - INFERNO[lo][0]),
        INFERNO[lo][1] + f * (INFERNO[hi][1] - INFERNO[lo][1]),
        INFERNO[lo][2] + f * (INFERNO[hi][2] - INFERNO[lo][2]),
    ];
}

// ═══════════════════════════════════════════════════════════════════
// COLOR SCIENCE
// ═══════════════════════════════════════════════════════════════════

function degamma(c) {
    return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
}

// sRGB uint8 ImageData → linear Float32 channels [0,1]
function extractLinearRGB(data, N) {
    const R = new Float32Array(N);
    const G = new Float32Array(N);
    const B = new Float32Array(N);
    for (let i = 0; i < N; i++) {
        R[i] = degamma(data[i * 4    ] / 255);
        G[i] = degamma(data[i * 4 + 1] / 255);
        B[i] = degamma(data[i * 4 + 2] / 255);
    }
    return [R, G, B];
}

// Linear RGB → LAB L* normalized [0,1]
function labLuminance(R, G, B, N) {
    const L = new Float32Array(N);
    for (let i = 0; i < N; i++) {
        const Y = 0.2126729 * R[i] + 0.7151522 * G[i] + 0.0721750 * B[i];
        const f = Y > 0.008856 ? Math.cbrt(Y) : 7.787 * Y + 16 / 116;
        L[i] = Math.max(0, (116 * f - 16) / 100);
    }
    return L;
}

// sRGB linear → LMS  (Hunt-Pointer-Estevez, D65)
// Precomputed: sRGB-linear → XYZ(D65) → LMS(HPE)
const LMS_M = [
    [0.31396, 0.63972, 0.04649],   // L  560 nm
    [0.15544, 0.75794, 0.08671],   // M  530 nm
    [0.01775, 0.10945, 0.87257],   // S  419 nm
];

function rgbToLms(R, G, B, N) {
    const Lc = new Float32Array(N);
    const Mc = new Float32Array(N);
    const Sc = new Float32Array(N);
    const [lr, lg, lb] = LMS_M[0];
    const [mr, mg, mb] = LMS_M[1];
    const [sr, sg, sb] = LMS_M[2];
    for (let i = 0; i < N; i++) {
        Lc[i] = lr * R[i] + lg * G[i] + lb * B[i];
        Mc[i] = mr * R[i] + mg * G[i] + mb * B[i];
        Sc[i] = sr * R[i] + sg * G[i] + sb * B[i];
    }
    return [Lc, Mc, Sc];
}

// ═══════════════════════════════════════════════════════════════════
// SIGNAL PROCESSING
// ═══════════════════════════════════════════════════════════════════

function gaussianKernel(sigma) {
    const r = Math.ceil(3 * sigma);
    const k = new Float32Array(2 * r + 1);
    let sum = 0;
    for (let i = 0; i <= 2 * r; i++) {
        const x = i - r;
        k[i] = Math.exp(-x * x / (2 * sigma * sigma));
        sum += k[i];
    }
    for (let i = 0; i < k.length; i++) k[i] /= sum;
    return k;
}

function blurH(src, W, H, k) {
    const half = (k.length - 1) >> 1;
    const dst = new Float32Array(W * H);
    for (let y = 0; y < H; y++) {
        const row = y * W;
        for (let x = 0; x < W; x++) {
            let v = 0;
            for (let j = 0; j < k.length; j++) {
                v += src[row + Math.min(Math.max(x + j - half, 0), W - 1)] * k[j];
            }
            dst[row + x] = v;
        }
    }
    return dst;
}

function blurV(src, W, H, k) {
    const half = (k.length - 1) >> 1;
    const dst = new Float32Array(W * H);
    for (let x = 0; x < W; x++) {
        for (let y = 0; y < H; y++) {
            let v = 0;
            for (let j = 0; j < k.length; j++) {
                v += src[Math.min(Math.max(y + j - half, 0), H - 1) * W + x] * k[j];
            }
            dst[y * W + x] = v;
        }
    }
    return dst;
}

function gaussianBlur(src, W, H, sigma) {
    const k = gaussianKernel(sigma);
    return blurV(blurH(src, W, H, k), W, H, k);
}

// DoG: difference-of-Gaussians, ON-center lateral inhibition
// Biologically: center excitation minus surround inhibition
function dog(src, W, H, sigmaC = 1.0, sigmaS = 3.0, w = 0.65) {
    const center   = gaussianBlur(src, W, H, sigmaC);
    const surround = gaussianBlur(src, W, H, sigmaS);
    const out = new Float32Array(W * H);
    for (let i = 0; i < W * H; i++) out[i] = Math.max(0, center[i] - w * surround[i]);
    return out;
}

// Sobel gradient magnitude (used only for VTL baseline)
function sobelMag(src, W, H) {
    const out = new Float32Array(W * H);
    for (let y = 1; y < H - 1; y++) {
        for (let x = 1; x < W - 1; x++) {
            const tl = src[(y-1)*W+(x-1)], tc = src[(y-1)*W+ x   ], tr = src[(y-1)*W+(x+1)];
            const ml = src[    y*W+(x-1)],                            mr = src[    y*W+(x+1)];
            const bl = src[(y+1)*W+(x-1)], bc = src[(y+1)*W+ x   ], br = src[(y+1)*W+(x+1)];
            const gx = -tl + tr - 2*ml + 2*mr - bl + br;
            const gy = -tl - 2*tc - tr + bl + 2*bc + br;
            out[y*W+x] = Math.sqrt(gx*gx + gy*gy);
        }
    }
    return out;
}

// ═══════════════════════════════════════════════════════════════════
// FIELD UTILITIES
// ═══════════════════════════════════════════════════════════════════

function normalize(f) {
    let mn = Infinity, mx = -Infinity;
    for (let i = 0; i < f.length; i++) {
        if (f[i] < mn) mn = f[i];
        if (f[i] > mx) mx = f[i];
    }
    const r = mx - mn;
    if (r < 1e-9) return new Float32Array(f.length);
    const out = new Float32Array(f.length);
    for (let i = 0; i < f.length; i++) out[i] = (f[i] - mn) / r;
    return out;
}

function fieldSub(A, B) {        // max(0, A-B)
    const out = new Float32Array(A.length);
    for (let i = 0; i < A.length; i++) out[i] = Math.max(0, A[i] - B[i]);
    return out;
}

function fieldAvg2(A, B) {
    const out = new Float32Array(A.length);
    for (let i = 0; i < A.length; i++) out[i] = (A[i] + B[i]) * 0.5;
    return out;
}

// Elementwise product of two normalized fields — agreement mask
function fieldMul(A, B) {
    const nA = normalize(A), nB = normalize(B);
    const out = new Float32Array(A.length);
    for (let i = 0; i < A.length; i++) out[i] = nA[i] * nB[i];
    return out;
}

// Max across three fields — biological ceiling
function fieldMax3(A, B, C) {
    const out = new Float32Array(A.length);
    for (let i = 0; i < A.length; i++) out[i] = Math.max(A[i], B[i], C[i]);
    return out;
}

// Apply field only where gate is in void (normalized gate < threshold)
// Reveals structure in the regions the gate ignores
function fieldVoidGate(field, gate, threshold = 0.18) {
    const nGate = normalize(gate);
    const out = new Float32Array(field.length);
    for (let i = 0; i < field.length; i++) {
        out[i] = nGate[i] < threshold ? field[i] : 0;
    }
    return out;
}

// L+M-2S yellow-blue opponency
function yellowBlue(L, M, S) {
    const out = new Float32Array(L.length);
    for (let i = 0; i < L.length; i++) out[i] = Math.max(0, L[i] + M[i] - 2 * S[i]);
    return out;
}

// ═══════════════════════════════════════════════════════════════════
// VTL METRICS
// ═══════════════════════════════════════════════════════════════════

// Gradient-weighted centroid, normalized [-1, 1]
function computeCentroid(field, W, H) {
    let sx = 0, sy = 0, sw = 0;
    for (let y = 0; y < H; y++) {
        for (let x = 0; x < W; x++) {
            const w = field[y * W + x];
            sx += w * (x / (W - 1) * 2 - 1);
            sy += w * (y / (H - 1) * 2 - 1);
            sw += w;
        }
    }
    return sw < 1e-9 ? [0, 0] : [sx / sw, sy / sw];
}

// μ cohesion: fraction of total energy in the top-quartile pixels
// High = energy is concentrated. Low = energy is spread thin.
function computeCohesion(field) {
    const copy = Float32Array.from(field).sort();
    const cutoff = copy[Math.floor(copy.length * 0.75)];
    let top = 0, total = 0;
    for (let i = 0; i < field.length; i++) {
        total += field[i];
        if (field[i] >= cutoff) top += field[i];
    }
    return total > 1e-9 ? top / total : 0;
}

// rᵥ void ratio: fraction of image with near-zero gradient response
function computeVoidRatio(field) {
    const nf = normalize(field);
    let count = 0;
    for (let i = 0; i < nf.length; i++) if (nf[i] < 0.18) count++;
    return count / nf.length;
}

// ═══════════════════════════════════════════════════════════════════
// MODE DEFINITIONS
// ═══════════════════════════════════════════════════════════════════

function buildModes(R, G, B, W, H) {
    const N = W * H;

    // VTL baseline: Sobel on LAB-L
    const lum = labLuminance(R, G, B, N);
    const baseline = sobelMag(lum, W, H);

    // LMS — normalize each channel independently so structure is comparable
    const [Lr, Mr, Sr] = rgbToLms(R, G, B, N);
    const Ln = normalize(Lr), Mn = normalize(Mr), Sn = normalize(Sr);

    return [
        {
            name:  'VTL  Sobel / LAB-L',
            short: 'Baseline',
            field: baseline,
            group: 'vtl',
            note:  'Current system: luminance gradients only',
        },
        {
            name:  'L cone  560 nm',
            short: 'L cone',
            field: dog(Ln, W, H),
            group: 'cone',
            note:  'Long-wavelength (red) cone response',
        },
        {
            name:  'M cone  530 nm',
            short: 'M cone',
            field: dog(Mn, W, H),
            group: 'cone',
            note:  'Medium-wavelength (green) cone response',
        },
        {
            name:  'S cone  419 nm',
            short: 'S cone',
            field: dog(Sn, W, H),
            group: 'cone',
            note:  'Short-wavelength (blue) cone response',
        },
        {
            name:  'L − M  red-green',
            short: 'L−M',
            field: dog(fieldSub(Lr, Mr), W, H),
            group: 'opponent',
            note:  'Red-green color opponency channel',
        },
        {
            name:  'L+M − 2S  yellow-blue',
            short: 'L+M−2S',
            field: dog(yellowBlue(Lr, Mr, Sr), W, H),
            group: 'opponent',
            note:  'Yellow-blue color opponency channel',
        },
        {
            name:  'Protanopia  (no L)',
            short: 'Protanopia',
            field: dog(fieldAvg2(Mr, Sr), W, H),
            group: 'deficiency',
            note:  'Missing long-wavelength cone — red-green confusion',
        },
        {
            name:  'Deuteranopia  (no M)',
            short: 'Deuteranopia',
            field: dog(fieldAvg2(Lr, Sr), W, H),
            group: 'deficiency',
            note:  'Missing medium-wavelength cone — most common deficiency',
        },
        {
            name:  'Tritanopia  (no S)',
            short: 'Tritanopia',
            field: dog(fieldAvg2(Lr, Mr), W, H),
            group: 'deficiency',
            note:  'Missing short-wavelength cone — blue-yellow confusion',
        },

        // ── Combined masks ───────────────────────────────────────────
        {
            name:    'VTL × L−M  confirmed edges',
            short:   'VTL×L−M',
            field:   fieldMul(baseline, dog(fieldSub(Lr, Mr), W, H)),
            group:   'combined',
            section: 'combined masks',
            note:    'Where luminance edge and color opponency agree — filters synthetic mass',
        },
        {
            name:  'Cone max  biological ceiling',
            short: 'Cone max',
            field: fieldMax3(dog(Ln, W, H), dog(Mn, W, H), dog(Sn, W, H)),
            group: 'combined',
            note:  'Widest reading any single cone channel gives — most biologically sensitive',
        },
        {
            name:  'L−M in VTL void  blind spot',
            short: 'Void/L−M',
            field: fieldVoidGate(dog(fieldSub(Lr, Mr), W, H), baseline),
            group: 'combined',
            note:  'Color opponency only where Sobel sees nothing — what VTL structurally ignores',
        },
    ];
}

// ═══════════════════════════════════════════════════════════════════
// RENDERING
// ═══════════════════════════════════════════════════════════════════

// Render gradient field as inferno heatmap blended over ghost original,
// with centroid crosshair overlay. Returns [cx, cy].
function renderPanel(canvas, imgData, field, W, H) {
    canvas.width  = W;
    canvas.height = H;
    const ctx = canvas.getContext('2d');

    const nf  = normalize(field);
    const out = new Uint8ClampedArray(W * H * 4);

    for (let i = 0; i < W * H; i++) {
        const [hr, hg, hb] = infernoRGB(nf[i]);
        const or = imgData.data[i * 4    ];
        const og = imgData.data[i * 4 + 1];
        const ob = imgData.data[i * 4 + 2];
        const a  = 0.84;
        out[i * 4    ] = (1 - a) * or + a * hr;
        out[i * 4 + 1] = (1 - a) * og + a * hg;
        out[i * 4 + 2] = (1 - a) * ob + a * hb;
        out[i * 4 + 3] = 255;
    }

    ctx.putImageData(new ImageData(out, W, H), 0, 0);

    // Centroid overlay
    const [cx, cy] = computeCentroid(field, W, H);
    const px = (cx + 1) / 2 * (W - 1);
    const py = (cy + 1) / 2 * (H - 1);

    // Line: center → centroid
    ctx.strokeStyle = 'rgba(0,229,255,0.40)';
    ctx.lineWidth   = 1;
    ctx.beginPath();
    ctx.moveTo(W / 2, H / 2);
    ctx.lineTo(px, py);
    ctx.stroke();

    // Center reference dot
    ctx.fillStyle = 'rgba(255,255,255,0.30)';
    ctx.beginPath();
    ctx.arc(W / 2, H / 2, 2.5, 0, Math.PI * 2);
    ctx.fill();

    // Centroid crosshair
    const s = 7;
    ctx.strokeStyle = '#00e5ff';
    ctx.lineWidth   = 1.5;
    ctx.beginPath();
    ctx.moveTo(px - s, py); ctx.lineTo(px + s, py);
    ctx.moveTo(px, py - s); ctx.lineTo(px, py + s);
    ctx.stroke();

    return [cx, cy];
}

// 2D scatter: each mode as a dot at (Δx, Δy)
function renderScatter(canvas, modes) {
    const W = canvas.width;
    const H = canvas.height;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = '#0f0f14';
    ctx.fillRect(0, 0, W, H);

    const PAD = 44, RANGE = 0.65;
    const CW = W - PAD * 2, CH = H - PAD * 2;

    const tx = dx => PAD + (dx + RANGE) / (2 * RANGE) * CW;
    const ty = dy => PAD + (dy + RANGE) / (2 * RANGE) * CH;

    // Grid
    ctx.strokeStyle = '#1c1c26';
    ctx.lineWidth = 1;
    for (const v of [-0.5, -0.25, 0, 0.25, 0.5]) {
        ctx.beginPath();
        ctx.moveTo(tx(v), PAD);     ctx.lineTo(tx(v), PAD + CH);
        ctx.moveTo(PAD, ty(v));     ctx.lineTo(PAD + CW, ty(v));
        ctx.stroke();
    }

    // Zero axes (slightly brighter)
    ctx.strokeStyle = '#2c2c3e';
    ctx.beginPath();
    ctx.moveTo(tx(0), PAD); ctx.lineTo(tx(0), PAD + CH);
    ctx.moveTo(PAD, ty(0)); ctx.lineTo(PAD + CW, ty(0));
    ctx.stroke();

    // Axis labels
    ctx.fillStyle = '#2e2e44';
    ctx.font      = '10px monospace';
    ctx.textAlign = 'center';
    ctx.fillText('← left  ·  Δx  ·  right →', W / 2, PAD - 16);
    ctx.save();
    ctx.translate(14, H / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText('← up  ·  Δy  ·  down →', 0, 0);
    ctx.restore();

    // Tick labels
    ctx.fillStyle = '#2e2e44';
    ctx.font      = '9px monospace';
    for (const v of [-0.5, 0, 0.5]) {
        ctx.textAlign = 'center';
        ctx.fillText(v.toFixed(1), tx(v), PAD + CH + 12);
        ctx.textAlign = 'right';
        ctx.fillText(v.toFixed(1), PAD - 4, ty(v) + 3);
    }

    // Plot each mode
    for (const m of modes) {
        if (m.cx == null) continue;
        const x = tx(m.cx), y = ty(m.cy);
        const col = GROUP_HEX[m.group];

        // Glow
        const grad = ctx.createRadialGradient(x, y, 0, x, y, 12);
        grad.addColorStop(0, col + '40');
        grad.addColorStop(1, col + '00');
        ctx.fillStyle = grad;
        ctx.beginPath(); ctx.arc(x, y, 12, 0, Math.PI * 2); ctx.fill();

        // Dot
        ctx.fillStyle = col;
        ctx.beginPath(); ctx.arc(x, y, 4.5, 0, Math.PI * 2); ctx.fill();

        // Label
        ctx.fillStyle = col;
        ctx.font      = '9px monospace';
        ctx.textAlign = 'left';
        ctx.fillText(m.short, x + 8, y + 3);
    }

    // Center reference
    ctx.strokeStyle = 'rgba(255,255,255,0.18)';
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.arc(tx(0), ty(0), 3, 0, Math.PI * 2); ctx.stroke();
}

// ═══════════════════════════════════════════════════════════════════
// APP
// ═══════════════════════════════════════════════════════════════════

function fmt(n) { return (n >= 0 ? '+' : '') + n.toFixed(3); }

async function loadImage(file) {
    return new Promise(resolve => {
        const img = new Image();
        const url = URL.createObjectURL(file);
        img.onload = () => {
            let W = img.naturalWidth, H = img.naturalHeight;
            const scale = Math.min(1, MAX_DIM / Math.max(W, H));
            W = Math.round(W * scale);
            H = Math.round(H * scale);
            const oc  = new OffscreenCanvas(W, H);
            const ctx = oc.getContext('2d');
            ctx.drawImage(img, 0, 0, W, H);
            URL.revokeObjectURL(url);
            resolve({ imgData: ctx.getImageData(0, 0, W, H), W, H });
        };
        img.src = url;
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const uploadZone    = document.getElementById('upload-zone');
    const fileInput     = document.getElementById('file-input');
    const workspace     = document.getElementById('workspace');
    const processing    = document.getElementById('processing');
    const origImg       = document.getElementById('orig-img');
    const grid          = document.getElementById('grid');
    const scatterCanvas = document.getElementById('scatter-canvas');

    uploadZone.addEventListener('click',     () => fileInput.click());
    uploadZone.addEventListener('dragover',  e  => { e.preventDefault(); uploadZone.classList.add('drag-over'); });
    uploadZone.addEventListener('dragleave', ()  => uploadZone.classList.remove('drag-over'));
    uploadZone.addEventListener('drop', e => {
        e.preventDefault();
        uploadZone.classList.remove('drag-over');
        if (e.dataTransfer.files[0]) handleFile(e.dataTransfer.files[0]);
    });
    fileInput.addEventListener('change', e => {
        if (e.target.files[0]) handleFile(e.target.files[0]);
    });

    async function handleFile(file) {
        processing.style.display = 'flex';
        workspace.style.display  = 'none';

        // Yield to let the processing overlay paint before heavy compute
        await new Promise(r => setTimeout(r, 60));

        try {
            const { imgData, W, H } = await loadImage(file);

            // Show original
            origImg.src = URL.createObjectURL(file);

            // Extract linear RGB
            const [R, G, B] = extractLinearRGB(imgData.data, W * H);

            // Build all gradient fields
            const modes = buildModes(R, G, B, W, H);

            // Render grid
            grid.innerHTML = '';
            const results = [];

            for (const mode of modes) {
                if (mode.section) {
                    const breakEl = document.createElement('div');
                    breakEl.className = 'grid-section-break';
                    breakEl.textContent = mode.section;
                    grid.appendChild(breakEl);
                }

                const panelEl = document.createElement('div');
                panelEl.className = 'panel';

                const nameEl = document.createElement('div');
                nameEl.className = `panel-name ${mode.group}`;
                nameEl.textContent = mode.name;
                nameEl.title = mode.note;

                const cvs = document.createElement('canvas');

                const metricsEl = document.createElement('div');
                metricsEl.className = 'panel-metrics';

                const [cx, cy] = renderPanel(cvs, imgData, mode.field, W, H);
                const mu = computeCohesion(mode.field);
                const rv = computeVoidRatio(mode.field);

                metricsEl.innerHTML =
                    `<span><span class="mk">Δx </span>${fmt(cx)}</span>` +
                    `<span><span class="mk">Δy </span>${fmt(cy)}</span>` +
                    `<span><span class="mk">μ </span>${mu.toFixed(2)}</span>` +
                    `<span><span class="mk">rᵥ </span>${rv.toFixed(2)}</span>`;

                panelEl.appendChild(nameEl);
                panelEl.appendChild(cvs);
                panelEl.appendChild(metricsEl);
                grid.appendChild(panelEl);

                results.push({ ...mode, cx, cy, mu, rv });
            }

            // Render scatter
            const sw = scatterCanvas.parentElement.offsetWidth || 640;
            scatterCanvas.width  = sw;
            scatterCanvas.height = Math.round(sw * 0.38);
            renderScatter(scatterCanvas, results);

            workspace.style.display = 'block';
        } finally {
            processing.style.display = 'none';
        }
    }
});
