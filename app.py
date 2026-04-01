import streamlit as st
from utils.style import apply_custom_style

st.set_page_config(page_title="Moements Woodworking", layout="wide")
apply_custom_style()

# --- HEADER SECTION ---
st.title("🌲 Moements")
st.subheader("Family Built. Locally Crafted.")

# --- THE "LEARN MORE" RICKROLL BUTTON ---
# We use a columns layout to center the big button
col_left, col_mid, col_right = st.columns([1, 2, 1])
with col_mid:
    st.markdown("""
        <style>
        .big-button {
            display: inline-block;
            padding: 15px 30px;
            font-size: 24px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #fff;
            background-color: #8B4513;
            border: none;
            border-radius: 15px;
            width: 100%;
            font-family: 'Georgia', serif;
        }
        .big-button:hover {background-color: #A0522D}
        </style>
        <a href="https://www.youtube.com/watch?v=oHg5SJYRHA0" target="_blank">
            <button class="big-button">
                ✨ LEARN MORE ABOUT OUR PROCESS
            </button>
        </a>
    """, unsafe_allow_html=True)

st.write("---")

# --- MAIN CONTENT ---
col1, col2 = st.columns([1, 1])

with col1:
    # This assumes the image is in your GitHub root folder
    st.image("IMG_2929.jpg", caption="Hand-selected slabs from Pelican Rapids, MN.")
    st.write("""
    ### Meet the Maker
    **Jon Moe** is a passionate STEM middle school teacher who brings the classroom's curiosity to the workshop. Located in the heart of **Pelican Rapids, MN**, Jon specializes in creating premium, heirloom-quality wood products. 
    
    Every piece at Moements is **Family Built**, ensuring that the heart of our home ends up in yours.
    """)

with col2:
    st.success("### Premium Woodwork & Education")
    st.write("""
    - **Custom Furniture:** Built to your exact specs.
    - **STEM Inspired:** Precision meets natural beauty.
    - **Build It Yourself:** We don't just build for you; we can build *with* you.
    """)
    st.write("---")
    st.info("📍 **Location:** Pelican Rapids, MN")
    st.write("📞 **Contact:** 701-866-2277")
    st.write("✉️ **Email:** jmoe72@yahoo.com")