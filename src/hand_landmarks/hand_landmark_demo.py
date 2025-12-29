#!/usr/bin/env python3
"""
Hand Landmark Detection - End-to-End Demo
Uses MediaPipe Hands (NOT from Hailo Zoo)
Extracts parameters: FPS, latency, landmark coordinates, finger angles
"""

import cv2
import mediapipe as mp
import numpy as np
import time
import json
from datetime import datetime


class HandLandmarkDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
    def detect(self, image):
        """Detect hand landmarks in image"""
        start_time = time.perf_counter()
        
        # Convert BGR to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process
        results = self.hands.process(rgb_image)
        
        latency_ms = (time.perf_counter() - start_time) * 1000
        
        return results, latency_ms
    
    def extract_parameters(self, results, image_shape):
        """Extract parameters from detection results"""
        params = {
            'num_hands': 0,
            'landmarks': [],
            'finger_angles': [],
            'hand_bbox': []
        }
        
        if results.multi_hand_landmarks:
            params['num_hands'] = len(results.multi_hand_landmarks)
            
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract 21 landmark coordinates
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append({
                        'x': lm.x * image_shape[1],  # Convert to pixel coordinates
                        'y': lm.y * image_shape[0],
                        'z': lm.z
                    })
                params['landmarks'].append(landmarks)
                
                # Calculate finger angles (example: thumb angle)
                if len(landmarks) >= 4:
                    # Thumb angle (using landmarks 0, 2, 4)
                    angle = self._calculate_angle(
                        landmarks[0], landmarks[2], landmarks[4]
                    )
                    params['finger_angles'].append(angle)
                
                # Calculate bounding box
                xs = [lm['x'] for lm in landmarks]
                ys = [lm['y'] for lm in landmarks]
                params['hand_bbox'].append({
                    'x_min': min(xs),
                    'y_min': min(ys),
                    'x_max': max(xs),
                    'y_max': max(ys),
                    'width': max(xs) - min(xs),
                    'height': max(ys) - min(ys)
                })
        
        return params
    
    def _calculate_angle(self, p1, p2, p3):
        """Calculate angle between three points"""
        v1 = np.array([p1['x'] - p2['x'], p1['y'] - p2['y']])
        v2 = np.array([p3['x'] - p2['x'], p3['y'] - p2['y']])
        
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
        return np.degrees(angle)
    
    def draw_landmarks(self, image, results):
        """Draw landmarks on image"""
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
        return image


