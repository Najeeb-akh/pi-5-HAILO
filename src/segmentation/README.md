# Segmentation Benchmark

YOLOv5n-Seg segmentation model for Raspberry Pi 5 with Hailo-8L.

## Quick Start

The model file is already in `models/` directory. You can benchmark it using the official Hailo tool:

```bash
# From project root
hailortcli benchmark models/yolov5n_seg_h8l_mz.hef
```

Or use the model path directly:

```bash
hailortcli benchmark /usr/share/hailo-models/yolov5n_seg_h8l_mz.hef
```

## Expected Performance

With Hailo-8L:
- **FPS**: ~64 FPS
- **Latency**: ~14 ms
- **Speedup**: ~80× vs CPU

Without Hailo (CPU only):
- **FPS**: ~0.8 FPS
- **Latency**: ~1250 ms

## Model Location

The model file `yolov5n_seg_h8l_mz.hef` is stored in the `models/` directory. If you need to download it:

```bash
cd models/
# Model should be pre-installed, but if needed:
cp /usr/share/hailo-models/yolov5n_seg_h8l_mz.hef .
```

## Results

Benchmark results are saved to `results/benchmarks/`. Check the main report (`final_report.md`) for detailed performance analysis.
