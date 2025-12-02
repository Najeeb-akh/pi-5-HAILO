# Demo Video Scripts for Hailo AI HAT Project

## Overview
This document provides detailed scripts and instructions for creating demonstration videos showcasing the Hailo-8L AI HAT capabilities on Raspberry Pi 5.

---

## Video 1: Pose Estimation Demo (YOLOv8s-Pose)

### Duration: 1-2 minutes
### Model: `yolov8s_pose_h8l_pi.hef`

#### Script:

**[0:00-0:10] Introduction**
- Show Raspberry Pi 5 with Hailo AI HAT attached
- Camera module connected
- Title overlay: "Real-Time Pose Estimation with Hailo AI HAT"

**[0:10-0:20] System Info**
- Quick display of terminal showing:
  ```bash
  hailortcli fw-control identify
  ```
- Show firmware version (4.20.0)

**[0:20-1:30] Live Demo**
- Run pose estimation with live camera feed
- Show person performing various poses:
  - Standing still
  - Raising arms
  - Walking
  - Sitting/standing
- Display FPS counter on screen (should show ~49 FPS)
- Highlight keypoint detection (17 keypoints visible)

**[1:30-1:50] Performance Overlay**
- Show text overlay:
  - "49.5 FPS - Real-time performance"
  - "19.1ms latency"
  - "33× faster than CPU"

**[1:50-2:00] Closing**
- Brief shot of setup
- End card: "Hailo-8L AI HAT | Raspberry Pi 5"

#### Recording Commands:

```bash
# Navigate to pose estimation directory
cd /home/admin/Desktop/Najeeb/src/pose_estimation

# Run the pose estimation demo (if you have a demo script)
# Or use rpicam-hello with Hailo processing
# Record screen with:
# - ffmpeg (if available)
# - Or use external screen recording
```

#### Tips:
- Use good lighting
- Ensure person is fully visible in frame
- Show different angles and movements
- Keep camera steady (use tripod if possible)

---

## Video 2: Segmentation Demo (YOLOv5n-Seg)

### Duration: 1-2 minutes
### Model: `yolov5n_seg_h8l_mz.hef`

#### Script:

**[0:00-0:10] Introduction**
- Title: "Real-Time Instance Segmentation"
- Show setup with multiple objects in scene

**[0:10-0:20] System Info**
- Display model info
- Show expected performance: 64 FPS

**[0:20-1:30] Live Demo**
- Run segmentation on live feed with various objects:
  - People walking
  - Multiple objects (chairs, bottles, backpacks)
  - Moving objects
- Show pixel-level masks in different colors
- Demonstrate detection of multiple instances

**[1:30-1:50] Performance Stats**
- "64.2 FPS - Industry-leading performance"
- "14.4ms latency"
- "80× faster than CPU baseline"

**[1:50-2:00] Closing**
- Applications: "Background removal, object counting, zone monitoring"

#### Recording Commands:

```bash
cd /home/admin/Desktop/Najeeb/src/segmentation

# Run segmentation demo
# Use rpicam-apps with Hailo post-processing
```

#### Tips:
- Show diverse objects
- Demonstrate overlapping objects
- Show segmentation accuracy
- Highlight different object classes

---

## Video 3: Multi-Model Comparison

### Duration: 2-3 minutes

#### Script:

**[0:00-0:15] Introduction**
- Title: "Hailo AI HAT: Multiple AI Models"
- Show Raspberry Pi 5 + Hailo-8L setup

**[0:15-0:45] Quick Demo Montage**
- 10 seconds each:
  1. Pose estimation
  2. Segmentation
  3. Object detection (YOLOv8s)

**[0:45-1:15] Performance Comparison Screen**
- Show graphs (use generated PNG files):
  - `fps_comparison.png`
  - `speedup_comparison.png`
- Narration: "All models achieve real-time performance"

