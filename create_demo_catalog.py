#!/usr/bin/env python3
"""
Demo Catalog Generator for Hailo AI HAT Project
Creates a PDF catalog of all demo videos and visualizations
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from pathlib import Path
from datetime import datetime

def create_demo_catalog():
    """Generate a professional PDF catalog of demos and visualizations"""
    
    # Setup paths
    output_file = Path('/home/admin/Desktop/Najeeb/results/DEMO_CATALOG.pdf')
    graphs_dir = Path('/home/admin/Desktop/Najeeb/results/graphs')
    
    # Create PDF document
    doc = SimpleDocTemplate(str(output_file), pagesize=letter,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=1*inch, bottomMargin=0.75*inch)
    
    # Container for PDF elements
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#00D9FF'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=colors.HexColor('#333333'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    # Title Page
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("HAILO AI HAT", title_style))
    elements.append(Paragraph("Demo Catalog & Visualization Guide", styles['Heading2']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Project info
    project_info = [
        ["Project:", "Hailo-8L AI HAT Performance Evaluation"],
        ["Device:", "Raspberry Pi 5 (8GB) + Hailo-8L AI HAT"],
        ["Date:", datetime.now().strftime("%B %d, %Y")],
        ["Firmware:", "HailoRT 4.20.0"],
        ["Performance:", "13 TOPS AI Acceleration"]
    ]
    
    info_table = Table(project_info, colWidths=[1.5*inch, 4.5*inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#00D9FF')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    elements.append(info_table)
    elements.append(Spacer(1, 0.5*inch))
    
    # Overview
    elements.append(Paragraph("Overview", heading_style))
    overview_text = """
    This catalog documents the comprehensive performance evaluation of the Hailo-8L AI HAT 
    on Raspberry Pi 5. The project includes benchmark testing of 5 different AI models across 
    various computer vision tasks, demonstrating exceptional speedups (7-80×) compared to 
    CPU-only processing. All models achieve real-time performance (>15 FPS) with ultra-low 
    latency (13-20ms).
    """
    elements.append(Paragraph(overview_text, body_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Key Results
    elements.append(Paragraph("Key Results", heading_style))
    results_data = [
        ["Task", "Model", "Hailo FPS", "Speedup", "Status"],
        ["Pose Estimation", "YOLOv8s", "49.5", "33.0×", "✓ Real-time"],
        ["Segmentation", "YOLOv5n", "64.2", "80.3×", "✓ Real-time"],
        ["Object Detection", "YOLOv8s", "57.8", "~29×", "✓ Real-time"],
        ["Classification", "ResNet50", "47.3", "7.0×", "✓ Real-time"],
        ["Person/Face Det.", "YOLOv5s", "63.4", "~32×", "✓ Real-time"]
    ]
    
    results_table = Table(results_data, colWidths=[1.5*inch, 1.3*inch, 1.1*inch, 1*inch, 1.1*inch])
    results_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#00D9FF')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    elements.append(results_table)
    elements.append(PageBreak())
    
    # Visualization Gallery
    elements.append(Paragraph("Visualization Gallery", heading_style))
    elements.append(Paragraph("Professional graphs generated from benchmark data", body_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Add graphs if they exist
    graph_files = [
        ('fps_comparison.png', 'FPS Comparison Chart', 
         'Compares CPU vs Hailo-8L performance across all models. Shows that all Hailo-accelerated models exceed the 15 FPS real-time threshold.'),
        ('latency_comparison.png', 'Latency Comparison Chart',
         'Demonstrates the dramatic reduction in inference latency (13-20ms with Hailo vs 150-1250ms on CPU).'),
        ('speedup_comparison.png', 'Speedup Factor Chart',
         'Highlights the speedup achieved with Hailo-8L, ranging from 7× for classification to 80× for segmentation.'),
        ('benchmark_dashboard.png', 'Comprehensive Performance Dashboard',
         'Multi-panel dashboard showing FPS, latency, speedup, and summary table in a single view.'),
        ('task_category_analysis.png', 'Task Category Analysis',
         'Analyzes performance by task type, showing that dense prediction tasks benefit most from AI acceleration.'),
        ('realtime_capability.png', 'Real-Time Capability Achievement',
         'Visualizes which models achieve real-time performance with and without Hailo acceleration.')
    ]
    
    for graph_file, title, description in graph_files:
        graph_path = graphs_dir / graph_file
        
        if graph_path.exists():
            elements.append(Paragraph(title, subheading_style))
            elements.append(Paragraph(description, body_style))
            elements.append(Spacer(1, 0.1*inch))
            
            # Add image (scaled to fit page)
            img = Image(str(graph_path), width=6.5*inch, height=4*inch)
            elements.append(img)
            elements.append(Spacer(1, 0.2*inch))
        else:
            elements.append(Paragraph(f"{title} (Not yet generated)", subheading_style))
            elements.append(Paragraph(f"File: {graph_file}", body_style))
            elements.append(Spacer(1, 0.1*inch))
    
    elements.append(PageBreak())
    
    # Demo Videos Section
    elements.append(Paragraph("Demo Video Guide", heading_style))
    elements.append(Paragraph(
        "The following demo videos showcase real-world performance of the Hailo AI HAT. "
        "Each video demonstrates a different AI model running in real-time.",
        body_style
    ))
    elements.append(Spacer(1, 0.2*inch))
    
    # Video descriptions
    videos = [
        {
            'title': 'Video 1: Pose Estimation Demo',
            'model': 'YOLOv8s-Pose',
            'duration': '1-2 minutes',
            'description': 'Demonstrates real-time human pose estimation with 17 keypoint detection. '
                          'Shows various poses and movements tracked at 49.5 FPS with only 19.1ms latency.',
            'file': 'pose_estimation_demo.mp4',
            'highlights': ['49.5 FPS performance', '17 keypoints tracked', 'Real-time pose tracking']
        },
        {
            'title': 'Video 2: Instance Segmentation Demo',
            'model': 'YOLOv5n-Seg',
            'duration': '1-2 minutes',
            'description': 'Shows pixel-level object segmentation running at 64.2 FPS. '
                          'Demonstrates detection and segmentation of multiple object classes with colored masks.',
            'file': 'segmentation_demo.mp4',
            'highlights': ['64.2 FPS (fastest)', 'Pixel-level accuracy', 'Multi-object detection']
        },
        {
            'title': 'Video 3: Multi-Model Comparison',
            'model': 'Various',
            'duration': '2-3 minutes',
            'description': 'Comprehensive comparison showing all 5 models. Includes performance graphs '
                          'and side-by-side CPU vs Hailo comparison.',
            'file': 'multi_model_comparison.mp4',
            'highlights': ['All models compared', 'Performance graphs shown', 'Real-world applications']
        },
        {
            'title': 'Video 4: Quick Terminal Demo',
            'model': 'All Models',
            'duration': '30 seconds',
            'description': 'Fast-paced demonstration of benchmark results running in terminal. '
                          'Shows all 5 models with their FPS and latency metrics.',
            'file': 'quick_demo_30sec.mp4',
            'highlights': ['Terminal benchmark runs', 'All models in 30 seconds', 'Performance summary']
        }
    ]
    
    for video in videos:
        elements.append(Paragraph(video['title'], subheading_style))
        
        video_info = [
            ["Model:", video['model']],
            ["Duration:", video['duration']],
            ["Filename:", video['file']]
        ]
        
        video_table = Table(video_info, colWidths=[1.2*inch, 4.8*inch])
        video_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        
        elements.append(video_table)
        elements.append(Spacer(1, 0.1*inch))
        elements.append(Paragraph(video['description'], body_style))
        
        # Highlights
        highlights_text = "<b>Highlights:</b> " + " • ".join(video['highlights'])
        elements.append(Paragraph(highlights_text, body_style))
        elements.append(Spacer(1, 0.2*inch))
    
    elements.append(PageBreak())
    
    # Recording Instructions
    elements.append(Paragraph("Recording Demo Videos", heading_style))
    elements.append(Paragraph(
        "To record your own demo videos, use the provided scripts and follow these guidelines:",
        body_style
    ))
    elements.append(Spacer(1, 0.15*inch))
    
    recording_steps = [
        ["1.", "Run the quick demo script:", "<font face='Courier'>./quick_demo_capture.sh</font>"],
        ["2.", "For screen recording:", "<font face='Courier'>asciinema rec demo.cast</font>"],
        ["3.", "For camera demos:", "Use rpicam-apps with Hailo post-processing"],
        ["4.", "Edit videos:", "Use OpenShot, Kdenlive, or online editors"],
        ["5.", "Save to:", "<font face='Courier'>results/demo_videos/</font>"]
    ]
    
    for step in recording_steps:
        step_text = f"<b>{step[0]}</b> {step[1]} {step[2]}"
        elements.append(Paragraph(step_text, body_style))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # Applications
    elements.append(Paragraph("Real-World Applications", heading_style))
    applications = [
        ("Fitness & Health", "Real-time form analysis, rep counting, fall detection"),
        ("Security & Surveillance", "Multi-camera person/face detection, zone monitoring"),
        ("Retail Analytics", "Object counting, customer tracking, queue management"),
        ("Industrial QC", "Defect detection, assembly verification, process monitoring"),
        ("Smart Home", "Gesture control, occupancy detection, privacy-preserving AI"),
        ("Robotics", "Vision-based navigation, object manipulation, human-robot interaction")
    ]
    
    for app_name, app_desc in applications:
        elements.append(Paragraph(f"<b>{app_name}:</b> {app_desc}", body_style))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # Resources
    elements.append(Paragraph("Project Resources", heading_style))
    resources = [
        ("Detailed Benchmarks:", "results/benchmarks/BENCHMARK_RESULTS.md"),
        ("Visualization Graphs:", "results/graphs/*.png"),
        ("Demo Scripts:", "demo_video_scripts.md"),
        ("Quick Demo Tool:", "quick_demo_capture.sh"),
        ("Final Documentation:", "FINAL_PROJECT_DOCUMENTATION.md"),
        ("Essential Guide:", "ESSENTIAL_GUIDE.md")
    ]
    
    for resource_name, resource_path in resources:
        elements.append(Paragraph(f"<b>{resource_name}</b> {resource_path}", body_style))
    
    elements.append(Spacer(1, 0.5*inch))
    
    # Footer
    footer_text = """
    <para alignment='center'>
    <b>Project completed: November 24, 2025</b><br/>
    Raspberry Pi 5 + Hailo-8L AI HAT<br/>
    All models achieve real-time performance with exceptional speedups<br/>
    <i>Edge AI Made Easy</i>
    </para>
    """
    elements.append(Paragraph(footer_text, body_style))
    
    # Build PDF
    doc.build(elements)
    print(f"✅ Demo catalog created: {output_file}")
    return output_file

if __name__ == '__main__':
    try:
        print("\n" + "="*60)
        print("Creating Demo Catalog PDF...")
        print("="*60 + "\n")
        output = create_demo_catalog()
        print(f"\n✅ Success! PDF saved to:\n   {output}\n")
    except Exception as e:
        print(f"\n❌ Error creating PDF: {e}")
        print("\nNote: This requires reportlab package.")
        print("Install with: pip install reportlab --break-system-packages\n")

