import streamlit as st
from utils.style import apply_custom_style

apply_custom_style()

st.title("Build It Yourself: The 'Weekend Warrior' Project")

st.write("""
### Why BIY?
As a STEM teacher, Jon loves to share the science behind the wood. From understanding moisture content to the physics of joinery, our BIY program is about more than just a table—it's a lesson.
""")

col1, col2 = st.columns(2)

with col1:
    st.header("The Birdhouse Project")
    st.write("A perfect starter project for families!")
    st.write("- **Skills Learned:** Measuring, basic drilling, assembly.")
    st.write("- **Time:** 2 Hours.")
    st.write("- **Price:** $45 (Includes all materials).")

with col2:
    st.image("IMG_2069.jpg", caption="Jon showing the ropes.")

st.write("---")
st.success("Ready to get your hands dirty? Contact Jon today to schedule a shop day!")