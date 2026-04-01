import streamlit as st
import pandas as pd
import os

st.title("Admin Order Management")

password = st.text_input("Enter Admin Password", type="password")

if password == "moements2026": # You can change this
    if os.path.exists('orders.csv'):
        df = pd.read_csv('orders.csv')
        st.write("### Current Order Requests")
        st.dataframe(df)
        
        if st.button("Clear All Orders"):
            os.remove('orders.csv')
            st.experimental_rerun()
    else:
        st.info("No orders found yet.")
else:
    st.error("Access Denied.")