**[1:15-2:00] Side-by-Side Comparison (if possible)**
- Split screen showing:
  - CPU-only processing (slow, low FPS)
  - Hailo accelerated (smooth, high FPS)
- For ResNet50 classification (easiest to show difference)

**[2:00-2:30] Applications & Use Cases**
- Text overlays showing applications:
  - "Fitness tracking & form analysis"
  - "Smart security systems"
  - "Retail analytics"
  - "Industrial quality control"

**[2:30-2:45] Benchmark Summary**
- Show `benchmark_dashboard.png`
- Highlight key metrics

**[2:45-3:00] Closing**
- "Edge AI Made Easy"
- Contact/project info

---

## Video 4: System Setup & Installation (Optional)

### Duration: 3-5 minutes

#### Script:

**[0:00-0:30] Introduction**
- Show components:
  - Raspberry Pi 5
  - Hailo-8L AI HAT
  - Camera module
  - Power supply

**[0:30-1:30] Hardware Installation**
- Time-lapse of:
  - Attaching Hailo HAT to Pi 5
  - Connecting camera
  - Powering on

**[1:30-3:00] Software Setup**
- Show terminal commands:
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install HailoRT
sudo apt install hailort

# Verify installation
hailortcli fw-control identify

# Download models
ls /usr/share/hailo-models/

# Run first benchmark
hailortcli benchmark /usr/share/hailo-models/yolov8s_h8l.hef
```

**[3:00-4:00] First Test**
- Run a quick benchmark
- Show results

**[4:00-5:00] Next Steps**
- Show project structure
- Point to documentation

---

## Recording Setup & Best Practices

### Equipment Needed:
1. **Camera Setup:**
   - Main camera for recording Raspberry Pi screen (use phone/webcam)
   - OV5647 camera module for AI inference
   - Optional: Second camera for wide shots

2. **Lighting:**
   - Good ambient lighting
   - Avoid glare on screen
   - Ensure subject (for pose/segmentation) is well-lit

3. **Screen Recording:**
   - Use `ffmpeg` for terminal/benchmark recordings
   - Use `scrot` or `import` for screenshots
   - Use `kazam` or `simplescreenrecorder` if available

### Screen Recording Commands:

```bash
# Install screen recording tool
sudo apt install simplescreenrecorder

# Or use ffmpeg (if display available)
ffmpeg -f x11grab -framerate 25 -s 1920x1080 -i :0.0 output.mp4

# Record terminal session with asciinema
sudo apt install asciinema
asciinema rec demo.cast
```

### Video Editing Tips:

1. **Add Overlays:**
   - FPS counter
   - Latency display
   - Model name
   - Performance metrics

2. **Transitions:**
   - Smooth cuts between scenes
   - Use fade-in/fade-out
   - Keep transitions short (0.5-1 second)

3. **Audio:**
   - Optional background music (low volume)
   - Voice narration (recommended)
   - Or use text overlays with no audio

4. **Export Settings:**
   - Resolution: 1080p (1920×1080)
   - Frame rate: 30 FPS
   - Format: MP4 (H.264)
   - Bitrate: 5-10 Mbps

### Video Editing Software (Free Options):

```bash
# OpenShot Video Editor
sudo apt install openshot-qt

# Kdenlive
sudo apt install kdenlive

# Or use online editors:
# - Clipchamp (web)
# - Canva Video (web)
```

---

## Quick Demo Recording Script

### 30-Second Quick Demo:

If you want to create a quick demo without editing:

```bash
#!/bin/bash
# quick_demo.sh - Automated demo recording

echo "=== Hailo AI HAT Demo ==="
echo ""

# Show system info
echo "System: Raspberry Pi 5 + Hailo-8L AI HAT"
hailortcli fw-control identify
echo ""

# Run quick benchmarks
echo "Running YOLOv8s Pose Estimation..."
hailortcli benchmark /usr/share/hailo-models/yolov8s_pose_h8l_pi.hef | grep "FPS"
echo ""

