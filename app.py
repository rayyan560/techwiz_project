"""
app.py - Main Streamlit Web Application for AI Office Copilot & Executive Assistant
Pearl Glassmorphism & Soft Platinum Metallic Design
"""

import os
import time
import json
import streamlit as st
import streamlit.components.v1 as components

# Import custom modules
from styles import inject_styles
from ai_engine import analyze_media_file, generate_mock_analysis
from utils import save_uploaded_media, save_base64_media, generate_pdf_report

# Page Config
st.set_page_config(
    page_title="AI Office Copilot & Executive Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Pearl Glass & Platinum CSS
inject_styles()

# Initialize Session State
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = None
if "recording_active" not in st.session_state:
    st.session_state.recording_active = False
if "api_key" not in st.session_state or not st.session_state.api_key:
    st.session_state.api_key = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6KVwlW51_7jrEhLBtGgEU63ar7A9KFI83SwWqm_aB5tGA")
    os.environ["GEMINI_API_KEY"] = st.session_state.api_key
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = set()
if "media_file_path" not in st.session_state:
    st.session_state.media_file_path = None
if "is_analyzing" not in st.session_state:
    st.session_state.is_analyzing = False


# ==============================================================================
# SIDEBAR & SETTINGS DRAWER
# ==============================================================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <div style="font-size: 2.2rem; margin-bottom: 5px;">💎</div>
        <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.25rem; color: #1E293B;">
            EXECUTIVE COPILOT
        </div>
        <div style="font-size: 0.78rem; color: #64748B; font-weight: 500;">
            Pearl Glass & Platinum Edition
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # API Configuration
    st.markdown("##### ⚙️ Gemini API Configuration")
    user_api_input = st.text_input(
        "Google Gemini API Key",
        value=st.session_state.api_key,
        type="password",
        help="Enter your GEMINI_API_KEY. Leave blank to run in Interactive Executive Demo Mode."
    )
    if user_api_input != st.session_state.api_key:
        st.session_state.api_key = user_api_input
        os.environ["GEMINI_API_KEY"] = user_api_input
        
    if st.session_state.api_key:
        st.markdown('<span class="badge-platinum">⚡ Gemini 2.0 Connected</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-gold">🧪 Interactive Demo Mode</span>', unsafe_allow_html=True)

    st.divider()
    
    # Quick Preset Launcher for Instant Demonstration
    st.markdown("##### 🚀 Quick Demo Presets")
    preset_choice = st.selectbox(
        "Load Sample Office Session:",
        [
            "Select a Preset...",
            "Q3 Product & Architecture Sync",
            "Executive Leadership Alignment",
            "Client Consultation & Security Brief"
        ]
    )
    
    if st.button("Load Preset Session", use_container_width=True):
        if preset_choice != "Select a Preset...":
            with st.spinner("Loading demo session data..."):
                time.sleep(1)
                mock_data = generate_mock_analysis(preset_choice)
                if "Leadership" in preset_choice:
                    mock_data["focus_score"] = 96
                    mock_data["sentiment"] = "Highly Focused & Strategic"
                elif "Security" in preset_choice:
                    mock_data["focus_score"] = 89
                    mock_data["sentiment"] = "Calm, Vigilant & Compliant"
                st.session_state.analysis_results = mock_data
                st.session_state.completed_tasks = set()
                st.toast(f"Loaded '{preset_choice}' analysis!", icon="✨")
                st.rerun()

    st.markdown("""
    <div style="position: fixed; bottom: 20px; font-size: 0.75rem; color: #94A3B8;">
        AI Office Copilot v2.5<br/>Powered by Google Gemini API
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# TOP HEADER BAR
# ==============================================================================
col_title, col_status = st.columns([3, 1])

with col_title:
    st.markdown("""
    <div>
        <h1 class="header-title">AI Office Copilot & Executive Assistant</h1>
        <div class="header-subtitle">Real-time Multimodal Webcam Stream • Live Diary Transcript • Action Intelligence • Focus Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with col_status:
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    if st.session_state.is_analyzing:
        st.markdown("""
        <div style="text-align: right;">
            <span class="badge-platinum"><span class="badge-pulse-red"></span> Analyzing Media with Gemini...</span>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.analysis_results:
        st.markdown("""
        <div style="text-align: right;">
            <span class="badge-platinum"><span class="badge-pulse-green"></span> Session Ready</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: right;">
            <span class="badge-platinum">Ready for Recording</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)


# ==============================================================================
# MAIN 3-COLUMN LAYOUT
# ==============================================================================
col_left, col_center, col_right = st.columns([3, 4, 3], gap="medium")


# ------------------------------------------------------------------------------
# LEFT COLUMN: WEBCAM & AUDIO MEDIA RECORDING CONTROLLER
# ------------------------------------------------------------------------------
with col_left:
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <h3 style="margin: 0; font-size: 1.15rem;">📷 Live Media Controller</h3>
        <span class="badge-platinum">Brushed Platinum</span>
    </div>
    """, unsafe_allow_html=True)

    input_mode = st.radio(
        "Select Capture Input:",
        ["🎙️ Mic Audio Recorder", "📹 Browser Webcam", "📁 Upload Media File", "📷 Camera Snapshot"],
        horizontal=True,
        label_visibility="collapsed"
    )

    if input_mode == "🎙️ Mic Audio Recorder":
        st.markdown("""
        <div style="background: rgba(255,255,255,0.7); padding: 12px; border-radius: 14px; border: 1px solid #CBD5E1; margin-bottom: 10px;">
            <div style="font-size: 0.85rem; font-weight: 700; color: #1E293B;">🎙️ Live Spoken Session Audio Capture</div>
            <div style="font-size: 0.78rem; color: #64748B;">Record your voice/meeting audio below. Gemini 2.0 Flash will analyze your audio and generate a full English transcript & summary.</div>
        </div>
        """, unsafe_allow_html=True)
        
        audio_file = st.audio_input("Record Live Audio", key="live_mic_recorder")
        if audio_file:
            # Check if this is a new audio recording file
            audio_bytes = audio_file.getvalue()
            current_hash = hash(audio_bytes)
            
            if st.session_state.get("last_audio_hash") != current_hash:
                st.session_state.last_audio_hash = current_hash
                st.session_state.is_analyzing = True
                st.session_state.analysis_results = None  # Clear old/preset results immediately!
                
                with st.spinner("⚡ Uploading your live audio to Gemini 3.6 Flash & extracting real transcript..."):
                    tmp_path = save_uploaded_media(audio_file)
                    st.session_state.media_file_path = tmp_path
                    res = analyze_media_file(tmp_path, st.session_state.api_key)
                    st.session_state.analysis_results = res
                    st.session_state.is_analyzing = False
                    st.session_state.completed_tasks = set()
                    st.toast("Real Audio Analyzed by Gemini 3.6!", icon="🚀")
                    st.rerun()
            else:
                if st.button("🔄 Re-analyze Audio with Gemini", type="primary", use_container_width=True):
                    st.session_state.is_analyzing = True
                    with st.spinner("Re-analyzing audio with Gemini 3.6 Flash..."):
                        tmp_path = save_uploaded_media(audio_file)
                        res = analyze_media_file(tmp_path, st.session_state.api_key)
                        st.session_state.analysis_results = res
                        st.session_state.is_analyzing = False
                        st.rerun()

    elif input_mode == "📹 Browser Webcam":
        # Embedded HTML5 Web MediaRecorder Component
        html5_recorder = """
        <div id="recorder-container" style="
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
            border-radius: 18px;
            padding: 16px;
            border: 2px solid #CBD5E1;
            box-shadow: 0 10px 25px rgba(30, 41, 59, 0.25);
            color: #F8FAFC;
            font-family: 'Plus Jakarta Sans', sans-serif;
            text-align: center;
        ">
            <video id="webcam-preview" autoplay playsinline muted style="
                width: 100%;
                height: 180px;
                object-fit: cover;
                border-radius: 12px;
                background: #000;
                border: 1px solid rgba(255,255,255,0.2);
                margin-bottom: 10px;
            "></video>

            <div id="audio-visualizer" style="
                display: none;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 180px;
                border-radius: 12px;
                background: linear-gradient(135deg, #0F172A, #1E293B);
                border: 1px dashed #38BDF8;
                margin-bottom: 10px;
                padding: 20px;
            ">
                <div style="font-size: 2.5rem; margin-bottom: 8px;">🎙️</div>
                <div style="font-weight: 700; font-size: 0.95rem; color: #38BDF8;">Audio-Only Microphone Mode Active</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Camera is disabled or not permitted. Recording speech via microphone.</div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding: 0 5px;">
                <div id="status-tag" style="font-size: 0.82rem; color: #94A3B8; font-weight: 600;">
                    Status: <span id="status-text" style="color: #64748B;">Connecting Mic/Cam...</span>
                </div>
                <div id="timer" style="font-family: monospace; font-size: 1.1rem; font-weight: 700; color: #E2E8F0;">
                    00:00
                </div>
            </div>

            <div style="display: flex; gap: 10px; justify-content: center; margin-bottom: 10px;">
                <button id="btn-start" onclick="startRecording()" style="
                    background: linear-gradient(135deg, #10B981, #059669);
                    color: white; border: none; padding: 10px 18px; border-radius: 10px;
                    font-weight: 700; cursor: pointer; font-size: 0.88rem; flex: 1;
                    box-shadow: 0 4px 12px rgba(16,185,129,0.3);
                ">🔴 Start Recording</button>

                <button id="btn-stop" onclick="stopRecording()" disabled style="
                    background: linear-gradient(135deg, #EF4444, #DC2626);
                    color: white; border: none; padding: 10px 18px; border-radius: 10px;
                    font-weight: 700; cursor: pointer; font-size: 0.88rem; flex: 1;
                    opacity: 0.5; box-shadow: 0 4px 12px rgba(239,68,68,0.3);
                ">⏹️ Stop Session</button>
            </div>
            
            <a id="btn-download" style="display: none; background: #3B82F6; color: white; text-decoration: none; padding: 8px 16px; border-radius: 8px; font-size: 0.82rem; font-weight: 600;">
                ⬇️ Download Recorded Audio/Video (.webm)
            </a>
        </div>

        <script>
            let mediaRecorder;
            let recordedChunks = [];
            let timerInterval;
            let seconds = 0;
            let stream;

            async function initCamera() {
                try {
                    // 1. Try requesting both video and audio
                    stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    document.getElementById('webcam-preview').style.display = "block";
                    document.getElementById('audio-visualizer').style.display = "none";
                    document.getElementById('webcam-preview').srcObject = stream;
                    document.getElementById('status-text').innerText = "Webcam & Mic Connected";
                    document.getElementById('status-text').style.color = "#10B981";
                } catch (errVideo) {
                    console.log("Camera access declined or unavailable, switching to audio-only:", errVideo);
                    try {
                        // 2. Fallback to audio-only microphone stream if camera unavailable/denied!
                        stream = await navigator.mediaDevices.getUserMedia({ video: false, audio: true });
                        document.getElementById('webcam-preview').style.display = "none";
                        document.getElementById('audio-visualizer').style.display = "flex";
                        document.getElementById('status-text').innerText = "🎙️ Microphone Only Connected";
                        document.getElementById('status-text').style.color = "#38BDF8";
                    } catch (errAudio) {
                        console.log("Microphone access error:", errAudio);
                        document.getElementById('status-text').innerText = "⚠️ Mic Permission Required";
                        document.getElementById('status-text').style.color = "#EF4444";
                    }
                }
            }

            async function startRecording() {
                if (!stream) {
                    await initCamera();
                }
                recordedChunks = [];
                try {
                    mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
                } catch (e) {
                    mediaRecorder = new MediaRecorder(stream);
                }

                mediaRecorder.ondataavailable = (e) => {
                    if (e.data.size > 0) recordedChunks.push(e.data);
                };

                mediaRecorder.onstop = () => {
                    if (timerInterval) clearInterval(timerInterval);
                    const blob = new Blob(recordedChunks, { type: 'video/webm' });
                    const url = URL.createObjectURL(blob);
                    const dlBtn = document.getElementById('btn-download');
                    dlBtn.href = url;
                    dlBtn.download = "office_session_recording.webm";
                    dlBtn.style.display = "inline-block";
                    document.getElementById('status-text').innerText = "Recording Saved! Download below & drop in Uploader.";
                    document.getElementById('status-text').style.color = "#38BDF8";
                };

                mediaRecorder.start(1000);
                seconds = 0;
                timerInterval = setInterval(() => {
                    seconds++;
                    let m = String(Math.floor(seconds / 60)).padStart(2, '0');
                    let s = String(seconds % 60).padStart(2, '0');
                    document.getElementById('timer').innerText = `${m}:${s}`;
                }, 1000);

                document.getElementById('btn-start').disabled = true;
                document.getElementById('btn-start').style.opacity = '0.5';
                document.getElementById('btn-stop').disabled = false;
                document.getElementById('btn-stop').style.opacity = '1';
                document.getElementById('status-text').innerText = "Recording Active...";
                document.getElementById('status-text').style.color = "#EF4444";
            }

            function stopRecording() {
                if (timerInterval) {
                    clearInterval(timerInterval);
                }
                if (mediaRecorder && mediaRecorder.state !== "inactive") {
                    mediaRecorder.stop();
                }
                document.getElementById('btn-start').disabled = false;
                document.getElementById('btn-start').style.opacity = '1';
                document.getElementById('btn-stop').disabled = true;
                document.getElementById('btn-stop').style.opacity = '0.5';
            }

            initCamera();
        </script>
        """
        components.html(html5_recorder, height=350)
        
        webcam_upload = st.file_uploader(
            "Drop Recorded WebM Video File Here to Analyze:",
            type=["webm", "mp4", "wav"],
            key="webcam_uploader"
        )
        if webcam_upload:
            if st.button("⚡ Analyze Recorded Video with Gemini", type="primary", use_container_width=True):
                st.session_state.is_analyzing = True
                with st.spinner("Uploading video to Gemini Files API & Extracting Multimodal Intelligence..."):
                    tmp_path = save_uploaded_media(webcam_upload)
                    st.session_state.media_file_path = tmp_path
                    res = analyze_media_file(tmp_path, st.session_state.api_key)
                    st.session_state.analysis_results = res
                    st.session_state.is_analyzing = False
                    st.session_state.completed_tasks = set()
                    st.toast("Real Video Session Analyzed!", icon="🚀")
                    st.rerun()

    elif input_mode == "📁 Upload Media File":
        uploaded_media = st.file_uploader(
            "Upload Session Recording (Video / Audio):",
            type=["webm", "mp4", "wav", "mp3", "m4a", "mov"],
            help="Upload an office meeting video or audio file for full multimodal analysis."
        )
        if uploaded_media:
            st.video(uploaded_media) if uploaded_media.name.endswith(('.mp4','.webm')) else st.audio(uploaded_media)
            if st.button("⚡ Process & Analyze Uploaded Media", type="primary", use_container_width=True):
                st.session_state.is_analyzing = True
                with st.spinner("Uploading to Gemini Files API & Extracting Multimodal Intelligence..."):
                    tmp_path = save_uploaded_media(uploaded_media)
                    st.session_state.media_file_path = tmp_path
                    res = analyze_media_file(tmp_path, st.session_state.api_key)
                    st.session_state.analysis_results = res
                    st.session_state.is_analyzing = False
                    st.session_state.completed_tasks = set()
                    st.toast("File Analysis Completed Successfully!", icon="🚀")
                    st.rerun()

    elif input_mode == "📷 Camera Snapshot":
        camera_img = st.camera_input("Take Executive Snapshot")
        if camera_img:
            if st.button("🔍 Analyze Visual Snapshot with Gemini", type="primary", use_container_width=True):
                st.session_state.is_analyzing = True
                with st.spinner("Analyzing image frame with Gemini 2.0..."):
                    tmp_path = save_uploaded_media(camera_img)
                    res = analyze_media_file(tmp_path, st.session_state.api_key)
                    st.session_state.analysis_results = res
                    st.session_state.is_analyzing = False
                    st.rerun()

    # Session Control & Quick Actions
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("##### 🛠️ Session Control Bar")
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("🔄 Reset Session", use_container_width=True):
            st.session_state.analysis_results = None
            st.session_state.completed_tasks = set()
            st.rerun()
    with c_btn2:
        if st.button("📥 Export PDF Brief", use_container_width=True):
            if st.session_state.analysis_results:
                pdf_bytes = generate_pdf_report(st.session_state.analysis_results)
                st.download_button(
                    label="⬇️ Download PDF Report",
                    data=pdf_bytes,
                    file_name="Executive_Meeting_Brief.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            else:
                st.warning("Run analysis first to generate PDF report.")


# ------------------------------------------------------------------------------
# CENTER COLUMN: REAL-TIME TRANSCRIPT STREAM & DYNAMIC ACTION ITEMS
# ------------------------------------------------------------------------------
with col_center:
    data = st.session_state.analysis_results

    # Tabs for Center View
    tab_transcript, tab_summary, tab_action = st.tabs([
        "📜 Live Transcript Stream", 
        "📝 Executive Summary", 
        "✅ Action Checklist"
    ])

    # 1. Transcript Tab (Notebook / Diary Style)
    with tab_transcript:
        st.markdown("### 🎙️ Notebook Spoken Transcript")
        if data and data.get("transcript"):
            st.markdown(f'<div class="transcript-box">{data["transcript"]}</div>', unsafe_allow_html=True)
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
            st.download_button(
                "📋 Copy / Download Raw Text Transcript",
                data=data["transcript"],
                file_name="meeting_transcript.txt",
                mime="text/plain"
            )
        else:
            st.info("No active transcript available. Start recording or load a sample preset from the sidebar.")

    # 2. Executive Summary Tab
    with tab_summary:
        st.markdown("### 📊 In-Depth Executive Summary")
        if data and data.get("summary"):
            st.markdown(f"""
            <div class="pearl-card pearl-card-platinum">
                {data["summary"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Executive summary will generate automatically post-recording.")

    # 3. Dynamic Action Items Checklist Tab
    with tab_action:
        st.markdown("### ⚡ Structured Action Items & Tasks")
        if data and data.get("action_items"):
            action_list = data["action_items"]
            
            completed_count = len(st.session_state.completed_tasks)
            total_count = len(action_list)
            
            st.progress(completed_count / total_count if total_count > 0 else 0)
            st.caption(f"Progress: {completed_count} of {total_count} tasks completed")
            
            for idx, item in enumerate(action_list):
                if isinstance(item, dict):
                    task_text = item.get("task", "")
                    assignee = item.get("assignee", "Unassigned")
                    deadline = item.get("deadline", "TBD")
                    priority = item.get("priority", "Medium")
                else:
                    task_text = str(item)
                    assignee = "Executive"
                    deadline = "TBD"
                    priority = "Medium"

                is_checked = idx in st.session_state.completed_tasks
                
                c_check, c_content = st.columns([0.1, 0.9])
                with c_check:
                    checked = st.checkbox("", value=is_checked, key=f"task_chk_{idx}")
                    if checked and idx not in st.session_state.completed_tasks:
                        st.session_state.completed_tasks.add(idx)
                        st.rerun()
                    elif not checked and idx in st.session_state.completed_tasks:
                        st.session_state.completed_tasks.remove(idx)
                        st.rerun()
                        
                with c_content:
                    style_strike = "text-decoration: line-through; opacity: 0.6;" if checked else ""
                    st.markdown(f"""
                    <div style="background: rgba(255,255,255,0.7); padding: 10px 14px; border-radius: 12px; border: 1px solid #CBD5E1; margin-bottom: 8px; {style_strike}">
                        <div style="font-weight: 600; font-size: 0.92rem; color: #1E293B;">{task_text}</div>
                        <div style="font-size: 0.78rem; color: #64748B; margin-top: 4px; display: flex; gap: 12px;">
                            <span>👤 <b>Assignee:</b> {assignee}</span>
                            <span>⏰ <b>Deadline:</b> {deadline}</span>
                            <span>🔥 <b>Priority:</b> {priority}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Action items checklist will appear here once media is analyzed.")


# ------------------------------------------------------------------------------
# RIGHT COLUMN: FOCUS GAUGES, SENTIMENT & PRIVACY ALERTS
# ------------------------------------------------------------------------------
with col_right:
    st.markdown("### 📈 Executive Intelligence Analytics")

    if data:
        focus_score = data.get("focus_score", 88)
        sentiment = data.get("sentiment", "Calm, Professional & Focused")
        alerts = data.get("alerts", "None")
        topics = data.get("key_topics", [])

        # 1. Energy & Focus Score Gauge
        st.markdown(f"""
        <div class="pearl-card pearl-card-gold" style="text-align: center;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #78350F; text-transform: uppercase; letter-spacing: 0.05em;">
                ⚡ Energy & Focus Gauge
            </div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 3.2rem; font-weight: 800; color: #1E293B; margin: 8px 0;">
                {focus_score}<span style="font-size: 1.5rem; color: #64748B;">/100</span>
            </div>
            <div style="width: 100%; background: #E2E8F0; border-radius: 10px; height: 10px; overflow: hidden;">
                <div style="width: {focus_score}%; background: linear-gradient(90deg, #F59E0B, #10B981); height: 100%; border-radius: 10px;"></div>
            </div>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 8px;">
                High active engagement detected across participants.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 2. Sentiment & Tone Meter
        st.markdown(f"""
        <div class="pearl-card">
            <div style="font-size: 0.8rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">
                🕊️ Sentiment & Tone Meter
            </div>
            <div style="font-weight: 700; font-size: 1.05rem; color: #1E293B;">
                {sentiment}
            </div>
            <div style="margin-top: 8px;">
                <span class="badge-platinum">Polite</span>
                <span class="badge-platinum">Executive</span>
                <span class="badge-platinum">Calm</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 3. Privacy & Security Alert Status
        is_warning = "warning" in alerts.lower() or "alert" in alerts.lower()
        alert_bg = "pearl-card-platinum"
        alert_icon = "🛡️"
        
        st.markdown(f"""
        <div class="pearl-card {alert_bg}">
            <div style="font-size: 0.8rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">
                {alert_icon} Privacy & Security Status
            </div>
            <div style="font-size: 0.88rem; color: #334155; font-weight: 500;">
                {alerts}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 4. Key Topic Breakdown
        if topics:
            st.markdown("""
            <div class="pearl-card">
                <div style="font-size: 0.8rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 12px;">
                    🏷️ Topic Breakdown
                </div>
            """, unsafe_allow_html=True)
            for top in topics:
                t_name = top.get("topic", "") if isinstance(top, dict) else str(top)
                t_w = top.get("weight", "33%") if isinstance(top, dict) else "33%"
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 6px;">
                    <span style="font-weight: 600; color: #334155;">{t_name}</span>
                    <span style="color: #64748B; font-weight: 700;">{t_w}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="pearl-card" style="text-align: center; padding: 40px 20px;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">📊</div>
            <div style="font-weight: 700; color: #1E293B; font-size: 1rem;">Analytics Standby</div>
            <div style="font-size: 0.82rem; color: #64748B; margin-top: 6px;">
                Focus score, sentiment meter, privacy alerts, and topic breakdown will render dynamically once a session is analyzed.
            </div>
        </div>
        """, unsafe_allow_html=True)
