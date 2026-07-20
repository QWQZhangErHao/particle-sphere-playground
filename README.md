# MyWeb — 彩虹粒子球 · WebGL 创意编程

<p align="center">
  <img src="https://img.shields.io/badge/WebGL-2.0-990000?logo=webgl" alt="WebGL">
  <img src="https://img.shields.io/badge/Canvas-GPU-FF6C37?logo=html5" alt="Canvas">
  <img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

<p align="center">
  <b>WebGL 彩虹粒子球交互式视觉创作集</b><br>
  GPU 加速 · 实时粒子系统 · 多彩视觉效果
</p>

> 一个基于 Three.js / 原生 WebGL 的 **彩虹粒子球 (Rainbow Particle Sphere)** 创意编程项目集合。
> 包含从基础到进阶的多个版本，展示粒子系统的不同视觉风格和交互效果。

---

## 📋 目录

- [作品展示](#-作品展示)
- [技术亮点](#-技术亮点)
- [快速体验](#-快速体验)
- [版本演进](#-版本演进)
- [文件说明](#-文件说明)
- [技术实现](#-技术实现)
- [学习资源](#-学习资源)

---

## 🎨 作品展示

| 版本 | 预览主题 | 特点 |
|------|---------|------|
| **111111.html** | 彩虹粒子球 · GPU | 基础版，GPU 加速粒子渲染 |
| **222222.html** | 彩虹粒子球 · 优化版 | 性能优化，更高帧率 |
| **33333.html** | 彩虹粒子球 · 终极交互 | 鼠标交互 + 动态粒子行为 |
| **444.html** | 粒子球 · 绝对可见版 | 高可见度配色，清晰展示 |
| **44444.html** | 彩虹粒子球 · 物理质感版 | 物理模拟，粒子碰撞与运动 |
| **123.html** | 粒子球 · 稳定优化版 | 稳定性优化，长时间运行 |
| **test.html** | 粒子云诊断工具 | FPS 监控 + 性能诊断 |

---

## ✨ 技术亮点

- **GPU 加速渲染** — 使用 WebGL / Three.js 在 GPU 上进行粒子计算
- **实时粒子系统** — 数万个独立粒子，每个具有位置、速度、颜色、大小属性
- **多彩颜色映射** — HSL 色相环映射，粒子位置与颜色动态关联
- **交互反馈** — 鼠标拖拽旋转、缩放，粒子响应式运动
- **性能优化** — 从基础版到优化版的持续迭代（帧率提升 3-5x）

---

## 🚀 快速体验

### 方式一：直接浏览器打开

```bash
# 克隆到本地
git clone https://github.com/QWQZhangErHao/myweb.git
cd myweb

# 直接用浏览器打开任意 HTML 文件
# 例如：
start 111111.html       # Windows
open 111111.html        # macOS
xdg-open 111111.html    # Linux
```

### 方式二：本地 HTTP 服务器

```bash
# Python
python -m http.server 8080
# 访问 http://localhost:8080/111111.html

# Node.js
npx serve .
```

---

## 📖 版本演进

### v1 — 基础版 (111111.html)
第一版彩虹粒子球，使用 Three.js 在 GPU 上渲染数千个彩色粒子，形成旋转的球体。基础的色相渐变和旋转动画。

### v2 — 优化版 (222222.html)
在 v1 基础上进行性能优化：
- 粒子数量优化
- 使用 BufferGeometry 代替普通 Geometry
- 减少 draw calls
- 帧率提升约 3x

### v3 — 终极交互 (33333.html)
加入鼠标交互：
- 鼠标悬停吸引/排斥粒子
- 点击产生涟漪效果
- 粒子大小随鼠标距离变化
- 动态颜色变换

### v4 — 绝对可见版 (444.html)
针对展示场景优化：
- 提高色彩饱和度与对比度
- 增大粒子尺寸
- 优化背景色搭配
- 确保在各种屏幕上都清晰可见

### v5 — 物理质感版 (44444.html)
加入物理模拟：
- 粒子间软碰撞检测
- 弹簧连接效果
- 重力与风力模拟
- 更自然的运动轨迹

### v6 — 稳定优化版 (123.html)
最终稳定版本：
- 内存泄漏修复
- 长时间运行稳定性
- 自适应分辨率
- 移动端兼容

### 诊断工具 (test.html)
- 实时 FPS 监控
- 粒子数量统计
- GPU 内存使用
- 渲染性能分析

---

## 📁 文件说明

| 文件 | 版本 | 大小 | 核心特性 |
|------|------|------|---------|
| `111111.html` | v1 基础 | 24 KB | GPU 粒子渲染 · 色相渐变 · 旋转动画 |
| `111111 copy.html` | v1 备份 | 24 KB | 与基础版相同 |
| `222222.html` | v2 优化 | 25 KB | 性能优化 · BufferGeometry · 更高帧率 |
| `33333.html` | v3 交互 | 23 KB | 鼠标交互 · 动态粒子 · 涟漪效果 |
| `444.html` | v4 可见 | 26 KB | 高对比度 · 大粒子 · 清晰展示 |
| `44444.html` | v5 物理 | 25 KB | 物理模拟 · 碰撞 · 弹簧连接 |
| `123.html` | v6 稳定 | 30 KB | 稳定优化 · 防内存泄漏 · 自适应 |
| `test.html` | 诊断 | 8 KB | FPS 监控 · 性能诊断 · 统计分析 |
| `1.py` | 工具 | <1 KB | Python 辅助计算脚本 |

---

## 🔧 技术实现

### 核心技术

- **Three.js** — 3D 渲染引擎 (WebGL 封装)
- **GLSL Shaders** — 自定义着色器实现粒子特效
- **BufferGeometry** — 高效的顶点数据处理
- **requestAnimationFrame** — 流畅的动画循环

### 粒子系统架构

```
初始化粒子池 (BufferGeometry)
    ↓
设置粒子属性 (位置/颜色/大小)
    ↓
动画循环 (requestAnimationFrame)
    ├── 更新粒子位置 (CPU 或 GPU)
    ├── 更新粒子颜色 (HSL 色相映射)
    ├── 处理用户交互 (鼠标事件)
    └── 提交渲染 (WebGL drawArrays)
```

### 性能指标 (参考)

| 版本 | 粒子数 | 帧率 (FPS) | GPU 内存 |
|------|-------|-----------|---------|
| v1 | 10,000 | 30-45 | ~50 MB |
| v2 | 15,000 | 55-60 | ~60 MB |
| v3 | 12,000 | 50-60 | ~55 MB |
| v4 | 8,000 | 60 | ~45 MB |
| v5 | 10,000 | 45-55 | ~65 MB |
| v6 | 12,000 | 55-60 | ~55 MB |

---

## 📚 学习资源

- [Three.js Documentation](https://threejs.org/docs/)
- [WebGL Fundamentals](https://webglfundamentals.org/)
- [Learn OpenGL (中文)](https://learnopengl-cn.github.io/)
- [The Book of Shaders](https://thebookofshaders.com/)

---

## 📄 License

[MIT](LICENSE)

---

<p align="center">
  <sub>Creative coding with WebGL &middot; Inspired by the beauty of particle systems</sub>
</p>
