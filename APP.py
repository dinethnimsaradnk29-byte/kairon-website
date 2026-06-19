import streamlit as st

# Page Configuration
st.set_page_config(page_title="KAIRON Official", layout="wide")

# App State එක මඟින් දැනට ඉන්න පිටුව (Page) තබා ගැනීම
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Custom CSS for Premium Tech Dark Theme
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
        font-family: 'Inter', 'Poppins', sans-serif;
    }
    
    /* Header Design */
    .custom-header {
        background-color: rgba(18, 18, 18, 0.95);
        border-bottom: 1px solid rgba(0, 229, 255, 0.2);
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }
    .header-logo {
        color: #00E5FF;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 2px;
    }
    
    /* Hero Section Styles */
    .hero-container {
        text-align: center;
        padding: 60px 20px;
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
    
    /* Section Headers */
    .section-title {
        color: #00E5FF;
        font-size: 32px;
        font-weight: 700;
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
    
    /* Brand Feature Card */
    .brand-card {
        background: linear-gradient(145deg, #1a1a1a, #222222);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 30px;
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
    
    /* Product Card Styles */
    .product-card {
        background-color: #1A1A1A;
        border: 1px solid #222;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    .product-price {
        color: #00E5FF;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# HEADER & NAVIGATION SYSTEM
# ==========================================
# Streamlit වල බොත්තම් උඩින්ම තියන්න Columns පාවිච්චි කිරීම
head_col1, head_col2, head_col3, head_col4, head_col5 = st.columns([2, 1, 1, 1, 1])

with head_col1:
    st.markdown('<div class="header-logo">KAIRON</div>', unsafe_allow_html=True)
with head_col2:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "Home"
with head_col3:
    if st.button("🏢 About", use_container_width=True):
        st.session_state.current_page = "About"
with head_col4:
    if st.button("🎮 Studios", use_container_width=True):
        st.session_state.current_page = "Studios"
with head_col5:
    if st.button("🛒 Shop (Daraz)", use_container_width=True):
        st.session_state.current_page = "Shop"

st.markdown("<hr style='border-color: rgba(0,229,255,0.2); margin-top:0;'>", unsafe_allow_html=True)

# ==========================================
# PAGE CONTENT CONTROLLER
# ==========================================

# 1. HOME PAGE
if st.session_state.current_page == "Home":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">KAIRON: The Future of Tech & Innovation</h1>
            <p class="hero-subtitle">We build high-performance digital experiences, interactive media, and next-generation software solutions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("Explore Our Shop Now 🚀"):
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
            <div class="brand-title">Fantx Studio</div>
            <p class="desc-text" style="font-size: 16px;">
            Our dedicated creative gaming division, currently developing immersive 3D atmospheric horror games.
            </p>
            <div class="spotlight-tag">🚨 Project Spotlight: Kanchi the scary teacher - chapter 1</div>
        </div>
        """, unsafe_allow_html=True)

# 4. SHOP PAGE (Daraz වගේ විකුණන බඩු දාන තැන)
elif st.session_state.current_page == "Shop":
    st.markdown('<h2 class="section-title">KAIRON Marketplace</h2>', unsafe_allow_html=True)
    st.write("Daraz වගේ අපේ බඩු විකුණන්න තියෙන නිල Marketplace එක මෙන්න:")
    
    shop_col1, shop_col2, shop_col3 = st.columns(3)
    
    with shop_col1:
        st.markdown("""
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff" width="100%">
                <h3 style='color:white;'>KAIRON Speed Sneakers</h3>
                <p class="product-price">රු. 15,000</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Buy Now", key="p1"):
            st.success("Added to Cart!")
            
    with shop_col2:
        st.markdown("""
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e" width="100%">
                <h3 style='color:white;'>KAIRON Cyber Audio V2</h3>
                <p class="product-price">රු 22,500</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Buy Now", key="p2"):
            st.success("Added to Cart!")
            
    with shop_col3:
        st.markdown("""
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30" width="100%">
                <h3 style='color:white;'>KAIRON Smart Watch X</h3>
                <p class="product-price">රු. 18,900</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Buy Now", key="p3"):
            st.success("Added to Cart!")
