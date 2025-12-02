# Pose Estimation Benchmark

## Overview
This module benchmarks YOLOv8-Pose model performance on Raspberry Pi 5 with and without Hailo acceleration.

## Models Required

### Hailo Model (.hef)
Download the pre-compiled model:
```bash
cd models/
wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/yolov8s_pose.hef
```

### CPU Model (.onnx) - Optional
For CPU baseline comparison, you can export from PyTorch:
```bash
pip install ultralytics
python -c "from ultralytics import YOLO; model = YOLO('yolov8s-pose.pt'); model.export(format='onnx')"
mv yolov8s-pose.onnx models/
```

## Usage

### Run Both CPU and Hailo Benchmarks
```bash
python benchmark_pose.py --mode both --iterations 100 --display
```

### Run Hailo Only
```bash
python benchmark_pose.py --mode hailo --iterations 200
```

### Run CPU Only
```bash
python benchmark_pose.py --mode cpu --iterations 50
```

### Use Video File Instead of Camera
```bash
python benchmark_pose.py --video /path/to/video.mp4 --iterations 100
```

## Command Line Options

- `--mode`: Which mode to benchmark (`cpu`, `hailo`, or `both`)
- `--hailo-model`: Path to .hef model file
- `--cpu-model`: Path to .onnx model file
- `--camera`: Camera device ID (default: 0)
- `--video`: Video file path (overrides camera)
- `--iterations`: Number of frames to process (default: 100)
- `--warmup`: Number of warmup frames (default: 20)
- `--display`: Show visual output during benchmark
- `--output-dir`: Directory to save results

## Expected Results

### Raspberry Pi 5 + Hailo-8L
- **FPS**: 20-25
- **Latency**: 40-50 ms
- **CPU Usage**: 10-20%

### Raspberry Pi 5 CPU Only
- **FPS**: 1.2-1.8
- **Latency**: 550-800 ms
- **CPU Usage**: 95-99%

### Speedup: ~12-18×

## Output Files

Results are saved to `../../results/benchmarks/`:

- `pose_benchmark_YYYYMMDD_HHMMSS.json` - Detailed metrics
- `pose_benchmark_results.csv` - Appended results for comparison

## Troubleshooting

### Hailo Not Detected
```bash
# Check if Hailo is connected
lspci | grep Hailo
hailortcli fw-control identify
```

### Camera Not Working
```bash
# Test camera
libcamera-hello

# Or try different camera ID
python benchmark_pose.py --camera 1
```

### Low FPS
- Ensure power supply is adequate (5V/5A)
- Check CPU temperature: `vcgencmd measure_temp`
- Close other applications
- Reduce resolution if needed

