import streamlit as st

# Page Configuration
st.set_page_config(page_title="KAIRON Official", layout="wide")

# Custom CSS for Premium Tech Dark Theme
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
        font-family: 'Inter', 'Poppins', sans-serif;
    }
    
    /* A. Fixed Header Styles */
    .custom-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: rgba(18, 18, 18, 0.95);
        border-bottom: 1px solid rgba(0, 229, 255, 0.2);
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 9999;
    }
    .header-logo {
        color: #00E5FF;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 2px;
        text-decoration: none;
    }
    .header-nav a {
        color: #FFFFFF;
        text-decoration: none;
        margin-left: 25px;
        font-weight: 500;
        transition: 0.3s;
    }
    .header-nav a:hover {
        color: #00E5FF;
        text-shadow: 0 0 10px #00E5FF;
    }
    
    /* Padding to prevent content from hiding under fixed header */
    .content-wrapper {
        margin-top: 100px;
    }
    
    /* B. Hero Section Styles */
    .hero-container {
        text-align: center;
        padding: 80px 20px;
    }
    .hero-title {
        color: #00E5FF;
        font-size: 52px;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(0, 229, 255, 0.3);
        margin-bottom: 20px;
    }
    .hero-subtitle {
        color: #B3B3B3;
        font-size: 20px;
        max-width: 800px;
        margin: 0 auto 40px auto;
        line-height: 1.6;
    }
    
    /* Custom Neon Button */
    .hero-btn {
        background-color: #00E5FF;
        color: #121212;
        border: none;
        padding: 14px 35px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
        text-decoration: none;
        display: inline-block;
    }
    .hero-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 25px #00E5FF;
        color: #121212;
    }
    
    /* Section Headers */
    .section-title {
        color: #00E5FF;
        font-size: 32px;
        font-weight: 700;
        margin-top: 50px;
        margin-bottom: 20px;
        border-left: 4px solid #00E5FF;
        padding-left: 15px;
    }
    
    /* Tech Description Text */
    .desc-text {
        color: #B3B3B3;
        font-size: 18px;
        line-height: 1.7;
    }
    
    /* D. Brand Feature Card */
    .brand-card {
        background: linear-gradient(145deg, #1a1a1a, #222222);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 30px;
        margin-top: 20px;
        transition: 0.3s;
    }
    .brand-card:hover {
        border-color: #00E5FF;
        box-shadow: 0 0 20px rgba(0, 229, 255, 0.1);
    }
    .brand-title {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .spotlight-tag {
        background-color: rgba(0, 229, 255, 0.1);
        color: #00E5FF;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        display: inline-block;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# A. HEADER & NAVIGATION (Fixed at Top)
# ==========================================
st.markdown("""
    <div class="custom-header">
        <a href="#" class="header-logo">KAIRON</a>
        <div class="header-nav">
            <a href="#">Home</a>
            <a href="#">Our Studios</a>
            <a href="#">Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Start Content Wrapper (to push content below fixed header)
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# ==========================================
# B. HERO SECTION (Main Banner)
# ==========================================
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">KAIRON: The Future of Tech & Innovation</h1>
        <p class="hero-subtitle">We build high-performance digital experiences, interactive media, and next-generation software solutions.</p>
        <a href="#" class="hero-btn">Explore Our Work</a>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Layout adjustments for Content
col_left, col_right = st.columns([2, 1.5])

with col_left:
    # ==========================================
    # C. ABOUT KAIRON
    # ==========================================
    st.markdown('<h2 class="section-title">Who We Are</h2>', unsafe_allow_html=True)
    st.markdown("""
        <p class="desc-text">
        KAIRON is a forward-thinking technology company specialized in software architecture, 
        hardware optimization, and creative engineering. We push the boundaries of what's possible.
        </p>
        """, unsafe_allow_html=True)

with col_right:
    # ==========================================
    # D. OUR ECOSYSTEM / BRANDS (Card Design)
    # ==========================================
    st.markdown('<h2 class="section-title">Our Ecosystem</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="brand-card">
            <div class="brand-title">Fantx Studio</div>
            <p class="desc-text" style="font-size: 16px;">
            Our dedicated creative gaming division, currently developing immersive 3D atmospheric horror games.
            </p>
            <div class="spotlight-tag">🚨 Project Spotlight: Kanchi the scary teacher - chapter 1</div>
        </div>
        """, unsafe_allow_html=True)

# Close Content Wrapper
st.markdown('</div>', unsafe_allow_html=True)
