import streamlit as st
from utils.style import apply_custom_style

apply_custom_style()

st.title("Project Gallery")

# Replace these filenames with your actual uploaded image names in GitHub
images = [
    {"file": "IMG_0337.jpg", "caption": "Sanding down premium slabs."},
    {"file": "IMG_0364.jpg", "caption": "Finished Dark Walnut Table."},
    {"file": "IMG_2069.jpg", "caption": "Custom Shotgun Display Rack."},
    {"file": "IMG_2929.jpg", "caption": "Live Edge Maple Preparation."}
]

cols = st.columns(2)
for i, img in enumerate(images):
    with cols[i % 2]:
        # If running locally, make sure images are in the same folder
        try:
            st.image(img["file"], caption=img["caption"], use_container_width=True)
        except:
            st.warning(f"Image {img['file']} not found. Please upload to GitHub.")