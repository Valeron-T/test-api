import streamlit as st
import requests

with st.form("my_form"):
    st.write("Checkout")
    st.write("Please enter card details to proceed.")

    name = st.text_input('Card Holder\'s Name')

    card_number = st.text_input('Card Number', max_chars=15)

    col1, col2 = st.columns(2)

    # Add inputs to the first column
    with col1:
        cvv = st.text_input('CVV', max_chars=3)

    # Add inputs to the second column
    with col2:
        exp = st.text_input('Date (MM/YY)', max_chars=5)

    col1, col2 = st.columns(2)


    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        print(card_number, name, cvv, exp)
        response = requests.post("https://test-api-lemon-one.vercel.app/checkout", {
            "name": name,
            "number": card_number,
            "exp": exp,
            "cvv": cvv
        })
        st.write("Response")
        st.write(response.json())