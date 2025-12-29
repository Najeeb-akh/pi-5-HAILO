# Hand Landmark Detection - End-to-End Demo

## Overview
This module implements hand landmark detection using **MediaPipe Hands** (NOT from Hailo Zoo). It extracts comprehensive parameters including FPS, latency, landmark coordinates, finger angles, and bounding boxes.

## Key Features

- ✅ **Not from Hailo Zoo** - Uses MediaPipe Hands (independent model)
- ✅ **21 Landmarks per Hand** - Full hand keypoint detection
- ✅ **Parameter Extraction** - FPS, latency, coordinates, angles, bounding boxes
- ✅ **End-to-End Demo** - Complete pipeline from camera to results
- ✅ **Real-time Visualization** - Live landmark overlay on video feed
- ✅ **Results Export** - JSON output with all parameters

## Models Used

### MediaPipe Hands
- **Source**: Google MediaPipe (NOT Hailo Zoo)
- **Landmarks**: 21 per hand (wrist, thumb, index, middle, ring, pinky)
- **Input**: RGB image (any resolution, auto-resized)
- **Output**: 3D landmark coordinates (x, y, z)
- **Max Hands**: 2 (configurable)

## Installation

### Dependencies
```bash
pip3 install mediapipe opencv-python numpy --break-system-packages
```

### Verify Installation
```bash
python3 -c "import mediapipe; print('✅ MediaPipe installed')"
```

## Usage

### Basic Demo (100 frames)
```bash
cd /home/admin/Desktop/Najeeb
python3 src/hand_landmarks/hand_landmark_demo.py --frames 100
```

### Custom Camera and Frame Count
```bash
python3 src/hand_landmarks/hand_landmark_demo.py --camera 0 --frames 200
```

### Without Saving Results
```bash
python3 src/hand_landmarks/hand_landmark_demo.py --frames 50 --no-save
```

## Command Line Options

- `--camera`: Camera device ID (default: 0)
- `--frames`: Number of frames to process (default: 100)
- `--no-save`: Do not save results to JSON file

## Parameters Extracted

### Performance Metrics
- **FPS**: Average frames per second
- **Latency**: Average, min, max inference time (ms)
- **Total Time**: Total processing time

### Detection Metrics
- **Number of Hands**: Detected hands per frame
- **Detection Rate**: Percentage of frames with hands detected
- **Landmarks per Hand**: Average number of landmarks detected

### Hand Parameters (per frame)
- **21 Landmark Coordinates**: (x, y, z) for each landmark
  - Wrist (1)
  - Thumb (4)
  - Index finger (4)
  - Middle finger (4)
  - Ring finger (4)
  - Pinky (4)
- **Finger Angles**: Calculated angles between key points
- **Bounding Box**: (x_min, y_min, x_max, y_max, width, height)

## Output Files

Results are saved to `../../results/benchmarks/`:

- `hand_landmarks_YYYYMMDD_HHMMSS.json` - Complete results with:
  - Performance metrics (FPS, latency)
  - Sample parameters (first 10 frames)
  - All latency measurements
  - Timestamp

## Expected Performance

### Raspberry Pi 5 (CPU-only)
- **FPS**: 15-25 frames/second
- **Latency**: 40-70 ms per frame
- **CPU Usage**: 30-50%
- **Accuracy**: High (MediaPipe optimized for edge devices)

### Comparison with Hailo Models
- **MediaPipe Hands**: CPU-based, no Hailo acceleration
- **Purpose**: Demonstrate end-to-end demo with non-Hailo-Zoo model
- **Advantage**: Easy to implement, good accuracy, real-time capable

## Example Output

```
======================================================================
Hand Landmark Detection - End-to-End Demo
======================================================================

✅ Camera opened
📊 Running 100 frames...

🔥 Warmup complete, starting benchmark...

   Progress: 10/100 frames...
   Progress: 20/100 frames...
   ...

======================================================================
RESULTS
======================================================================
Total frames processed:  100
Total time:              4.23 seconds
Average FPS:             23.64 frames/second
Average latency:         42.30 ms
Min latency:             38.50 ms
Max latency:             52.10 ms

Frames with hands:       87/100
Detection rate:          87.0%
Avg landmarks per hand:  21.0
======================================================================

✅ Results saved to: results/benchmarks/hand_landmarks_20250101_120000.json
```

## Landmark Index Reference

MediaPipe Hands provides 21 landmarks per hand:

```
0: Wrist
1-4: Thumb (CMC, MCP, IP, Tip)
5-8: Index Finger (MCP, PIP, DIP, Tip)
9-12: Middle Finger (MCP, PIP, DIP, Tip)
13-16: Ring Finger (MCP, PIP, DIP, Tip)
17-20: Pinky (MCP, PIP, DIP, Tip)
```

## Troubleshooting

### Camera Not Opening
```bash
# Check available cameras
rpicam-hello --list-cameras

# Try different camera ID
python3 src/hand_landmarks/hand_landmark_demo.py --camera 1
```

### MediaPipe Installation Issues
```bash
# Install with specific version
pip3 install mediapipe==0.10.8 --break-system-packages
```

### Low FPS
- Reduce input resolution (MediaPipe auto-resizes)
- Lower `max_num_hands` parameter
- Close other applications

## Integration with Project

This module demonstrates:
1. ✅ **Non-Hailo-Zoo Model** - Uses MediaPipe (independent source)
2. ✅ **Parameter Extraction** - Comprehensive metrics collection
3. ✅ **End-to-End Demo** - Complete pipeline implementation
4. ✅ **Results Documentation** - JSON export for analysis

## Next Steps (Optional)

### Compile for Hailo
If you want to accelerate MediaPipe Hands with Hailo:
1. Export MediaPipe Hands to ONNX
2. Compile with Hailo compiler:
   ```bash
   hailomc compile hand_landmarks.onnx --hw-arch hailo8l --output hand_landmarks.hef
   ```
3. Use Hailo Python API for inference

### Compare Performance
- Run MediaPipe Hands (CPU) vs. compiled Hailo version
- Measure speedup and accuracy differences

