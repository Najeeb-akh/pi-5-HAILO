#!/bin/bash
# Helper script to record a short video for hand landmark detection

echo "📹 Recording hand video for landmark detection demo..."
echo "   Show your hands to the camera for 5 seconds"
echo "   Press Ctrl+C to stop early"
echo ""

# Record 5 seconds of video
rpicam-vid -t 5000 --codec h264 -o /tmp/hand_video.h264

# Convert to mp4 if needed (or use the h264 directly)
if [ -f /tmp/hand_video.h264 ]; then
    echo ""
    echo "✅ Video recorded: /tmp/hand_video.h264"
    echo ""
    echo "To run the demo with this video:"
    echo "  python3 src/hand_landmarks/hand_landmark_demo.py --video /tmp/hand_video.h264 --frames 150"
else
    echo "❌ Failed to record video"
    exit 1
fi

