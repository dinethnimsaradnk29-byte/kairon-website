import streamlit as st

# Page Configuration (Mobile and PC Responsive layout)
st.set_page_config(page_title="KAIRON Official", layout="wide")

# App State එක මඟින් පිටු (Pages) සහ Product Modals පාලනය කිරීම
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# Advanced CSS for Colors, Animations, Responsive Tweaks, Cards & Footer
st.markdown("""
    <style>
    /* Global Background & Font */
    .stApp {
        background-color: #0B0C10;
        color: #FFFFFF;
        font-family: 'Inter', 'Poppins', sans-serif;
    }
    
    /* Brand Logo Style */
    .header-logo {
        color: #00E5FF;
        font-size: 36px;
        font-weight: 900;
        letter-spacing: 4px;
        text-align: center;
        margin-bottom: 15px;
        text-shadow: 0 0 15px rgba(0, 229, 255, 0.3);
    }
    
    /* Smooth CSS Hover Animations for Navigation Buttons */
    .stButton>button {
        background-color: rgba(255, 255, 255, 0.03) !important;
        color: #B3B3B3 !important;
        border: 1px solid #222 !important;
        transition: all 0.3s ease-in-out !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
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
        padding: 60px 20px;
    }
    .hero-title {
        background: linear-gradient(45deg, #00E5FF, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: calc(26px + 2vw); /* Responsive Font Size */
        font-weight: 800;
        margin-bottom: 20px;
    }
    .hero-subtitle {
        color: #999999;
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
        margin-bottom: 25px;
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
        background: linear-gradient(145deg, #11141a, #1a1f29);
        border: 1px solid rgba(0, 229, 255, 0.1);
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
    
    /* Daraz-Inspired Premium Product Card Style */
    .product-card {
        background-color: #12161F;
        border: 1px solid #1F2633;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease;
        margin-bottom: 10px;
    }
    .product-card:hover {
        border-color: #00E5FF;
        box-shadow: 0 8px 25px rgba(0, 229, 255, 0.15);
        transform: translateY(-4px);
    }
    .product-title {
        color: #FFFFFF;
        font-size: 18px;
        font-weight: 600;
        margin: 12px 0 6px 0;
        height: 25px;
        overflow: hidden;
    }
    .product-price {
        color: #00E5FF;
        font-weight: 700;
        font-size: 20px;
        margin-bottom: 10px;
    }
    .flash-tag {
        background: linear-gradient(90deg, #FF3E6C, #FF6B6B);
        color: white;
        font-size: 11px;
        font-weight: bold;
        padding: 3px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    /* Product Info Modal View */
    .modal-container {
        background-color: #12161F;
        border: 1px solid #00E5FF;
        border-radius: 12px;
        padding: 25px;
        margin-top: 20px;
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

# Navigation Buttons
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
with nav_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "Home"
        st.session_state.selected_product = None
with nav_col2:
    if st.button("🏢 About", use_container_width=True):
        st.session_state.current_page = "About"
        st.session_state.selected_product = None
with nav_col3:
    if st.button("🎮 Studios", use_container_width=True):
        st.session_state.current_page = "Studios"
        st.session_state.selected_product = None
with nav_col4:
    if st.button("🛒 Marketplace", use_container_width=True):
        st.session_state.current_page = "Shop"
        st.session_state.selected_product = None

st.markdown("<hr style='border-color: rgba(0,229,255,0.1); margin-top:5px;'>", unsafe_allow_html=True)

# ==========================================
# PAGE MANAGER (පිටු පාලනය)
# ==========================================

# 1. HOME PAGE & HERO SECTION
if st.session_state.current_page == "Home":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">KAIRON: The Future of Tech & Innovation</h1>
            <p class="hero-subtitle">We build high-performance digital experiences, interactive media, and next-generation software and hardware optimization.</p>
        </div>
        """, unsafe_allow_html=True)
    
    _, btn_center_col, _ = st.columns([1.5, 1, 1.5])
    with btn_center_col:
        if st.button("Enter KAIRON Store ⚡", use_container_width=True, key="explore_btn"):
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

