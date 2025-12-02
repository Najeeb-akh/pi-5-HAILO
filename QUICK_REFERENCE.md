# Quick Reference Guide - Graphs & Demos

## 📊 View Generated Graphs

```bash
# Navigate to graphs directory
cd /home/admin/Desktop/Najeeb/results/graphs

# List all graphs
ls -lh *.png

# Open a graph (if desktop environment available)
xdg-open fps_comparison.png
```

**Available Graphs:**
- `fps_comparison.png` - Performance overview
- `latency_comparison.png` - Latency analysis  
- `speedup_comparison.png` - Acceleration metrics
- `benchmark_dashboard.png` - Comprehensive dashboard
- `task_category_analysis.png` - Task comparison
- `realtime_capability.png` - Real-time achievement

---

## 📄 View PDF Catalog

```bash
# Open demo catalog
cd /home/admin/Desktop/Najeeb
xdg-open results/DEMO_CATALOG.pdf

# Or copy to desktop for easy access
cp results/DEMO_CATALOG.pdf ~/Desktop/
```

**Catalog Contents:** 8 pages with graphs, video guides, and instructions

---

## 🎥 Record Quick Demo

```bash
# Navigate to project root
cd /home/admin/Desktop/Najeeb

# Option 1: Just run the demo (watch output)
./quick_demo_capture.sh

# Option 2: Record with asciinema (terminal recording)
asciinema rec demo.cast
./quick_demo_capture.sh
# Press Ctrl+D when done

# Option 3: Screen record while running
# Start your screen recorder, then:
./quick_demo_capture.sh
```

---

## 🔄 Regenerate Assets

```bash
cd /home/admin/Desktop/Najeeb

# Regenerate all graphs
python3 generate_benchmark_graphs.py

# Regenerate PDF catalog
python3 create_demo_catalog.py
```

---

## 📖 Read Documentation

```bash
cd /home/admin/Desktop/Najeeb

# View demo video scripts
cat demo_video_scripts.md | less

# View visualization summary
cat VISUALIZATION_DEMO_SUMMARY.md | less

# View final project documentation
cat FINAL_PROJECT_DOCUMENTATION.md | less

# View benchmark results
cat results/benchmarks/BENCHMARK_RESULTS.md | less
```

---

## 📁 Key File Locations

| What | Where |
|------|-------|
| Graphs | `results/graphs/*.png` |
| PDF Catalog | `results/DEMO_CATALOG.pdf` |
| Video Scripts | `demo_video_scripts.md` |
| Demo Tool | `quick_demo_capture.sh` |
| Benchmark Results | `results/benchmarks/BENCHMARK_RESULTS.md` |
| Documentation | `FINAL_PROJECT_DOCUMENTATION.md` |

---

## 🚀 Quick Commands Cheat Sheet

```bash
# Project root
cd /home/admin/Desktop/Najeeb

# List all graphs with sizes
ls -lh results/graphs/*.png

# List all important files
ls -lh *.md *.sh *.py results/*.pdf

# Run demo
./quick_demo_capture.sh

# Generate graphs
python3 generate_benchmark_graphs.py

# Generate PDF
python3 create_demo_catalog.py

# View file tree
tree -L 3 -h

# Check project size
du -sh .
du -sh results/
```

---

## 💡 Tips

**For Presentations:**
- Use `benchmark_dashboard.png` for overview slides
- Use individual graphs for detailed analysis
- Reference `DEMO_CATALOG.pdf` for comprehensive view

**For Recording:**
- Test `./quick_demo_capture.sh` before recording
- Use asciinema for terminal recordings
- Use simplescreenrecorder for screen capture

**For Sharing:**
- Graphs are 300 DPI (print quality)
- PDF is 1.9 MB (email-friendly)
- All assets in `results/` directory

---

## 🎯 What to Include in Final Submission

✅ **Essential:**
- `FINAL_PROJECT_DOCUMENTATION.md` - Complete project record
- `results/benchmarks/BENCHMARK_RESULTS.md` - Detailed results
- `results/DEMO_CATALOG.pdf` - Visual catalog

✅ **Highly Recommended:**
- `results/graphs/*.png` - All 6 visualization graphs
- `VISUALIZATION_DEMO_SUMMARY.md` - Assets overview

✅ **Optional but Impressive:**
- Demo videos (if recorded)
- `quick_demo_capture.sh` - Demo automation
- `generate_benchmark_graphs.py` - Graph generator script

---

## 📊 Graph Descriptions (for captions)

**fps_comparison.png:**
> "Figure 1: FPS performance comparison between CPU baseline and Hailo-8L AI HAT across five different computer vision models. All Hailo-accelerated models exceed the 15 FPS real-time threshold (green dashed line)."

**latency_comparison.png:**
> "Figure 2: Inference latency comparison on logarithmic scale. Hailo-8L achieves 13-20ms latency compared to CPU baseline of 150-1250ms, representing a 7-87× reduction."

**speedup_comparison.png:**
> "Figure 3: Speedup factors achieved with Hailo-8L acceleration. Dense prediction tasks (segmentation, pose estimation, detection) show 29-80× speedup, while classification shows 7× speedup."

**benchmark_dashboard.png:**
> "Figure 4: Comprehensive performance dashboard showing FPS, latency, speedup factors, and summary statistics across all tested models."

**task_category_analysis.png:**
> "Figure 5: Performance analysis by task category. Dense prediction tasks average 46.3× speedup while classification tasks achieve 7.0× speedup, demonstrating Hailo's optimization for spatially dense outputs."

**realtime_capability.png:**
> "Figure 6: Real-time capability achievement chart. Color-coded visualization shows all models achieving real-time performance (>15 FPS) with Hailo acceleration, compared to CPU baseline where no models reach real-time threshold."

---

## 🎬 Recording Tips

**Terminal Demo:**
```bash
# Install asciinema if needed
sudo apt install asciinema

# Record demo
asciinema rec -t "Hailo AI HAT Demo" demo.cast
./quick_demo_capture.sh
# Ctrl+D to stop

# Play back
asciinema play demo.cast

# Upload (optional)
asciinema upload demo.cast
```

**Screen Recording:**
```bash
# Install recorder if needed
sudo apt install simplescreenrecorder

# Or use command line
ffmpeg -f x11grab -framerate 25 -s 1920x1080 -i :0.0 \
       -c:v libx264 -preset fast output.mp4
```

---

## ✅ Checklist Before Submission

- [ ] All 6 graphs generated in `results/graphs/`
- [ ] `DEMO_CATALOG.pdf` created and reviewed
- [ ] `FINAL_PROJECT_DOCUMENTATION.md` includes Section 6
- [ ] Benchmark results documented in `BENCHMARK_RESULTS.md`
- [ ] All files organized in proper directories
- [ ] Optional: Demo video(s) recorded
- [ ] Optional: Demo script tested

---

**Project:** Hailo AI HAT Performance Benchmark  
**Date:** November 24, 2025  
**Status:** ✅ All assets complete and ready for submission!

For detailed information, see:
- `VISUALIZATION_DEMO_SUMMARY.md` - Complete overview
- `demo_video_scripts.md` - Video recording guide
- `results/graphs/README.md` - Graph documentation

