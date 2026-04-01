import streamlit as st
import pandas as pd
import os

st.title("Admin Order Management")

password = st.text_input("Enter Admin Password", type="password")

if password: # Only check if the user has typed something
    if password == "moements2026": 
        if os.path.exists('orders.csv'):
            df = pd.read_csv('orders.csv')
            st.write("### Current Order Requests")
            st.dataframe(df)
            
            if st.button("Clear All Orders"):
                os.remove('orders.csv')
                st.rerun() # Updated from experimental_rerun
        else:
            st.info("No orders found yet.")
    else:
        st.error("Incorrect Password.")
else:
    st.info("Please enter the password to view orders.")