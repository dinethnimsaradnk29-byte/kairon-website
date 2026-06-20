import streamlit as st

# Page Configuration (Mobile and PC Responsive layout)
st.set_page_config(page_title="KAIRON Official", layout="wide")

# App State එක මඟින් පිටු (Pages) පාලනය කිරීම
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Advanced CSS for Colors, Animations, Responsive Tweaks & Footer
st.markdown("""
    <style>
    /* Global Background & Font */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
        font-family: 'Inter', 'Poppins', sans-serif;
    }
    
    /* Brand Logo Style */
    .header-logo {
        color: #00E5FF;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 3px;
        text-align: center;
        margin-bottom: 15px;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.2);
    }
    
    /* Smooth CSS Hover Animations for Buttons */
    .stButton>button {
        background-color: transparent !important;
        color: #B3B3B3 !important;
        border: 1px solid #333 !important;
        transition: all 0.3s ease-in-out !important;
        border-radius: 6px !important;
    }
    .stButton>button:hover {
        color: #00E5FF !important;
        border-color: #00E5FF !important;
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.4) !important;
        transform: translateY(-2px);
    }
    
    /* Hero Banner Styles */
    .hero-container {
        text-align: center;
        padding: 80px 20px;
    }
    .hero-title {
        color: #00E5FF;
        font-size: calc(24px + 2vw); /* Responsive Font Size */
        font-weight: 800;
        text-shadow: 0 0 20px rgba(0, 229, 255, 0.3);
        margin-bottom: 20px;
    }
    .hero-subtitle {
        color: #B3B3B3;
        font-size: 18px;
        max-width: 800px;
        margin: 0 auto 40px auto;
        line-height: 1.6;
    }
    
    /* Section Structure */
    .section-title {
        color: #00E5FF;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 20px;
        border-left: 4px solid #00E5FF;
        padding-left: 15px;
    }
    .desc-text {
        color: #B3B3B3;
        font-size: 16px;
        line-height: 1.7;
    }
    
    /* Premium Brand Card Grid */
    .brand-card {
        background: linear-gradient(145deg, #161616, #1f1f1f);
        border: 1px solid rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 30px;
        transition: 0.3s ease;
    }
    .brand-card:hover {
        border-color: #00E5FF;
        box-shadow: 0 0 20px rgba(0, 229, 255, 0.15);
    }
    .spotlight-tag {
        background-color: rgba(0, 229, 255, 0.1);
        color: #00E5FF;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: bold;
        display: inline-block;
        margin-top: 15px;
    }
    
    /* Product Card grid style */
    .product-card {
        background-color: #161616;
        border: 1px solid #222;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .product-card:hover {
        border-color: #00E5FF;
    }
    
    /* Footer Design */
    .custom-footer {
        margin-top: 80px;
        padding: 30px 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center;
        color: #666666;
        font-size: 14px;
    }
    .footer-highlight {
        color: #B3B3B3;
        font-size: 12px;
        margin-top: 5px;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# RESPONSIVE HEADER & NAVBAR
# ==========================================
st.markdown('<div class="header-logo">KAIRON</div>', unsafe_allow_html=True)

# PC සහ Mobile දෙකටම ගැළපෙන සේ Navigation Buttons 4 සකස් කිරීම
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
with nav_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "Home"
with nav_col2:
    if st.button("🏢 About", use_container_width=True):
        st.session_state.current_page = "About"
with nav_col3:
    if st.button("🎮 Studios", use_container_width=True):
        st.session_state.current_page = "Studios"
with nav_col4:
    if st.button("🛒 Shop", use_container_width=True):
        st.session_state.current_page = "Shop"

st.markdown("<hr style='border-color: rgba(0,229,255,0.1); margin-top:5px;'>", unsafe_allow_html=True)

# ==========================================
# PAGE MANAGER (පිටු පාලනය)
# ==========================================

# 1. HOME PAGE & HERO SECTION
if st.session_state.current_page == "Home":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">KAIRON: The Future of Tech & Innovation</h1>
            <p class="hero-subtitle">We build high-performance digital experiences, interactive media, and next-generation software solutions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # "Explore Our Work" බටන් එක (ක්ලික් කළ විට Shop එකට යයි)
    _, btn_center_col, _ = st.columns([1.5, 1, 1.5])
    with btn_center_col:
        if st.button("Explore Our Work ⚡", use_container_width=True, key="explore_btn"):
            st.session_state.current_page = "Shop"
            st.rerun()

# 2. ABOUT PAGE
elif st.session_state.current_page == "About":
    st.markdown('<h2 class="section-title">Who We Are</h2>', unsafe_allow_html=True)
    st.markdown("""
        <p class="desc-text">
        KAIRON is a forward-thinking technology company specialized in software architecture, 
        hardware optimization, and creative engineering. We push the boundaries of what's possible.
        </p>
        """, unsafe_allow_html=True)

# 3. STUDIOS PAGE
elif st.session_state.current_page == "Studios":
    st.markdown('<h2 class="section-title">Our Ecosystem</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="brand-card">
            <div class="brand-title" style="font-size:24px; font-weight:bold; color:#fff;">Fantx Studio</div>
            <p class="desc-text" style="margin-top:10px;">
            Our dedicated creative gaming division, currently developing immersive 3D atmospheric horror games.
            </p>
            <div class="spotlight-tag">📡 Project Spotlight: Kanchi the scary teacher - chapter 1</div>
        </div>
        """, unsafe_allow_html=True)

# 4. SHOP PAGE (Daraz Marketplace)
elif st.session_state.current_page == "Shop":
    st.markdown('<h2 class="section-title">KAIRON Marketplace</h2>', unsafe_allow_html=True)
    
    shop_col1, shop_col2, shop_col3 = st.columns(3)
    
    with shop_col1:
        st.markdown("""
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff" width="100%" style="border-radius:5px;">
                <h3 style='color:white; margin-top:15px;'>KAIRON Pro Sneakers</h3>
                <p style="color:#00E5FF; font-weight:bold; font-size:18px;">රු. 15,000</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Buy Now", key="shop_p1", use_container_width=True):
            st.success("Added to Cart!")
            
    with shop_col2:
        st.markdown("""
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e" width="100%" style="border-radius:5px;">
                <h3 style='color:white; margin-top:15px;'>Cyber Audio Headphone</h3>
                <p style="color:#00E5FF; font-weight:bold; font-size:18px;">රු. 22,500</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Buy Now", key="shop_p2", use_container_width=True):
            st.success("Added to Cart!")
            
    with shop_col3:
        st.markdown("""
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30" width="100%" style="border-radius:5px;">
                <h3 style='color:white; margin-top:15px;'>KAIRON Smart Watch</h3>
                <p style="color:#00E5FF; font-weight:bold; font-size:18px;">රු. 18,900</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Buy Now", key="shop_p3", use_container_width=True):
            st.success("Added to Cart!")

# ==========================================
# FOOTER SECTION (යටම කොටස)
# ==========================================
st.markdown("""
    <div class="custom-footer">
        <div>© 2026 KAIRON Official. All Rights Reserved.</div>
        <div class="footer-highlight">Built for the next generation.</div>
    </div>
    """, unsafe_allow_html=True)
