import streamlit as st

# Page Configuration (Mobile and PC Responsive layout)
st.set_page_config(page_title="KAIRON Official", layout="wide")

# App State එක මඟින් පිටු (Pages) සහ Product Modals පාලනය කිරීම
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# Advanced CSS for Banners, Grid Layouts, Animations & Dark Premium Theme
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
    
    /* Navigation Buttons */
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
    
    /* Daraz-Style Premium Large Promo Banner */
    .promo-banner {
        width: 100%;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 35px;
        border: 1px solid rgba(0, 229, 255, 0.2);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        transition: transform 0.4s ease;
    }
    .promo-banner:hover {
        transform: scale(1.01);
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

# 1. HOME PAGE
if st.session_state.current_page == "Home":
    # සයිට් එක මැදට දමා ඇති ලස්සන Flash Sale බැනරය
    st.markdown("""
        <div class="promo-banner">
            <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200&q=80" width="100%" style="display:block; object-fit:cover; max-height:400px;">
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align:center; color:#B3B3B3;'>Welcome to KAIRON Ecosystem</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666;'>Select a tab from the navigation bar to start exploring.</p>", unsafe_allow_html=True)

# 2. ABOUT PAGE
elif st.session_state.current_page == "About":
    st.markdown('<h2 class="section-title">Who We Are</h2>', unsafe_allow_html=True)
    st.markdown("<p class='desc-text'>KAIRON is a forward-thinking technology company specialized in software architecture, hardware optimization, and creative engineering.</p>", unsafe_allow_html=True)

# 3. STUDIOS PAGE
elif st.session_state.current_page == "Studios":
    st.markdown('<h2 class="section-title">Our Ecosystem</h2>', unsafe_allow_html=True)
    st.markdown("<p class='desc-text'>Fantx Studio - Our dedicated creative gaming division, currently developing immersive 3D atmospheric horror games.</p>", unsafe_allow_html=True)

# 4. PREMIUM TECH MARKETPLACE PAGE
elif st.session_state.current_page == "Shop":
    
    # මැදට දමා ඇති ලස්සන Daraz Style Flash Sale බැනරය
    st.markdown("""
        <div class="promo-banner">
            <img src="https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1200&q=80" width="100%" style="display:block; object-fit:cover; max-height:350px;">
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">KAIRON Tech Marketplace</h2>', unsafe_allow_html=True)
    
    # මෙතන තියෙන්නේ බඩු වල විස්තර (ඔයාට ඕන විදිහට මේ ටෙක්ස්ට්ස් වෙනස් කරන්න පුළුවන්)
    products = {
        "p1": {
            "title": "KAIRON 8GB DDR3 PC RAM",
            "price": "රු. 7,733",
            "image": "https://images.unsplash.com/photo-1562976540-1502c2145186?w=500",
            "desc": "High-performance 8GB DDR3 1333MHz Desktop Memory Module. Optimized for multitasking and stability.",
            "specs": "Capacity: 8GB | Speed: 1333MHz | Type: DDR3 | Warranty: 1 Year"
        },
        "p2": {
            "title": "KAIRON Cyber Audio V2",
            "price": "රු. 22,500",
            "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
            "desc": "Immersive 7.1 Surround Sound gaming headset. Features premium noise-canceling microphone.",
            "specs": "Driver: 50mm Neodymium | Connectivity: Wired USB | RGB Support"
        },
        "p3": {
            "title": "KAIRON Smart Watch X",
            "price": "රු. 18,900",
            "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
            "desc": "Next-gen fitness tracker and smart assistant. Supports bluetooth calling and real-time health metrics.",
            "specs": "Display: 1.96-inch AMOLED | Waterproof: IP68 | Battery: 14 Days"
        }
    }
    
    # Product එකක් ක්ලික් කරපු ගමන් විස්තර පෙන්වන තැන
    if st.session_state.selected_product:
        p_id = st.session_state.selected_product
        selected = products[p_id]
        
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

    # Products Grid
    shop_col1, shop_col2, shop_col3 = st.columns(3)
    
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
    </div>
    """, unsafe_allow_html=True)
