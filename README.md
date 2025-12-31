# Hailo AI HAT Performance Benchmark Project

**Student:** Najeeb Abu Kheit  
**Date:** November 24, 2025  
**Hardware:** Raspberry Pi 5 (8GB) + Hailo-8L AI HAT

## Project Overview

This project benchmarks the performance of the Hailo-8L AI accelerator on Raspberry Pi 5 across **5 different computer vision models**, comparing results with CPU baselines and manufacturer specifications.

## Quick Results

| Task | Model | Hailo FPS | CPU FPS | Speedup |
|------|-------|-----------|---------|---------|
| Segmentation | YOLOv5n-Seg | **64.2** | 0.8* | **80.3×** |
| Person/Face | YOLOv5s | **63.4** | ~2* | **~32×** |
| Object Detection | YOLOv8s | **57.8** | ~2* | **~29×** |
| Pose Estimation | YOLOv8s-Pose | **49.5** | 1.5* | **33.0×** |
| Classification | ResNet50 | **47.3** | **6.7** | **7.0×** |

\* = Estimated from literature  
**Bold** = Real measured baseline

**Key Finding:** All models achieve real-time performance (>15 FPS), with speedups ranging from 7× to 80× depending on task complexity.

## Documentation

### Main Report
📄 **[PROJECT_REPORT.md](PROJECT_REPORT.md)** - Complete project report with:
- Table of contents
- Clear explanations of all results
- Step-by-step reproduction guide
- Code examples
- Conclusions and findings

### Other Documentation
- `FINAL_PROJECT_DOCUMENTATION.md` - Detailed implementation record
- `ESSENTIAL_GUIDE.md` - Quick reference guide
- `results/benchmarks/BENCHMARK_RESULTS.md` - Detailed benchmark analysis
- `docs/research/` - Background research materials

## Project Structure

```
.
├── PROJECT_REPORT.md          # Main project report (START HERE)
├── README.md                  # This file
├── SYSTEM_INFO.txt            # Complete system information (for reproducibility)
├── collect_system_info.sh     # Script to collect system info
├── benchmark_cpu_resnet50.py  # CPU baseline benchmark tool
│
├── src/
│   ├── pose_estimation/       # Pose estimation model
│   ├── segmentation/          # Segmentation model
│   ├── hand_landmarks/        # MediaPipe hand detection (CPU only)
│   └── utils/
│
├── docs/
│   └── research/              # Background research
│
└── results/
    ├── benchmarks/            # Benchmark results and logs
    └── graphs/                # Visualization graphs
```

## Quick Start

### 1. Hardware Verification
```bash
lspci | grep Hailo
hailortcli fw-control identify
```

### 2. Install Dependencies
```bash
pip3 install opencv-python numpy psutil --break-system-packages
```

**Why `--break-system-packages`?**  
Raspberry Pi OS uses system-managed Python. This flag allows installing to system Python, which is required for Hailo bindings. See [PEP 668](https://peps.python.org/pep-0668/) for details.

### 3. Run Benchmarks
```bash
# Hailo benchmarks (using official tool)
hailortcli benchmark /usr/share/hailo-models/yolov8s_pose_h8l_pi.hef
hailortcli benchmark /usr/share/hailo-models/yolov5n_seg_h8l_mz.hef

# CPU baseline (ResNet50 only)
python3 benchmark_cpu_resnet50.py
```

## Key Models Tested

1. **Pose Estimation** (YOLOv8s-Pose) - 49.5 FPS
2. **Segmentation** (YOLOv5n-Seg) - 64.2 FPS
3. **Object Detection** (YOLOv8s) - 57.8 FPS
4. **Classification** (ResNet50) - 47.3 FPS
5. **Person/Face Detection** (YOLOv5s) - 63.4 FPS

**Note:** Hand Landmark Detection (MediaPipe) is included as an example of a non-Hailo-Zoo model, but it runs on CPU only and is NOT optimized for Hailo.

## Results Summary

- ✅ **All models exceed real-time threshold** (>15 FPS)
- ✅ **Dense prediction tasks:** 30-80× speedup
- ✅ **Classification:** 7× speedup (measured, not estimated)
- ✅ **Results exceed manufacturer specs** (2-3× better)

## Reproducing This Project

See **[PROJECT_REPORT.md](PROJECT_REPORT.md)** Section 5 for complete step-by-step reproduction guide.

## Code Examples

All code examples are included in:
- `benchmark_cpu_resnet50.py` - CPU baseline measurement
- `src/hand_landmarks/hand_landmark_demo.py` - MediaPipe hand detection
- See PROJECT_REPORT.md Appendix for detailed code explanations

## System Information

**Complete system details** are documented in:
- `SYSTEM_INFO.txt` - Complete system information dump
- `PROJECT_REPORT.md` Section 3.1 - Detailed system environment

**Key System Details:**
- **OS:** Debian GNU/Linux 12 (bookworm)
- **Kernel:** 6.12.34+rpt-rpi-2712
- **Python:** 3.11.2
- **HailoRT:** 4.20.0

To regenerate system info:
```bash
./collect_system_info.sh > SYSTEM_INFO.txt
```

## Important Notes

- **Model files (`.hef`)** are excluded from git (too large). They can be found in `/usr/share/hailo-models/` on Raspberry Pi with AI Kit installed.
- **MediaPipe model** is NOT optimized for Hailo - it runs on CPU only.
- **CPU baselines** for most models are estimated from literature. Only ResNet50 has a real measured baseline.
- **System information** is critical for reproducibility - see `SYSTEM_INFO.txt` and `PROJECT_REPORT.md` Section 3.1.

## References

- Hailo Technologies Ltd. (2024). "Hailo-8L AI Accelerator Product Brief"
- Hailo Model Zoo: https://github.com/hailo-ai/hailo_model_zoo
- Raspberry Pi AI Kit Documentation
- PEP 668: https://peps.python.org/pep-0668/

---

**Project Status:** ✅ Complete  
**Total Models Tested:** 5 Hailo models + 1 CPU baseline + 1 MediaPipe (CPU only)

