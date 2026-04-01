import streamlit as st
import time
from utils.style import apply_custom_style

st.set_page_config(page_title="Moements Woodworking", layout="wide")
apply_custom_style()

# --- HEADER SECTION ---
st.title("🌲 Moements")
st.subheader("Family Built. Locally Crafted.")

# --- APRIL FOOLS RICKROLL LOGIC ---
col_left, col_mid, col_right = st.columns([1, 2, 1])

with col_mid:
    # Use a Streamlit button to trigger the prank
    if st.button("✨ LEARN MORE ABOUT OUR PROCESS", use_container_width=True):
        # 1. Show the prank message
        st.error("## 🤡 APRIL FOOLS! YOU'VE BEEN RICKROLLED!")
        st.balloons()
        
        # 2. Wait for 2 seconds
        time.sleep(2)
        
        # 3. Show the link to the video
        st.markdown(f"""
            <div style="text-align: center; padding: 20px; border: 2px dashed #8B4513; border-radius: 10px;">
                <h3>Gotcha! Click below for your prize:</h3>
                <a href="https://www.youtube.com/watch?v=oHg5SJYRHA0" target="_blank" style="font-size: 20px; color: #FFFFFF; background-color: #8B4513; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    Watch Secret Process Video 🎥
                </a>
            </div>
        """, unsafe_allow_html=True)

st.write("---")

# --- MAIN CONTENT ---
col1, col2 = st.columns([1, 1])

with col1:
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