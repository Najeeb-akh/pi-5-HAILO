#!/usr/bin/env python3
"""
Hailo AI HAT Benchmark Visualization
Generates professional graphs from benchmark results for final project documentation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Set style for professional-looking graphs
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['legend.fontsize'] = 10

# Create output directory
output_dir = Path('/home/admin/Desktop/Najeeb/results/graphs')
output_dir.mkdir(parents=True, exist_ok=True)

# Benchmark data from BENCHMARK_RESULTS.md
data = {
    'models': ['Pose\nEstimation\n(YOLOv8s)', 'Segmentation\n(YOLOv5n)', 
               'Object\nDetection\n(YOLOv8s)', 'Classification\n(ResNet50)', 
               'Person/Face\nDetection\n(YOLOv5s)'],
    'short_names': ['Pose', 'Segmentation', 'Detection', 'Classification', 'Person/Face'],
    'cpu_fps': [1.5, 0.8, 2.0, 6.73, 2.0],
    'hailo_fps': [49.5, 64.2, 57.8, 47.3, 63.4],
    'hailo_latency': [19.1, 14.4, 13.3, 15.5, 13.2],
    'cpu_latency': [667, 1250, 500, 148.6, 500],
    'speedup': [33.0, 80.3, 28.9, 7.0, 31.8]
}

# Color scheme
hailo_color = '#00D9FF'  # Hailo brand cyan
cpu_color = '#FF6B6B'    # Warm red for CPU
speedup_color = '#4ECDC4' # Teal for speedup
realtime_color = '#95E1D3' # Light green for real-time threshold

def create_fps_comparison():
    """Create FPS comparison bar chart"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    x = np.arange(len(data['models']))
    width = 0.35
    
    # Create bars
    bars1 = ax.bar(x - width/2, data['cpu_fps'], width, label='CPU (Baseline)', 
                   color=cpu_color, alpha=0.8, edgecolor='black', linewidth=1.2)
    bars2 = ax.bar(x + width/2, data['hailo_fps'], width, label='Hailo-8L AI HAT', 
                   color=hailo_color, alpha=0.8, edgecolor='black', linewidth=1.2)
    
    # Add real-time threshold line
    ax.axhline(y=15, color=realtime_color, linestyle='--', linewidth=2, 
               label='Real-time Threshold (15 FPS)', alpha=0.7)
    
    # Customize
    ax.set_xlabel('Model / Task', fontweight='bold', fontsize=13)
    ax.set_ylabel('Frames Per Second (FPS)', fontweight='bold', fontsize=13)
    ax.set_title('Hailo AI HAT Performance: FPS Comparison\nRaspberry Pi 5 + Hailo-8L (13 TOPS)', 
                 fontweight='bold', fontsize=15, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(data['models'], fontsize=10)
    ax.legend(loc='upper left', framealpha=0.95, fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # Add annotation
    ax.text(0.98, 0.97, 'Higher is better →', transform=ax.transAxes,
            fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig(output_dir / 'fps_comparison.png', dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {output_dir / 'fps_comparison.png'}")
    plt.close()


def create_latency_comparison():
    """Create latency comparison bar chart (log scale)"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    x = np.arange(len(data['models']))
    width = 0.35
    
    # Create bars
    bars1 = ax.bar(x - width/2, data['cpu_latency'], width, label='CPU (Baseline)', 
                   color=cpu_color, alpha=0.8, edgecolor='black', linewidth=1.2)
    bars2 = ax.bar(x + width/2, data['hailo_latency'], width, label='Hailo-8L AI HAT', 
                   color=hailo_color, alpha=0.8, edgecolor='black', linewidth=1.2)
    
    # Use log scale for better visualization
    ax.set_yscale('log')
    
    # Customize
    ax.set_xlabel('Model / Task', fontweight='bold', fontsize=13)
    ax.set_ylabel('Latency (milliseconds, log scale)', fontweight='bold', fontsize=13)
    ax.set_title('Hailo AI HAT Performance: Latency Comparison\nRaspberry Pi 5 + Hailo-8L (13 TOPS)', 
                 fontweight='bold', fontsize=15, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(data['models'], fontsize=10)
    ax.legend(loc='upper left', framealpha=0.95, fontsize=11)
    ax.grid(axis='y', alpha=0.3, which='both')
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}' if height < 100 else f'{height:.0f}',
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # Add annotation
    ax.text(0.98, 0.03, '← Lower is better', transform=ax.transAxes,
            fontsize=10, verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig(output_dir / 'latency_comparison.png', dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {output_dir / 'latency_comparison.png'}")
    plt.close()


def create_speedup_chart():
    """Create speedup comparison bar chart"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    x = np.arange(len(data['models']))
    
    # Create gradient colors based on speedup value
    colors = []
    for speedup in data['speedup']:
        if speedup < 10:
            colors.append('#FFB74D')  # Orange for lower speedup
        elif speedup < 30:
            colors.append('#4ECDC4')  # Teal for medium
        else:
            colors.append('#00D9FF')  # Cyan for high speedup
    
    bars = ax.bar(x, data['speedup'], color=colors, alpha=0.8, 
                  edgecolor='black', linewidth=1.2)
    
    # Customize
    ax.set_xlabel('Model / Task', fontweight='bold', fontsize=13)
    ax.set_ylabel('Speedup Factor (×)', fontweight='bold', fontsize=13)
    ax.set_title('Hailo AI HAT Speedup vs CPU Baseline\nRaspberry Pi 5 + Hailo-8L (13 TOPS)', 
                 fontweight='bold', fontsize=15, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(data['models'], fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.1f}×',
               ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    # Add legend for color coding
    legend_elements = [
        mpatches.Patch(color='#FFB74D', label='Moderate Speedup (< 10×)', alpha=0.8),
        mpatches.Patch(color='#4ECDC4', label='High Speedup (10-30×)', alpha=0.8),
        mpatches.Patch(color='#00D9FF', label='Exceptional Speedup (> 30×)', alpha=0.8)
    ]
    ax.legend(handles=legend_elements, loc='upper left', framealpha=0.95, fontsize=11)
    
    # Add annotation
    ax.text(0.98, 0.97, 'Higher is better →', transform=ax.transAxes,
            fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig(output_dir / 'speedup_comparison.png', dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {output_dir / 'speedup_comparison.png'}")
    plt.close()


def create_comprehensive_dashboard():
    """Create a comprehensive dashboard with multiple metrics"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # 1. FPS Comparison (top left)
    ax1 = fig.add_subplot(gs[0, 0])
    x = np.arange(len(data['short_names']))
    width = 0.35
    ax1.bar(x - width/2, data['cpu_fps'], width, label='CPU', color=cpu_color, alpha=0.8)
    ax1.bar(x + width/2, data['hailo_fps'], width, label='Hailo-8L', color=hailo_color, alpha=0.8)
    ax1.axhline(y=15, color='green', linestyle='--', linewidth=1.5, alpha=0.5, label='Real-time (15 FPS)')
    ax1.set_ylabel('FPS', fontweight='bold')
    ax1.set_title('Frames Per Second Comparison', fontweight='bold', fontsize=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(data['short_names'], fontsize=9, rotation=15, ha='right')
    ax1.legend(fontsize=9)
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. Latency Comparison (top right)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.bar(x - width/2, data['cpu_latency'], width, label='CPU', color=cpu_color, alpha=0.8)
    ax2.bar(x + width/2, data['hailo_latency'], width, label='Hailo-8L', color=hailo_color, alpha=0.8)
    ax2.set_yscale('log')
    ax2.set_ylabel('Latency (ms, log scale)', fontweight='bold')
    ax2.set_title('Inference Latency Comparison', fontweight='bold', fontsize=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels(data['short_names'], fontsize=9, rotation=15, ha='right')
    ax2.legend(fontsize=9)
    ax2.grid(axis='y', alpha=0.3, which='both')
    
    # 3. Speedup Factors (bottom left)
    ax3 = fig.add_subplot(gs[1, 0])
    colors = ['#00D9FF' if s > 30 else '#4ECDC4' if s > 10 else '#FFB74D' for s in data['speedup']]
    bars = ax3.bar(x, data['speedup'], color=colors, alpha=0.8, edgecolor='black', linewidth=1)
    ax3.set_ylabel('Speedup Factor (×)', fontweight='bold')
    ax3.set_title('Hailo-8L Speedup vs CPU', fontweight='bold', fontsize=12)
    ax3.set_xticks(x)
    ax3.set_xticklabels(data['short_names'], fontsize=9, rotation=15, ha='right')
    ax3.grid(axis='y', alpha=0.3)
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}×', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # 4. Performance Summary Table (bottom right)
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')
    
    # Create summary table
    table_data = []
    table_data.append(['Model', 'Hailo FPS', 'Speedup', 'Status'])
    for i in range(len(data['short_names'])):
        status = '✅ Real-time' if data['hailo_fps'][i] > 15 else '⚠️ Slow'
        table_data.append([
            data['short_names'][i],
            f"{data['hailo_fps'][i]:.1f}",
            f"{data['speedup'][i]:.1f}×",
            status
        ])
    
    table = ax4.table(cellText=table_data, cellLoc='left', loc='center',
                     colWidths=[0.35, 0.2, 0.2, 0.25])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Style header row
    for i in range(4):
        table[(0, i)].set_facecolor('#00D9FF')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternate row colors
    for i in range(1, len(table_data)):
        for j in range(4):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#f0f0f0')
    
    ax4.set_title('Performance Summary', fontweight='bold', fontsize=12, pad=20)
    
    # Add main title
    fig.suptitle('Hailo AI HAT Benchmark Dashboard\nRaspberry Pi 5 + Hailo-8L (13 TOPS)', 
                 fontweight='bold', fontsize=16, y=0.98)
    
    plt.savefig(output_dir / 'benchmark_dashboard.png', dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {output_dir / 'benchmark_dashboard.png'}")
    plt.close()


def create_task_category_analysis():
    """Create analysis by task category (Dense vs Classification)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Categorize tasks
    dense_tasks = ['Pose', 'Segmentation', 'Detection', 'Person/Face']
    dense_speedup = [33.0, 80.3, 28.9, 31.8]
    classification_speedup = [7.0]
    
    # Plot 1: Speedup by category
    categories = ['Dense\nPrediction\n(avg)', 'Classification']
    avg_speedup = [np.mean(dense_speedup), classification_speedup[0]]
    
    bars = ax1.bar(categories, avg_speedup, color=[hailo_color, '#FFB74D'], 
                   alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Average Speedup (×)', fontweight='bold', fontsize=12)
    ax1.set_title('Speedup by Task Category', fontweight='bold', fontsize=13)
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}×', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Plot 2: Individual dense task speedups
    x = np.arange(len(dense_tasks))
    bars2 = ax2.bar(x, dense_speedup, color=hailo_color, alpha=0.8, 
                    edgecolor='black', linewidth=1.2)
    ax2.set_ylabel('Speedup (×)', fontweight='bold', fontsize=12)
    ax2.set_title('Dense Prediction Tasks Breakdown', fontweight='bold', fontsize=13)
    ax2.set_xticks(x)
    ax2.set_xticklabels(dense_tasks, fontsize=10)
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}×', ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    plt.suptitle('Hailo-8L Performance by Task Type\nDense Prediction Shows Highest Acceleration', 
                 fontweight='bold', fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig(output_dir / 'task_category_analysis.png', dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {output_dir / 'task_category_analysis.png'}")
    plt.close()


def create_realtime_capability_chart():
    """Create chart showing real-time capability achievement"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.arange(len(data['models']))
    
    # Show both CPU and Hailo, color-coded by real-time capability
    cpu_colors = ['#FF6B6B' if fps < 15 else '#95E1D3' for fps in data['cpu_fps']]
    hailo_colors = ['#FF6B6B' if fps < 15 else '#4ECDC4' for fps in data['hailo_fps']]
    
    width = 0.35
    bars1 = ax.bar(x - width/2, data['cpu_fps'], width, label='CPU', 
                   color=cpu_colors, alpha=0.8, edgecolor='black', linewidth=1.2)
    bars2 = ax.bar(x + width/2, data['hailo_fps'], width, label='Hailo-8L', 
                   color=hailo_colors, alpha=0.8, edgecolor='black', linewidth=1.2)
    
    # Add real-time threshold
    ax.axhline(y=15, color='green', linestyle='--', linewidth=2.5, 
               label='Real-time Threshold (15 FPS)', alpha=0.7)
    
    # Customize
    ax.set_xlabel('Model / Task', fontweight='bold', fontsize=13)
    ax.set_ylabel('Frames Per Second (FPS)', fontweight='bold', fontsize=13)
    ax.set_title('Real-Time Capability: CPU vs Hailo-8L AI HAT\nAll Models Achieve Real-Time with Hailo', 
                 fontweight='bold', fontsize=14, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(data['models'], fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    
    # Custom legend
    legend_elements = [
        mpatches.Patch(color='#FF6B6B', label='Below Real-time (< 15 FPS)', alpha=0.8),
        mpatches.Patch(color='#4ECDC4', label='Real-time Capable (≥ 15 FPS)', alpha=0.8),
        mpatches.Patch(color='green', label='Real-time Threshold', alpha=0.7)
    ]
    ax.legend(handles=legend_elements, loc='upper left', framealpha=0.95, fontsize=10)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'realtime_capability.png', dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {output_dir / 'realtime_capability.png'}")
    plt.close()


def main():
    """Generate all visualization graphs"""
    print("\n" + "="*60)
    print("Hailo AI HAT Benchmark Visualization Generator")
    print("="*60 + "\n")
    
    print("Generating graphs...")
    print()
    
    # Generate all graphs
    create_fps_comparison()
    create_latency_comparison()
    create_speedup_chart()
    create_comprehensive_dashboard()
    create_task_category_analysis()
    create_realtime_capability_chart()
    
    print()
    print("="*60)
    print("✅ All graphs generated successfully!")
    print(f"📁 Output directory: {output_dir}")
    print()
    print("Generated files:")
    print("  1. fps_comparison.png - FPS comparison bar chart")
    print("  2. latency_comparison.png - Latency comparison (log scale)")
    print("  3. speedup_comparison.png - Speedup factors chart")
    print("  4. benchmark_dashboard.png - Comprehensive dashboard")
    print("  5. task_category_analysis.png - Task category analysis")
    print("  6. realtime_capability.png - Real-time capability chart")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()

