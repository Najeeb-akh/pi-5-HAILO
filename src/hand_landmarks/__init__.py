"""
Hand Landmark Detection Module
Uses MediaPipe Hands (NOT from Hailo Zoo)
"""

from .hand_landmark_demo import HandLandmarkDetector, run_demo

__all__ = ['HandLandmarkDetector', 'run_demo']

