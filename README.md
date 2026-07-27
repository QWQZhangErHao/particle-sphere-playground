# 🌈 Particle Sphere Playground

<p align="center">
  <img src="https://img.shields.io/badge/Three.js-r160-000000?logo=threedotjs" alt="Three.js">
  <img src="https://img.shields.io/badge/WebGL-2.0-990000?logo=webgl" alt="WebGL">
  <img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <a href="https://qwqzhangerhao.github.io/particle-sphere-playground"><img src="https://img.shields.io/badge/Live%20Demo-2ea44f?logo=githubpages" alt="Live Demo"></a>
</p>

<p align="center">
  <b>Rainbow Particle Sphere — Interactive WebGL Creative Coding Collection</b><br>
  GPU-accelerated real-time particle systems built with Three.js
</p>

<p align="center">
  <a href="#-live-demos"><b>🎮 Play Now</b></a> ·
  <a href="#-versions"><b>📖 Versions</b></a> ·
  <a href="#-quick-start"><b>⚡ Quick Start</b></a>
</p>

---

A collection of **interactive 3D particle spheres** showing different visual styles and effects — from basic GPU rendering to physics simulation and hand-tracking interaction. Each file is a self-contained HTML page; open it in any browser and it just works.

## 🎮 Live Demos

| Version | Play | Description |
|---------|:----:|-------------|
| **Basic** | [▶ Play](https://qwqzhangerhao.github.io/particle-sphere-playground/v1-basic.html) | Foundational GPU particle sphere with hue gradient |
| **Optimized** | [▶ Play](https://qwqzhangerhao.github.io/particle-sphere-playground/v2-optimized.html) | Performance-tuned, higher frame rates |
| **Interactive** | [▶ Play](https://qwqzhangerhao.github.io/particle-sphere-playground/v3-interactive.html) | Mouse hover/click interaction, dynamic particles |
| **Enhanced** | [▶ Play](https://qwqzhangerhao.github.io/particle-sphere-playground/v4-enhanced.html) | High-contrast colors, large particles, better visibility |
| **Physics** | [▶ Play](https://qwqzhangerhao.github.io/particle-sphere-playground/v5-physics.html) | Soft-body physics, gravity, spring connections |
| **Stable** | [▶ Play](https://qwqzhangerhao.github.io/particle-sphere-playground/v6-stable.html) | Memory-safe, mobile-friendly, long-run stable |
| **Diagnostics** | [▶ Play](https://qwqzhangerhao.github.io/particle-sphere-playground/diagnostics.html) | FPS monitor, GPU stats, performance analysis |

## 🚀 Quick Start

Clone and open any file directly:

```bash
git clone https://github.com/QWQZhangErHao/particle-sphere-playground.git
cd particle-sphere-playground

# Open a file directly (no server needed)
open v1-basic.html          # macOS
start v1-basic.html         # Windows
xdg-open v1-basic.html      # Linux

# Or serve locally
python -m http.server 8080
# http://localhost:8080/v1-basic.html
```

## 📖 Versions

Each version builds on the previous one, adding new features and refinement:

| Version | File | Particles | FPS | Highlight |
|---------|------|:---------:|:---:|-----------|
| **v1 Basic** | [`v1-basic.html`](v1-basic.html) | 10,000 | 30-45 | First particle sphere, HSL hue mapping, rotation |
| **v2 Optimized** | [`v2-optimized.html`](v2-optimized.html) | 15,000 | 55-60 | BufferGeometry, reduced draw calls (~3× faster) |
| **v3 Interactive** | [`v3-interactive.html`](v3-interactive.html) | 12,000 | 50-60 | Mouse hover/click ripple, particle attraction |
| **v4 Enhanced** | [`v4-enhanced.html`](v4-enhanced.html) | 8,000 | 60 | High contrast, larger particles, screen-friendly |
| **v5 Physics** | [`v5-physics.html`](v5-physics.html) | 10,000 | 45-55 | Soft-body collision, springs, wind & gravity |
| **v6 Stable** | [`v6-stable.html`](v6-stable.html) | 12,000 | 55-60 | Memory-safe, responsive, mobile-ready |
| **Diagnostics** | [`diagnostics.html`](diagnostics.html) | — | — | FPS chart, GPU memory, performance counters |

## ✨ Features

- **GPU-accelerated** — All particle rendering offloaded to WebGL
- **6 evolving versions** — From basic to physics simulation, showing progressive enhancement
- **Zero dependencies to run** — Just open an HTML file in a modern browser
- **Interactive** — Mouse drag to rotate, hover for particle effects, click for ripples (v3+)
- **Live diagnostics** — Built-in performance monitoring and FPS tracking

## 🧰 Tech Stack

- [Three.js r160](https://threejs.org/) — WebGL 3D rendering engine
- Custom GLSL shaders for particle effects
- `BufferGeometry` for efficient vertex processing
- `requestAnimationFrame` animation loop
- ES6 modules via import maps

## 📄 License

[MIT](LICENSE)

---

<p align="center">
  <sub>Creative coding with Three.js & WebGL · Inspired by the beauty of particle systems</sub>
</p>
