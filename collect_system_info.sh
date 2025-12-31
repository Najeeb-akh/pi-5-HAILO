#!/bin/bash
# System Information Collection Script
# Collects all system details needed for project reproducibility

echo "=========================================="
echo "System Information Collection"
echo "=========================================="
echo ""

echo "=== Operating System ==="
cat /etc/os-release
echo ""

echo "=== Kernel Information ==="
uname -a
echo ""

echo "=== Kernel Version Details ==="
cat /proc/version
echo ""

echo "=== Hardware Information ==="
cat /proc/cpuinfo | grep -E "(model name|Hardware|Revision)" | head -5
echo ""

echo "=== Python Version ==="
python3 --version
echo ""

echo "=== Python Packages ==="
pip3 list | grep -E "(opencv|numpy|mediapipe|psutil)"
echo ""

echo "=== Hailo Device Information ==="
lspci | grep Hailo
echo ""

echo "=== Hailo Firmware Details ==="
hailortcli fw-control identify 2>/dev/null
echo ""

echo "=== Camera Information ==="
rpicam-hello --list-cameras 2>/dev/null || echo "Camera check skipped (not critical)"
echo ""

echo "=========================================="
echo "Collection Complete"
echo "=========================================="
echo ""
echo "Save this output to SYSTEM_INFO.txt for documentation"

