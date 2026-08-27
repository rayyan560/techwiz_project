"""
utils.py - Utility Functions & PDF Report Generator for AI Office Copilot
"""

import os
import base64
import tempfile
import io
from typing import Dict, Any, List
from datetime import datetime

# ReportLab imports for generating executive PDF reports
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


def save_uploaded_media(uploaded_file) -> str:
    """Save Streamlit UploadedFile to temporary disk path and return path."""
    ext = os.path.splitext(uploaded_file.name)[1]
    if not ext:
        ext = ".webm"
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name


def save_base64_media(b64_data: str, mime_type: str = "video/webm") -> str:
    """Save base64 encoded media string to temporary disk file."""
    if "," in b64_data:
        b64_data = b64_data.split(",")[1]
    
    raw_bytes = base64.b64decode(b64_data)
    ext = ".webm" if "webm" in mime_type else ".mp4" if "mp4" in mime_type else ".wav"
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(raw_bytes)
        return tmp.name


def generate_pdf_report(analysis_data: Dict[str, Any], session_name: str = "Executive Meeting Session") -> bytes:
    """
    Generate an Executive PDF Report using ReportLab with platinum metallic theme.
    Returns PDF bytes for direct download.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Define custom executive palette
    CHARCOAL = colors.HexColor("#334155")
    DARK_SLATE = colors.HexColor("#1E293B")
    PLATINUM_BG = colors.HexColor("#F1F5F9")
    ACCENT_GOLD = colors.HexColor("#78350F")
    BORDER_COLOR = colors.HexColor("#CBD5E1")
    
    title_style = ParagraphStyle(
        'ExecTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=DARK_SLATE,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'ExecSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#64748B"),
        spaceAfter=15
    )
    
    h2_style = ParagraphStyle(
        'ExecH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=DARK_SLATE,
        spaceBefore=14,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'ExecBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=CHARCOAL,
        spaceAfter=8
    )
    
    story = []
    
    # Header Title Block
    story.append(Paragraph("AI OFFICE COPILOT & EXECUTIVE BRIEF", title_style))
    date_str = datetime.now().strftime("%B %d, %Y | %I:%M %p")
    story.append(Paragraph(f"Session: {session_name} &nbsp;•&nbsp; Generated: {date_str}", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=BORDER_COLOR, spaceAfter=15))
    
    # Executive Key Metrics Bar
    focus_score = analysis_data.get("focus_score", 85)
    sentiment = analysis_data.get("sentiment", "Calm & Professional")
    alerts = analysis_data.get("alerts", "None")
    
    metrics_data = [
        [
            Paragraph("<b>FOCUS & ENERGY SCORE</b>", ParagraphStyle('M1', parent=body_style, fontSize=8, textColor=colors.HexColor("#64748B"))),
            Paragraph("<b>SENTIMENT & TONE</b>", ParagraphStyle('M2', parent=body_style, fontSize=8, textColor=colors.HexColor("#64748B"))),
            Paragraph("<b>PRIVACY / ALERT STATUS</b>", ParagraphStyle('M3', parent=body_style, fontSize=8, textColor=colors.HexColor("#64748B")))
        ],
        [
            Paragraph(f"<font size=14 color='#1E293B'><b>{focus_score}%</b></font>", body_style),
            Paragraph(f"<font size=10 color='#334155'><b>{sentiment}</b></font>", body_style),
            Paragraph(f"<font size=9 color='#334155'>{alerts}</font>", body_style)
        ]
    ]
    
    metrics_table = Table(metrics_data, colWidths=[170, 180, 180])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PLATINUM_BG),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(metrics_table)
    story.append(Spacer(1, 15))
    
    # Summary Section
    story.append(Paragraph("Executive Summary", h2_style))
    summary_text = analysis_data.get("summary", "No summary generated.").replace("\n", "<br/>")
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))
    
    # Action Items Table
    action_items = analysis_data.get("action_items", [])
    if action_items:
        story.append(Paragraph("Structured Action Items & Tasks", h2_style))
        
        table_data = [[
            Paragraph("<b>Task & Deliverable</b>", ParagraphStyle('TH1', parent=body_style, fontSize=8, textColor=DARK_SLATE)),
            Paragraph("<b>Assignee</b>", ParagraphStyle('TH2', parent=body_style, fontSize=8, textColor=DARK_SLATE)),
            Paragraph("<b>Deadline</b>", ParagraphStyle('TH3', parent=body_style, fontSize=8, textColor=DARK_SLATE)),
            Paragraph("<b>Priority</b>", ParagraphStyle('TH4', parent=body_style, fontSize=8, textColor=DARK_SLATE))
        ]]
        
        for item in action_items:
            if isinstance(item, dict):
                task = item.get("task", "")
                assignee = item.get("assignee", "Unassigned")
                deadline = item.get("deadline", "TBD")
                priority = item.get("priority", "Medium")
            else:
                task = str(item)
                assignee = "Executive"
                deadline = "TBD"
                priority = "Medium"
                
            table_data.append([
                Paragraph(task, body_style),
                Paragraph(assignee, body_style),
                Paragraph(deadline, body_style),
                Paragraph(f"<b>{priority}</b>", body_style)
            ])
            
        action_table = Table(table_data, colWidths=[240, 100, 100, 90])
        action_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E2E8F0")),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(action_table)
        story.append(Spacer(1, 15))
        
    # Spoken Transcript Section
    transcript = analysis_data.get("transcript", "")
    if transcript:
        story.append(Paragraph("Spoken Transcript Record", h2_style))
        formatted_transcript = transcript.replace("\n", "<br/>")
        transcript_style = ParagraphStyle(
            'ExecTranscript',
            parent=body_style,
            fontSize=8.5,
            leading=13,
            textColor=CHARCOAL
        )
        story.append(Paragraph(formatted_transcript, transcript_style))
        
    # Build Document
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