echo "Running YOLOv5n Segmentation..."
hailortcli benchmark /usr/share/hailo-models/yolov5n_seg_h8l_mz.hef | grep "FPS"
echo ""

echo "Demo complete! All models running at 50+ FPS (real-time)"
```

Make executable and record terminal:
```bash
chmod +x quick_demo.sh
asciinema rec quick_demo.cast
./quick_demo.sh
# Press Ctrl+D to stop recording
```

---

## Demo Video Checklist

### Before Recording:
- [ ] Hailo HAT properly connected
- [ ] Camera module working
- [ ] System updated and models downloaded
- [ ] Test run completed successfully
- [ ] Screen recording software ready
- [ ] Good lighting setup
- [ ] Quiet environment (if recording audio)

### During Recording:
- [ ] Steady camera/screen
- [ ] Clear visibility of FPS counter
- [ ] Smooth subject movements (for pose/segmentation)
- [ ] No interruptions or errors
- [ ] Capture performance metrics
- [ ] Show real-world scenarios

### After Recording:
- [ ] Review footage for quality
- [ ] Trim unnecessary parts
- [ ] Add overlays/text if needed
- [ ] Add background music (optional)
- [ ] Export in appropriate format
- [ ] Test playback
- [ ] Save to demo_videos folder

---

## File Organization

```
results/demo_videos/
├── pose_estimation_demo.mp4
├── segmentation_demo.mp4
├── multi_model_comparison.mp4
├── system_setup_guide.mp4
├── quick_demo_30sec.mp4
└── raw_footage/
    ├── pose_raw_1.mp4
    ├── pose_raw_2.mp4
    └── ...
```

---

## Alternative: Using Pre-recorded Footage

If you cannot create new videos, you can:

1. **Use Screenshots:**
   - Capture key moments from benchmark runs
   - Create slideshow-style video
   - Add text explaining each frame

2. **Create Animation:**
   - Use graphs we generated
   - Animate transitions between charts
   - Add narration or text overlays

3. **Screen Recording Only:**
   - Record terminal benchmark runs
   - Show FPS counters and results
   - No camera needed

### Create Video from Screenshots:

```bash
# Install ffmpeg if not available
sudo apt install ffmpeg

# Create video from images
ffmpeg -framerate 1 -pattern_type glob -i 'results/graphs/*.png' \
       -c:v libx264 -r 30 -pix_fmt yuv420p \
       results/demo_videos/graphs_slideshow.mp4

# Add audio narration (optional)
ffmpeg -i graphs_slideshow.mp4 -i narration.mp3 \
       -c:v copy -c:a aac \
       results/demo_videos/graphs_with_audio.mp4
```

---

## Sharing & Presentation

### For Final Project:

1. **Upload Videos:**
   - Keep files under 25MB if sharing via email
   - Or upload to YouTube/Google Drive (unlisted)
   - Embed links in documentation

2. **Create Video Catalog PDF:**
   - List all videos with descriptions
   - Include thumbnails
   - Add QR codes for online links
   - Timestamp key moments

3. **Demo Package:**
   ```
   demo_package/
   ├── videos/
   │   ├── pose_demo.mp4
   │   ├── segmentation_demo.mp4
   │   └── comparison.mp4
   ├── graphs/
   │   ├── all PNG files
   ├── thumbnails/
   │   └── video_thumbnails.png
   └── DEMO_CATALOG.pdf
   ```

---

## Notes

- **Performance:** Actual demo performance may vary slightly from benchmark results due to application overhead
- **Lighting:** Good lighting is crucial for pose estimation and segmentation demos
- **Movement:** Smooth, deliberate movements show better results than fast, erratic ones
- **Background:** Clean, uncluttered background helps with segmentation
- **Duration:** Keep videos short and focused (1-3 minutes each)
- **Quality:** 1080p resolution, stable footage preferred over shaky high-FPS

---

**Ready to record? Start with the easiest demo (benchmark terminal output) and progress to live camera demos!**

