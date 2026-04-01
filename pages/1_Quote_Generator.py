import streamlit as st
from utils.style import apply_custom_style
from utils.logic import calculate_price, save_order

apply_custom_style()

st.title("Project Quote Generator")

with st.form("quote_form"):
    col1, col2 = st.columns(2)
    with col1:
        p_type = st.selectbox("Product Type", ["Table", "Shelf", "Cutting Board", "Furniture"])
        wood = st.selectbox("Wood Choice", ["Pine", "Maple", "Oak", "Walnut", "Reclaimed/Live Edge"])
    
    with col2:
        l = st.number_input("Length (inches)", min_value=1.0, value=12.0)
        w = st.number_input("Width (inches)", min_value=1.0, value=12.0)
        h = st.number_input("Thickness/Height (inches)", min_value=0.5, value=1.5)

    submitted = st.form_submit_button("Calculate Estimate")

if submitted:
    price = calculate_price(p_type, l, w, h, wood)
    st.success(f"### Estimated Price: ${price}")
    
    st.write("---")
    st.subheader("Ready to place this order?")
    with st.expander("Contact Information"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        notes = st.text_area("Custom Requests/Notes")
        
        if st.button("Submit Order Request"):
            if name and email:
                save_order({"Name": name, "Email": email, "Product": p_type, "Wood": wood, "Price": price, "Notes": notes})
                st.balloons()
                st.success("Order sent! We will contact you soon.")
            else:
                st.error("Please provide a name and email.")