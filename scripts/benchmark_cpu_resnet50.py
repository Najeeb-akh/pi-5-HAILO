#!/usr/bin/env python3
"""
CPU-only ResNet50 benchmark using OpenCV DNN
Minimal, lightweight CPU baseline for comparison with Hailo
"""

import cv2
import numpy as np
import time

def benchmark_resnet50_cpu(num_frames=100):
    """Run ResNet50 inference on CPU using OpenCV DNN"""
    
    print("=" * 70)
    print("CPU Baseline Benchmark: ResNet50 Image Classification")
    print("=" * 70)
    print()
    
    # Load ResNet50 from OpenCV's model zoo
    print("📥 Loading ResNet50 model...")
    model_url = "https://github.com/onnx/models/raw/main/validated/vision/classification/resnet/model/resnet50-v1-7.onnx"
    model_path = "/tmp/resnet50_cpu.onnx"
    
    # Download if needed
    import urllib.request
    import os
    if not os.path.exists(model_path):
        print(f"   Downloading model from {model_url}")
        print("   (This is a one-time download, ~100MB)")
        urllib.request.urlretrieve(model_url, model_path)
        print("   ✅ Download complete")
    else:
        print(f"   ✅ Using cached model: {model_path}")
    
    # Load with OpenCV DNN
    net = cv2.dnn.readNetFromONNX(model_path)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    print("✅ Model loaded\n")
    
    # Prepare synthetic input (224x224x3, standard ImageNet size)
    print(f"🎯 Running {num_frames} inference iterations...")
    print(f"   Input size: 224x224x3 (RGB)")
    print()
    
    input_blob = np.random.randint(0, 255, (1, 3, 224, 224)).astype(np.float32)
    
    # Warmup (first run is always slower)
    for _ in range(3):
        net.setInput(input_blob)
        _ = net.forward()
    
    # Benchmark
    latencies = []
    start_total = time.perf_counter()
    
    for i in range(num_frames):
        start = time.perf_counter()
        net.setInput(input_blob)
        _ = net.forward()
        end = time.perf_counter()
        
        latency_ms = (end - start) * 1000
        latencies.append(latency_ms)
        
        if (i + 1) % 10 == 0:
            print(f"   Progress: {i+1}/{num_frames} frames...")
    
    end_total = time.perf_counter()
    total_time = end_total - start_total
    
    # Results
    fps = num_frames / total_time
    avg_latency = np.mean(latencies)
    min_latency = np.min(latencies)
    max_latency = np.max(latencies)
    
    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Total frames:        {num_frames}")
    print(f"Total time:          {total_time:.2f} seconds")
    print(f"FPS (CPU-only):      {fps:.2f} frames/second")
    print(f"Avg Latency:         {avg_latency:.2f} ms")
    print(f"Min Latency:         {min_latency:.2f} ms")
    print(f"Max Latency:         {max_latency:.2f} ms")
    print()
    
    print("=" * 70)
    print("COMPARISON WITH HAILO")
    print("=" * 70)
    hailo_fps = 47.33  # From previous benchmark
    speedup = hailo_fps / fps
    print(f"Hailo-8L FPS:        {hailo_fps:.2f}")
    print(f"CPU FPS:             {fps:.2f}")
    print(f"Speedup:             {speedup:.1f}×")
    print("=" * 70)
    
    return fps, avg_latency

if __name__ == "__main__":
    fps, latency = benchmark_resnet50_cpu(num_frames=100)

