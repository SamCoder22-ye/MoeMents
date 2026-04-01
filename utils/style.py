import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Main background and text */
        .stApp {
            background-color: #F5F5DC; /* Beige */
            color: #4B3621; /* Deep Wood Brown */
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #5D4037 !important;
            font-family: 'Georgia', serif;
        }

        /* Buttons */
        .stButton>button {
            background-color: #8B4513;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 24px;
        }
        
        .stButton>button:hover {
            background-color: #A0522D;
            color: white;
            border: 1px solid white;
        }

        /* Input fields */
        .stTextInput>div>div>input, .stSelectbox>div>div>select {
            background-color: #FFFFFF;
            border: 1px solid #D2B48C;
        }

        /* Cards for Gallery/Quotes */
        .css-1r6slb0 {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_list=True)