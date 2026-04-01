import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Main background - Darkened Beige for better contrast */
        .stApp {
            background-color: #D2B48C; /* Tan/Dark Beige */
            color: #2E1A08; /* Darker Wood Brown */
        }
        
        /* Typography - Bigger Fonts */
        html, body, [class*="css"] {
            font-size: 110%; 
        }

        h1 { font-size: 3.5rem !important; color: #4B3621 !important; font-family: 'Georgia', serif; }
        h2 { font-size: 2.5rem !important; color: #4B3621 !important; }
        h3 { font-size: 1.8rem !important; color: #FFFFFF !important; } /* White headers for contrast */

        /* Buttons */
        .stButton>button {
            background-color: #5D4037;
            color: white;
            font-size: 1.2rem;
            border-radius: 8px;
            padding: 12px 30px;
        }
        
        /* Cards */
        .stAlert, .css-1r6slb0, div[data-testid="stVerticalBlock"] > div:has(div.stImage) {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #8B4513;
        }
        </style>
    """, unsafe_allow_html=True)