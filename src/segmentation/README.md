# Segmentation Benchmark

## Overview
This module benchmarks YOLOv8-Seg (instance segmentation) model performance on Raspberry Pi 5 with and without Hailo acceleration.

## Models Required

### Hailo Model (.hef)
Download the pre-compiled model:
```bash
cd models/
wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/yolov8s_seg.hef
```

### CPU Model (.onnx) - Optional
For CPU baseline comparison:
```bash
pip install ultralytics
python -c "from ultralytics import YOLO; model = YOLO('yolov8s-seg.pt'); model.export(format='onnx')"
mv yolov8s-seg.onnx models/
```

## Usage

### Run Both CPU and Hailo Benchmarks
```bash
python benchmark_segmentation.py --mode both --iterations 100 --display
```

### Run Hailo Only
```bash
python benchmark_segmentation.py --mode hailo --iterations 200
```

### Run CPU Only
```bash
python benchmark_segmentation.py --mode cpu --iterations 50
```

### Use Video File
```bash
python benchmark_segmentation.py --video /path/to/video.mp4
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
- **FPS**: 15-20
- **Latency**: 50-67 ms
- **CPU Usage**: 15-25%

### Raspberry Pi 5 CPU Only
- **FPS**: 0.6-0.9
- **Latency**: 1100-1600 ms
- **CPU Usage**: 98-99%

### Speedup: ~18-25×

Segmentation is the most compute-intensive task, so it shows the **highest speedup** with Hailo acceleration.

## Output Files

Results are saved to `../../results/benchmarks/`:

- `segmentation_benchmark_YYYYMMDD_HHMMSS.json` - Detailed metrics
- `segmentation_benchmark_results.csv` - Appended results for comparison

## Model Details

### YOLOv8-Seg
- **Task**: Instance segmentation
- **Input**: 640×640 RGB
- **Output**: 
  - Bounding boxes for detected objects
  - Segmentation masks for each instance
- **Classes**: 80 COCO classes

### Why Segmentation?
Segmentation is the **most demanding** computer vision task:
- Pixel-level classification (640×640 = 409,600 predictions per frame)
- Object detection + mask generation
- Heavy computational load

This makes it the **perfect benchmark** to demonstrate Hailo's power:
- CPU struggles to achieve even 1 FPS
- Hailo enables real-time 15-20 FPS
- Shows 20-25× speedup

## Troubleshooting

### Model Not Found
```bash
# Download models
cd models/
wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/yolov8s_seg.hef
```

### Out of Memory
Segmentation uses more memory. Ensure:
- 4GB+ RAM on Pi 5
- Close other applications
- Reduce `--iterations` if needed

### Very Low CPU FPS
This is **expected**! Segmentation is extremely slow on CPU.
- 0.6-0.9 FPS is normal
- Use `--iterations 50` for faster CPU benchmarking
- This demonstrates why Hailo is necessary

