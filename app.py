import streamlit as st
from utils.style import apply_custom_style

st.set_page_config(page_title="Moements Woodworking", layout="wide")
apply_custom_style()

st.title("🌲 Moements")
st.subheader("Handcrafted Quality. Timeless Design.")

col1, col2 = st.columns([1, 1])

with col1:
    st.image("https://images.unsplash.com/photo-1581447100595-3771b994fa3a?q=80&w=1000", caption="Craftsmanship in every grain.")
    st.write("""
    ### Our Story
    At Moements, we believe every piece of wood has a story. Whether it's a 
    live-edge dining table or a custom-engraved cutting board, we bring 
    industrial engineering precision to artisanal woodworking.
    """)

with col2:
    st.info("✨ **Ready to start?** Use the sidebar to generate a custom quote or view our gallery.")
    st.write("---")
    st.write("**Services Provided:**")
    st.write("- Custom Dining & Coffee Tables")
    st.write("- Floating Shelves & Cabinetry")
    st.write("- Professional Finishing & Restoration")