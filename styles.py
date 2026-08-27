"""
styles.py - Custom Styling & CSS Engine for AI Office Copilot & Executive Assistant
Pearl Glassmorphism with Soft Platinum Metallic Accents
"""

import streamlit as st

PEARL_GLASS_CSS = """
<style>
/* ==========================================================================
   GLOBAL RESET & FONTS
   ========================================================================== */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="st-"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    color: #334155 !important; /* Soft Metallic Charcoal - NO pure black #000000 */
}

/* Base App Background - Pearlescent White to Soft Warm Slate */
.stApp {
    background: linear-gradient(135deg, #F8FAFC 0%, #F0F4F8 40%, #E2E8F0 100%) !important;
    background-attachment: fixed !important;
}

/* Hide default streamlit header/footer decorations for a clean desktop feel */
header[data-testid="stHeader"] {
    background: rgba(248, 250, 252, 0.6) !important;
    backdrop-filter: blur(12px) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.8) !important;
}

footer {
    visibility: hidden;
}

/* ==========================================================================
   STRICT SIDEBAR OVERRIDES (DARK MODE COMPATIBILITY FIX)
   ========================================================================== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 100%) !important;
    border-right: 1.5px solid #CBD5E1 !important;
    box-shadow: 4px 0 20px rgba(148, 163, 184, 0.1) !important;
}

section[data-testid="stSidebar"] *, 
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] h5 {
    color: #334155 !important;
}

/* Sidebar Inputs & Selectbox Contrast Fix */
section[data-testid="stSidebar"] input {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    border: 1.5px solid #CBD5E1 !important;
    border-radius: 12px !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    border: 1.5px solid #CBD5E1 !important;
    border-radius: 12px !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] span {
    color: #1E293B !important;
}

/* ==========================================================================
   PEARL GLASS CARDS & FRAMES
   ========================================================================== */
.pearl-card {
    position: relative;
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    border: 1.5px solid transparent;
    border-image: linear-gradient(135deg, #ffffff, #cbd5e1, #ffffff) 1;
    box-shadow: 0 10px 30px rgba(226, 232, 240, 0.8), 
                0 4px 12px rgba(148, 163, 184, 0.08),
                inset 0 1px 1px rgba(255, 255, 255, 0.9);
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    overflow: hidden;
}

.pearl-card::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 140px;
    height: 140px;
    background: radial-gradient(circle at top right, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0) 70%);
    pointer-events: none;
    z-index: 1;
    border-radius: 0 20px 0 100%;
}

.pearl-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 16px 40px rgba(203, 213, 225, 0.9), 
                0 6px 16px rgba(148, 163, 184, 0.12),
                inset 0 1px 2px rgba(255, 255, 255, 1);
    border-color: rgba(203, 213, 225, 0.8);
}

.pearl-card-gold {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(245, 230, 211, 0.45));
    border: 1.5px solid rgba(234, 216, 195, 0.8);
}

.pearl-card-platinum {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(230, 233, 240, 0.5));
    border: 1.5px solid rgba(203, 213, 225, 0.9);
}

/* ==========================================================================
   HEADINGS & TYPOGRAPHY
   ========================================================================== */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif !important;
    color: #1E293B !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
}

.header-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #1E293B 0%, #475569 50%, #64748B 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    padding: 0;
}

.header-subtitle {
    font-size: 0.95rem;
    color: #64748B;
    font-weight: 500;
    margin-top: 4px;
}

/* ==========================================================================
   BUTTONS & CONTROLS
   ========================================================================== */
.stButton > button {
    border-radius: 14px !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    letter-spacing: 0.01em !important;
    padding: 0.65rem 1.4rem !important;
    border: 1.5px solid rgba(203, 213, 225, 0.9) !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%) !important;
    color: #334155 !important;
    box-shadow: 0 4px 12px rgba(226, 232, 240, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;
    transition: all 0.25s ease !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%) !important;
    box-shadow: 0 6px 18px rgba(203, 213, 225, 0.9) !important;
    border-color: #CBD5E1 !important;
    color: #0F172A !important;
}

.stButton > button[kind="primary"], div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #475569 0%, #334155 100%) !important;
    color: #F8FAFC !important;
    border: 1px solid #334155 !important;
    box-shadow: 0 6px 20px rgba(51, 65, 85, 0.25) !important;
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #334155 0%, #1E293B 100%) !important;
    color: #FFFFFF !important;
    box-shadow: 0 8px 24px rgba(30, 41, 59, 0.35) !important;
}

/* ==========================================================================
   METRICS & GAUGES
   ========================================================================== */
div[data-testid="stMetricValue"] {
    font-family: 'Outfit', sans-serif !important;
    font-size: 2.1rem !important;
    font-weight: 700 !important;
    color: #1E293B !important;
}

div[data-testid="stMetricLabel"] {
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    color: #64748B !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

/* ==========================================================================
   TABS & NAVIGATION
   ========================================================================== */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px !important;
    background: rgba(226, 232, 240, 0.6) !important;
    padding: 6px !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255, 255, 255, 0.8) !important;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 12px !important;
    padding: 8px 18px !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    color: #475569 !important;
    border: none !important;
    background: transparent !important;
    transition: all 0.2s ease !important;
}

.stTabs [aria-selected="true"] {
    background: #FFFFFF !important;
    color: #1E293B !important;
    box-shadow: 0 4px 12px rgba(148, 163, 184, 0.25) !important;
}

/* ==========================================================================
   NOTEBOOK DIARY TRANSCRIPT STYLE
   ========================================================================== */
.transcript-box {
    background: #FAFAFA;
    background-image: linear-gradient(#E2E8F0 1px, transparent 1px);
    background-size: 100% 2.2rem;
    line-height: 2.2rem;
    padding: 20px 24px;
    border-radius: 16px;
    border-left: 4px solid #475569;
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.03);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.95rem;
    color: #334155;
    max-height: 380px;
    overflow-y: auto;
}

.transcript-speaker {
    display: inline-block;
    font-weight: 700;
    color: #1E293B;
    background: #E2E8F0;
    padding: 2px 10px;
    border-radius: 8px;
    font-size: 0.8rem;
    margin-right: 8px;
}

/* ==========================================================================
   BADGES & ACCENT PILLS
   ========================================================================== */
.badge-platinum {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, #E6E9F0, #E2E8F0);
    color: #334155;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.8);
    box-shadow: 0 2px 6px rgba(148, 163, 184, 0.15);
}

.badge-gold {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, #F5E6D3, #EAD8C3);
    color: #78350F;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.9);
}

.badge-pulse-green {
    display: inline-block;
    width: 8px;
    height: 8px;
    background-color: #10B981;
    border-radius: 50%;
    box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
    animation: pulse-green 1.8s infinite;
}

@keyframes pulse-green {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.badge-pulse-red {
    display: inline-block;
    width: 8px;
    height: 8px;
    background-color: #EF4444;
    border-radius: 50%;
    box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7);
    animation: pulse-red 1.5s infinite;
}

@keyframes pulse-red {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(239, 68, 68, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
}

/* ==========================================================================
   PROGRESS BAR & METERS
   ========================================================================== */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #94A3B8 0%, #334155 100%) !important;
    border-radius: 10px !important;
}

.stProgress > div > div {
    background-color: #E2E8F0 !important;
    border-radius: 10px !important;
    height: 10px !important;
}

div[data-testid="stCheckbox"] label {
    font-size: 0.92rem !important;
    color: #334155 !important;
    font-weight: 500 !important;
}

.stExpander {
    background: rgba(255, 255, 255, 0.8) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    box-shadow: 0 4px 12px rgba(226, 232, 240, 0.4) !important;
}
</style>
"""

def inject_styles():
    """Inject Pearl Glassmorphism CSS into current Streamlit session."""
    st.markdown(PEARL_GLASS_CSS, unsafe_allow_html=True)
