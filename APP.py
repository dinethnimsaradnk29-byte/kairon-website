import streamlit as st

# 1. Page එකේ settings සහ CSS මඟින් Dark Theme එක සැකසීම
st.set_page_config(page_title="KAIRON Official", layout="wide")

# CSS පාවිච්චි කරලා ඔයා කියපු පාටවල් (Matte Black & Neon Cyan) ඇතුළත් කිරීම
st.markdown(f"""
    <style>
    /* මුළු සයිට් එකේම පසුබිම තද කළු කිරීම */
    .stApp {{
        background-color: #121212;
        color: #FFFFFF;
        font-family: 'Inter', 'Poppins', sans-serif;
    }}
    
    /* Neon Cyan මාතෘකා */
    .neon-title {{
        color: #00E5FF;
        font-size: 42px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    
    /* සාමාන්‍ය විස්තර (ලා අළු පාට) */
    .sub-text {{
        color: #B3B3B3;
        font-size: 18px;
    }}
    
    /* Premium Look බටන් එකක් */
    .stButton>button {{
        background-color: transparent;
        color: #00E5FF;
        border: 2px solid #00E5FF;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #00E5FF;
        color: #121212;
        box-shadow: 0 0 15px #00E5FF;
    }}
    </style>
    """, unsafe_allow_index=True)

# 2. UI Layout එක නිර්මාණය කිරීම
st.markdown('<p class="neon-title">KAIRON</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">නිල වෙබ්අඩවිය — Next-Gen E-Commerce Platform</p>', unsafe_allow_html=True)

st.write("---") # රේඛාවක්

# නිෂ්පාදන පෙන්වීමට Columns (තීරු) 3ක් සෑදීම
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1542291026-7eec264c27ff", caption="Premium Sneakers") # Sample Image
    st.markdown("<h3 style='color: #FFFFFF;'>Pro Sneakers</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00E5FF; font-weight: bold;'>රු. 15,000</p>", unsafe_allow_html=True)
    if st.button("Buy Now", key="btn1"):
        st.success("Added to cart!")

with col2:
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e", caption="Wireless Headphones")
    st.markdown("<h3 style='color: #FFFFFF;'>Cyber Audio V2</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00E5FF; font-weight: bold;'>රු. 22,500</p>", unsafe_allow_html=True)
    if st.button("Buy Now", key="btn2"):
        st.success("Added to cart!")

with col3:
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30", caption="Smart Watch")
    st.markdown("<h3 style='color: #FFFFFF;'>Kairon Watch X</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00E5FF; font-weight: bold;'>රු. 18,900</p>", unsafe_allow_html=True)
    if st.button("Buy Now", key="btn3"):
        st.success("Added to cart!")