# 4. PREMIUM DARAZ-STYLE MARKETPLACE PAGE
elif st.session_state.current_page == "Shop":
    st.markdown('<h2 class="section-title">KAIRON Tech Marketplace</h2>', unsafe_allow_html=True)
    
    # Products Data Repository (බඩු වල විස්තර මෙතන තියෙන්නේ)
    products = {
        "p1": {
            "title": "KAIRON 8GB DDR3 PC RAM",
            "price": "රු. 7,733",
            "image": "https://images.unsplash.com/photo-1562976540-1502c2145186?w=500",
            "desc": "High-performance 8GB DDR3 1333MHz Desktop Memory Module. Optimized for multitasking and stability on H110 and older motherboards.",
            "specs": "Capacity: 8GB | Speed: 1333MHz | Type: DDR3 PC3L | Warranty: 1 Year"
        },
        "p2": {
            "title": "KAIRON Cyber Audio V2",
            "price": "රු. 22,500",
            "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
            "desc": "Immersive 7.1 Surround Sound gaming headset. Features premium noise-canceling microphone and breathable cyber-RGB earcups.",
            "specs": "Driver: 50mm Neodymium | Connectivity: Wired USB / 3.5mm | RGB: Dynamic Neon Cyan"
        },
        "p3": {
            "title": "KAIRON Smart Watch X",
            "price": "රු. 18,900",
            "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
            "desc": "Next-gen fitness tracker and smart assistant. Supports bluetooth calling, real-time health metrics, and long-lasting 14-day battery life.",
            "specs": "Display: 1.96-inch AMOLED | Waterproof: IP68 | Battery: 300mAh"
        }
    }
    
    # Product විස්තරයක් දැනටමත් ඕපන් කරලා නම් තියෙන්නේ ඒක උඩින්ම පෙන්වනවා (Interactive View)
    if st.session_state.selected_product:
        p_id = st.session_state.selected_product
        selected = products[p_id]
        
        # Details View Layout
        st.markdown(f"""
        <div class="modal-container">
            <h3 style="color:#00E5FF; margin-bottom:5px;">{selected['title']}</h3>
            <p style="color:#FF3E6C; font-weight:bold; font-size:22px; margin-bottom:15px;">{selected['price']}</p>
            <p style="color:#B3B3B3; font-size:16px; line-height:1.6;"><b>Product Description:</b><br>{selected['desc']}</p>
            <p style="color:#666666; font-size:14px; margin-top:10px;"><b>Specifications:</b> {selected['specs']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_m1, col_m2 = st.columns([1, 5])
        with col_m1:
            if st.button("🛒 Buy Now", key="modal_buy", use_container_width=True):
                st.success("Successfully Added to Cart!")
        with col_m2:
            if st.button("❌ Close Details", key="modal_close", use_container_width=True):
                st.session_state.selected_product = None
                st.rerun()
                
        st.markdown("<br><hr style='border-color:rgba(255,255,255,0.05);'><br>", unsafe_allow_html=True)

    # Grid Display (බඩු ටික පේළියට පෙන්වන තැන)
    shop_col1, shop_col2, shop_col3 = st.columns(3)
    
    # Product 1
    with shop_col1:
        st.markdown(f"""
            <div class="product-card">
                <span class="flash-tag">🔥 GEMS SAVE Rs. 155</span>
                <img src="{products['p1']['image']}" width="100%" style="border-radius:8px; height:200px; object-fit:cover;">
                <div class="product-title">{products['p1']['title']}</div>
                <div class="product-price">{products['p1']['price']}</div>
            </div>
            """, unsafe_allow_html=True)
        if st.button("🔎 View Details", key="btn_p1", use_container_width=True):
            st.session_state.selected_product = "p1"
            st.rerun()
            
    # Product 2
    with shop_col2:
        st.markdown(f"""
            <div class="product-card">
                <span class="flash-tag">🔥 FLASH SALE DELIVER</span>
                <img src="{products['p2']['image']}" width="100%" style="border-radius:8px; height:200px; object-fit:cover;">
                <div class="product-title">{products['p2']['title']}</div>
                <div class="product-price">{products['p2']['price']}</div>
            </div>
            """, unsafe_allow_html=True)
        if st.button("🔎 View Details", key="btn_p2", use_container_width=True):
            st.session_state.selected_product = "p2"
            st.rerun()
            
    # Product 3
    with shop_col3:
        st.markdown(f"""
            <div class="product-card">
                <span class="flash-tag">🔥 BEST MATCH</span>
                <img src="{products['p3']['image']}" width="100%" style="border-radius:8px; height:200px; object-fit:cover;">
                <div class="product-title">{products['p3']['title']}</div>
                <div class="product-price">{products['p3']['price']}</div>
            </div>
            """, unsafe_allow_html=True)
        if st.button("🔎 View Details", key="btn_p3", use_container_width=True):
            st.session_state.selected_product = "p3"
            st.rerun()

# ==========================================
# FOOTER SECTION
# ==========================================
st.markdown("""
    <div class="custom-footer">
        <div>© 2026 KAIRON Official. All Rights Reserved.</div>
        <div class="footer-highlight">Built for the next generation.</div>
    </div>
    """, unsafe_allow_html=True)
