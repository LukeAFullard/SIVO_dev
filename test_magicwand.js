const fs = require('fs');

// Create a mock image 10x10.
const w = 10;
const h = 10;
const mask = new Uint8Array(w * h);

// solid block from (2,2) to (7,7)
for (let y = 2; y <= 7; y++) {
    for (let x = 2; x <= 7; x++) {
        mask[y * w + x] = 1;
    }
}

function traceContour(mask, w, h) {
    let startX = -1, startY = -1;
    for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
            if (mask[y * w + x] === 1) {
                startX = x; startY = y; break;
            }
        }
        if (startX !== -1) break;
    }
    if (startX === -1) return [];

    const path = [];
    let cx = startX, cy = startY;

    // Directions: 0=E, 1=SE, 2=S, 3=SW, 4=W, 5=NW, 6=N, 7=NE
    // Notice how they go clockwise
    const dx = [1, 1, 0, -1, -1, -1, 0, 1];
    const dy = [0, 1, 1, 1, 0, -1, -1, -1];
    let dir = 7;

    path.push({x: cx, y: cy});

    let pointsFound = 0;
    const MAX_POINTS = 10000;

    // To prevent infinite loops in degenerate cases (like single pixels)
    // we should track visited boundary directed edges, or just rely on reaching start pixel.

    // In Moore, you look CLOCKWISE starting from the pixel BEFORE you entered the current pixel.
    while (pointsFound < MAX_POINTS) {
        let found = false;
        // Start looking from dir (which is backtrack direction + 2 typically)
        // Wait, the standard Moore neighbor tracing algorithm:
        // Let M be the current pixel. Let B be the previous pixel (in the background).
        // Check B's neighbors clockwise.
        // If our directions are clockwise, we just iterate i from 0 to 7:
        for (let i = 0; i < 8; i++) {
            const ndir = (dir + i) % 8;
            const nx = cx + dx[ndir];
            const ny = cy + dy[ndir];

            if (nx >= 0 && nx < w && ny >= 0 && ny < h && mask[ny * w + nx] === 1) {
                cx = nx; cy = ny;
                path.push({x: cx, y: cy});
                // The new backtrack direction is the opposite of the direction we just moved
                // which is (ndir + 4) % 8. We want to start searching from the pixel *before* that,
                // so we can use (ndir + 4 + 1) or + 2. Usually it's (ndir + 5) or (ndir + 6).
                // Let's use ndir + 6 % 8 (which is -2) or ndir + 5
                dir = (ndir + 5) % 8;
                found = true;
                pointsFound++;
                break;
            }
        }

        if (cx === startX && cy === startY) break;
        if (!found) break;
    }

    return path;
}

const path = traceContour(mask, w, h);
console.log("Path length:", path.length);
console.log("Path:", path);
