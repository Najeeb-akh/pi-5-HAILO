# Hailo-Compatible Models Reference

## 📦 Model Selection for This Project

This document lists specific models available for Hailo-8L with download links, expected performance, and usage instructions.

---

## 🧍 Pose Estimation Models

### 1. YOLOv8-Pose (Recommended)

#### Model Variants
| Variant | Parameters | Input Size | Hailo FPS (est.) | Download |
|---------|------------|------------|------------------|----------|
| YOLOv8n-pose | 3.3M | 640×480 | 30-40 | [Model Zoo](https://github.com/hailo-ai/hailo_model_zoo) |
| YOLOv8s-pose | 11.6M | 640×480 | 20-30 | [Model Zoo](https://github.com/hailo-ai/hailo_model_zoo) |
| YOLOv8m-pose | 26.4M | 640×480 | 12-18 | [Model Zoo](https://github.com/hailo-ai/hailo_model_zoo) |

#### Features
- **Keypoints**: 17 body keypoints (COCO format)
- **Output**: Bounding boxes + pose coordinates
- **Accuracy**: High precision on diverse poses
- **Format**: Pre-compiled .hef available

#### Download Command
```bash
# Using Hailo Model Zoo
hailo model-zoo download yolov8s_pose --target hailo8l

# Direct download (check version)
wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/yolov8s_pose.hef
```

#### Expected Performance
- **Hailo-8L FPS**: 20-25 @ 640×480
- **CPU FPS**: 1-2 @ 640×480
- **Speedup**: ~15×
- **Latency**: 40-50ms per frame

---

### 2. MediaPipe Pose

#### Specifications
- **Input Size**: 256×256
- **Keypoints**: 33 body landmarks
- **Model Size**: ~3MB
- **Accuracy**: Excellent for single person

#### Performance Estimate
- **Hailo FPS**: 60-80 @ 256×256
- **CPU FPS**: 5-8 @ 256×256
- **Speedup**: ~10×

#### Notes
- Requires conversion from TensorFlow Lite → ONNX → HEF
- Smaller input = faster inference
- Better for close-up shots

---

### 3. YOLO-Pose (Original)

#### Specifications
- **Variants**: YOLO-Pose-S, YOLO-Pose-M, YOLO-Pose-L
- **Input Size**: 640×640
- **Based on**: YOLOv7 architecture

#### Availability
- May need manual compilation
- Check Hailo community repos
- Alternative to YOLOv8-pose

---

## 🎨 Segmentation Models

### 1. YOLOv8-Segmentation (Recommended)

#### Model Variants
| Variant | Parameters | Input Size | Hailo FPS (est.) | Download |
|---------|------------|------------|------------------|----------|
| YOLOv8n-seg | 3.4M | 640×640 | 25-30 | [Model Zoo](https://github.com/hailo-ai/hailo_model_zoo) |
| YOLOv8s-seg | 11.8M | 640×640 | 15-20 | [Model Zoo](https://github.com/hailo-ai/hailo_model_zoo) |
| YOLOv8m-seg | 27.3M | 640×640 | 8-12 | [Model Zoo](https://github.com/hailo-ai/hailo_model_zoo) |

#### Features
- **Task**: Instance segmentation (objects + masks)
- **Classes**: 80 COCO classes
- **Output**: Bounding boxes + pixel masks
- **Quality**: High mask accuracy

#### Download Command
```bash
# Using Hailo Model Zoo
hailo model-zoo download yolov8s_seg --target hailo8l

# Direct download
wget https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.11.0/hailo8l/yolov8s_seg.hef
```

#### Expected Performance
- **Hailo-8L FPS**: 15-20 @ 640×640
- **CPU FPS**: 0.5-1 @ 640×640
- **Speedup**: ~20-25×
- **Latency**: 50-70ms per frame

---

### 2. Fast-SCNN (Fast Semantic Segmentation)

#### Specifications
- **Input Size**: 512×512 or 1024×1024
- **Classes**: 19 (Cityscapes dataset)
- **Purpose**: Real-time semantic segmentation
- **Model Size**: ~1.1M parameters

#### Features
- Optimized for speed
- Good for street scene understanding
- Lower accuracy than DeepLab but much faster

#### Expected Performance
- **Hailo FPS**: 25-35 @ 512×512
- **CPU FPS**: 2-3 @ 512×512
- **Speedup**: ~12×

#### Download
```bash
# Check Hailo Model Zoo for availability
hailo model-zoo list | grep -i "fastseg\|fast-scnn"
```

---

### 3. DeepLabV3

#### Specifications
- **Backbone**: ResNet-50 or MobileNetV2
- **Input Size**: 513×513
- **Classes**: 21 (PASCAL VOC) or 19 (Cityscapes)
- **Accuracy**: High segmentation quality

#### Features
- State-of-the-art semantic segmentation
- Heavier than Fast-SCNN
- Better boundary detection

#### Expected Performance
- **Hailo FPS**: 8-15 @ 513×513
- **CPU FPS**: 0.3-0.8 @ 513×513
- **Speedup**: ~15-20×

---

## 📊 Model Comparison Summary

### For Pose Estimation - Choose YOLOv8s-pose
**Reasoning:**
- ✅ Official Hailo support
- ✅ Pre-compiled .hef available
- ✅ Good balance of speed/accuracy
- ✅ Extensive documentation
- ✅ Easy comparison with online benchmarks

### For Segmentation - Choose YOLOv8s-seg
**Reasoning:**
- ✅ Matches YOLOv8 family consistency
- ✅ Instance segmentation (more impressive visually)
- ✅ Clear performance metrics available
- ✅ Large speedup vs CPU
- ✅ Good documentation

### Alternative: Fast-SCNN as Second Segmentation Model
- Lighter weight
- Different approach (semantic vs instance)
- Good for comparison within segmentation task

---

## 🔗 Model Download Links

### Official Hailo Model Zoo
```bash
# Clone the model zoo repository
git clone https://github.com/hailo-ai/hailo_model_zoo.git
cd hailo_model_zoo

# List all available models for Hailo-8L
hailo model-zoo list --target hailo8l

# Download specific models
hailo model-zoo download yolov8s_pose --target hailo8l
hailo model-zoo download yolov8s_seg --target hailo8l
```

### Direct Downloads (S3 Bucket)
Base URL: `https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/`

**Check version** - Latest as of Nov 2024 is v2.11.0 or v2.12.0

#### Pose Estimation
```
v2.11.0/hailo8l/yolov8n_pose.hef
v2.11.0/hailo8l/yolov8s_pose.hef
v2.11.0/hailo8l/yolov8m_pose.hef
```

#### Segmentation
```
v2.11.0/hailo8l/yolov8n_seg.hef
v2.11.0/hailo8l/yolov8s_seg.hef
v2.11.0/hailo8l/fastseg_resnet18.hef
```

---

## 🛠️ Model Compilation (Advanced)

If you want to compile custom models or different versions:

### Requirements
- Hailo Dataflow Compiler (DFC)
- ONNX or TensorFlow model file
- Calibration dataset (for quantization)

### Basic Compilation Flow
```bash
# 1. Convert to ONNX (if needed)
# PyTorch example:
torch.onnx.export(model, dummy_input, "model.onnx")

# 2. Compile for Hailo-8L
hailo compiler compile \
    --model model.onnx \
    --hw-arch hailo8l \
    --output model.hef \
    --batch-size 1 \
    --performance

# 3. Test the compiled model
hailortcli run model.hef
```

### Note
- Compilation requires Hailo Developer License (free registration)
- Most users should use pre-compiled models from Model Zoo
- Compilation process can be complex for custom models

---

## 📈 Benchmark Reference Data

### From Hailo Official Documentation

#### Hailo-8L (13 TOPS)
| Model | Task | Resolution | FPS |
|-------|------|------------|-----|
| YOLOv5s | Detection | 640×640 | 30 |
| YOLOv8n | Detection | 640×640 | 45 |
| YOLOv8s-pose | Pose | 640×640 | 22 |
| YOLOv8s-seg | Segmentation | 640×640 | 18 |
| ResNet50 | Classification | 224×224 | 280 |

#### Raspberry Pi 5 CPU (4× Cortex-A76)
| Model | Task | Resolution | FPS |
|-------|------|------------|-----|
| YOLOv5s | Detection | 640×640 | 2.5 |
| YOLOv8n | Detection | 640×640 | 3.2 |
| YOLOv8s-pose | Pose | 640×640 | 1.5 |
| YOLOv8s-seg | Segmentation | 640×640 | 0.8 |
| ResNet50 | Classification | 224×224 | 18 |

**Source**: Hailo official benchmarks, Pi 5 specs

---

## 🎯 Recommended Setup for Your Project

### Primary Models to Use

1. **Pose Estimation**: YOLOv8s-pose
   - Good balance of speed/accuracy
   - ~22 FPS on Hailo-8L
   - ~1.5 FPS on Pi5 CPU
   - **Speedup: ~15×**

2. **Segmentation**: YOLOv8s-seg
   - Instance segmentation
   - ~18 FPS on Hailo-8L
   - ~0.8 FPS on Pi5 CPU
   - **Speedup: ~22×**

### Why These Specific Models?
- ✅ Both from same YOLO family (consistency)
- ✅ Pre-compiled HEF files available
- ✅ Extensive documentation
- ✅ Reference benchmarks available online
- ✅ Good visual results for demos
- ✅ Significant speedup (15-22×)
- ✅ Real-time capable on Hailo

---

## 📚 Additional Resources

### Model Documentation
- [YOLOv8 Documentation](https://docs.ultralytics.com/models/yolov8/)
- [Hailo Model Zoo GitHub](https://github.com/hailo-ai/hailo_model_zoo)
- [COCO Dataset Keypoint Format](https://cocodataset.org/#keypoints-2020)

### Benchmarks and Comparisons
- [Hailo Developer Zone](https://hailo.ai/developer-zone/)
- [Papers With Code - Pose Estimation](https://paperswithcode.com/task/pose-estimation)
- [Papers With Code - Semantic Segmentation](https://paperswithcode.com/task/semantic-segmentation)

### Community Projects
- Hailo Community Forum: community.hailo.ai
- GitHub: Search "hailo raspberry pi pose" / "hailo segmentation"
- YouTube: "Hailo AI HAT benchmark" videos

