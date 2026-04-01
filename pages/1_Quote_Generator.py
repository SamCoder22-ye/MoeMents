import streamlit as st
from utils.style import apply_custom_style
from utils.logic import calculate_price, save_order

apply_custom_style()

st.title("Start Your Project")

tab1, tab2 = st.tabs(["Get a Quote", "Inquire: Build It Yourself"])

with tab1:
    with st.form("quote_form"):
        col1, col2 = st.columns(2)
        with col1:
            p_type = st.selectbox("Product Type", ["Table", "Shelf", "Cutting Board", "Furniture"])
            wood = st.selectbox("Wood Choice", ["Pine", "Maple", "Oak", "Walnut", "Reclaimed/Live Edge"])
        with col2:
            l = st.number_input("Length (in)", min_value=1.0, value=12.0)
            w = st.number_input("Width (in)", min_value=1.0, value=12.0)
            h = st.number_input("Height (in)", min_value=0.5, value=1.5)
        
        submitted = st.form_submit_button("Calculate Estimate")

    if submitted:
        price = calculate_price(p_type, l, w, h, wood)
        st.write(f"## Estimated Price: ${price}")
        st.write("---")
        st.subheader("Contact Jon Moe to Finalize")
        
        contact_method = st.radio("How would you like to reach out?", ["Text/Message Jon", "Email Jon"])
        
        with st.expander("Send Inquiry Details"):
            u_name = st.text_input("Your Name")
            u_contact = st.text_input("Your Email or Phone")
            if st.button("Generate Contact Link"):
                if contact_method == "Text/Message Jon":
                    st.write(f"👉 [Click here to Text Jon](sms:+17018662277?&body=Hi Jon, I am interested in a {wood} {p_type} quoted at ${price}.)")
                else:
                    st.write(f"👉 [Click here to Email Jon](mailto:jmoe72@yahoo.com?subject=Woodworking Inquiry&body=Hi Jon, I am interested in a {wood} {p_type}.)")
                save_order({"Name": u_name, "Contact": u_contact, "Type": "Quote", "Details": f"{wood} {p_type}"})

with tab2:
    st.header("Build It Yourself (BIY) Program")
    st.write("Want to learn the trade? Join Jon in the shop to build your own custom piece.")
    if st.button("Inquire about BIY Workshop"):
        st.write("Reach Jon at **701-866-2277** or **jmoe72@yahoo.com** to discuss your project!")