def run_demo(camera_id=0, num_frames=100, save_results=True, video_file=None):
    """Run end-to-end hand landmark detection demo"""
    
    print("=" * 70)
    print("Hand Landmark Detection - End-to-End Demo")
    print("=" * 70)
    print()
    
    # Initialize detector
    detector = HandLandmarkDetector()
    
    # Open camera or video file
    if video_file:
        print(f"📹 Using video file: {video_file}")
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            print(f"❌ Error: Could not open video file {video_file}")
            return
        # Get total frames from video if available
        total_video_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_video_frames > 0 and num_frames > total_video_frames:
            num_frames = total_video_frames
            print(f"   Video has {total_video_frames} frames, using all of them")
    else:
        # Try different backends for Raspberry Pi camera
        backends = [
            (cv2.CAP_V4L2, "V4L2"),
            (cv2.CAP_ANY, "ANY"),
        ]
        cap = None
        for backend_id, backend_name in backends:
            try:
                cap = cv2.VideoCapture(camera_id, backend_id)
                if cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        print(f"✅ Camera opened using {backend_name} backend")
                        break
                    else:
                        cap.release()
                        cap = None
            except:
                if cap:
                    cap.release()
                cap = None
        
        if not cap or not cap.isOpened():
            print(f"❌ Error: Could not open camera {camera_id}")
            print("   Tip: Try using a video file with --video option")
            print("   Or use rpicam-vid to record a video first")
            return
    
    print(f"📊 Running {num_frames} frames...")
    print()
    
    # Metrics
    latencies = []
    all_parameters = []
    frame_count = 0
    start_total = time.perf_counter()
    
    # Warmup
    for _ in range(5):
        ret, frame = cap.read()
        if ret:
            detector.detect(frame)
    
    print("🔥 Warmup complete, starting benchmark...\n")
    
    # Main loop
    while frame_count < num_frames:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect
        results, latency = detector.detect(frame)
        latencies.append(latency)
        
        # Extract parameters
        params = detector.extract_parameters(results, frame.shape)
        params['frame'] = frame_count
        params['latency_ms'] = latency
        all_parameters.append(params)
        
        # Draw landmarks
        frame = detector.draw_landmarks(frame, results)
        
        # Display info
        fps = 1000.0 / latency if latency > 0 else 0
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Latency: {latency:.1f}ms", (10, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Hands: {params['num_hands']}", (10, 110),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Frame: {frame_count}/{num_frames}", (10, 150),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, "Press 'q' to quit", (10, frame.shape[0] - 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        try:
            cv2.imshow('Hand Landmark Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("\n⚠️  User interrupted (pressed 'q')")
                break
        except cv2.error as e:
            # If display is not available, continue without showing
            if "Can't initialize GTK backend" in str(e) or "display" in str(e).lower():
                print(f"   Processing frame {frame_count} (no display available)...")
            else:
                raise
        
        frame_count += 1
        if frame_count % 10 == 0:
            print(f"   Progress: {frame_count}/{num_frames} frames...")
    
    end_total = time.perf_counter()
    total_time = end_total - start_total
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Check if we have any data
    if frame_count == 0 or len(latencies) == 0:
        print("\n❌ Error: No frames were processed. Please check your camera connection.")
        return None, None, None
    
    # Calculate statistics
    avg_fps = frame_count / total_time if total_time > 0 else 0
    avg_latency = np.mean(latencies) if len(latencies) > 0 else 0
    min_latency = np.min(latencies) if len(latencies) > 0 else 0
    max_latency = np.max(latencies) if len(latencies) > 0 else 0
    
    # Print results
    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Total frames processed:  {frame_count}")
    print(f"Total time:              {total_time:.2f} seconds")
    print(f"Average FPS:             {avg_fps:.2f} frames/second")
    print(f"Average latency:         {avg_latency:.2f} ms")
    print(f"Min latency:             {min_latency:.2f} ms")
    print(f"Max latency:             {max_latency:.2f} ms")
    print()
    
    # Extract and display parameter statistics
    if all_parameters:
        hands_detected = sum(1 for p in all_parameters if p['num_hands'] > 0)
        print(f"Frames with hands:       {hands_detected}/{frame_count}")
        print(f"Detection rate:          {hands_detected/frame_count*100:.1f}%")
        
        # Average number of landmarks per frame
        if hands_detected > 0:
            total_landmarks = sum(len(p['landmarks']) for p in all_parameters if p['landmarks'])
            avg_landmarks = total_landmarks / hands_detected if hands_detected > 0 else 0
            print(f"Avg landmarks per hand:  {avg_landmarks:.1f}")
    
    print("=" * 70)
    
    # Save results
    if save_results:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = f"results/benchmarks/hand_landmarks_{timestamp}.json"
        
        results_data = {
            'timestamp': timestamp,
            'total_frames': frame_count,
            'total_time_sec': total_time,
            'avg_fps': avg_fps,
            'avg_latency_ms': avg_latency,
            'min_latency_ms': min_latency,
            'max_latency_ms': max_latency,
            'parameters_sample': all_parameters[:10],  # First 10 frames
            'all_latencies': latencies
        }
        
        import os
        os.makedirs(os.path.dirname(results_file), exist_ok=True)
        
        with open(results_file, 'w') as f:
            json.dump(results_data, f, indent=2)
        
        print(f"\n✅ Results saved to: {results_file}")
    
    return avg_fps, avg_latency, all_parameters


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Hand Landmark Detection Demo')
    parser.add_argument('--camera', type=int, default=0, help='Camera ID')
    parser.add_argument('--frames', type=int, default=100, help='Number of frames')
    parser.add_argument('--video', type=str, default=None, help='Video file path (overrides camera)')
    parser.add_argument('--no-save', action='store_true', help='Do not save results')
    
    args = parser.parse_args()
    
    run_demo(
        camera_id=args.camera,
        num_frames=args.frames,
        save_results=not args.no_save,
        video_file=args.video
    )

