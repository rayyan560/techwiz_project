# AI Office Copilot & Executive Assistant 💼

An executive-grade multimodal web application powered by **Python**, **Streamlit**, and **Google Gemini API (`gemini-3.6-flash`)**. Featuring a **Pearl Glassmorphism with Soft Platinum Metallic** visual design system.

---

## 🌟 Key Features

1. **Pearl Glassmorphism & Platinum Aesthetic**: Pearlescent background gradients, glossy pearl white cards with specular mirror light reflections, 1.5px metallic gradient borders, and metallic charcoal typography (`#334155`).
2. **Multimodal Media Capture**:
   - **`🎙️ Mic Audio Recorder`**: 1-Click live speech/audio recording.
   - **`📹 Browser Webcam`**: Live camera preview & HTML5 WebM recorder.
   - **`📁 Upload Media File`**: Support for `.webm`, `.mp4`, `.wav`, `.mp3`, `.m4a`.
3. **Google Gemini 3.6 Flash Intelligence**:
   - Spoken transcript generation with automatic **Urdu/Hindi to English Translation**.
   - In-depth executive summary & strategic takeaways.
   - Dynamic action items checklist with state tracking.
   - Energy & Focus Score radial gauge (0-100%).
   - Sentiment & Tone meter.
   - Privacy & Security compliance scanner.
4. **1-Click Executive PDF Brief Export**: Formatted PDF report export generated via ReportLab.

---

## 🚀 Quick Start Guide

### 1. Clone Repository
```bash
git clone https://github.com/rayyan560/techwiz_project.git
cd techwiz_project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Gemini API Key (Optional)
```bash
set GEMINI_API_KEY="your_actual_gemini_api_key"
```

### 4. Launch Streamlit Application
```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```
techwiz_project/
├── app.py              # Main Streamlit Web Application & 3-Column UI
├── ai_engine.py        # Gemini Multimodal API Engine (gemini-3.6-flash)
├── styles.py           # Pearl Glassmorphism & Platinum CSS Theme Engine
├── utils.py            # Executive PDF Brief Generator (ReportLab)
├── requirements.txt    # Python Dependencies
├── .gitignore          # Git exclusion rules
└── README.md           # Documentation
```
