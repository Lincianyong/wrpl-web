import streamlit as st
import time
import numpy as np
import pandas as pd

from wirpl_books.models.transaction import TransactionModel

st.set_page_config(page_title="Transactions", page_icon="📈")

st.markdown("# Transactions")
st.sidebar.header("Transactions")
st.write(
    """Manage Transactions"""
)

customer_model = TransactionModel()

with st.container():
    st.write("## Select Transactions")
    df = pd.DataFrame(customer_model.get_all(), columns=customer_model.COLUMN_NAMES)
    st.write(df)

    if st.button("Refresh"):
        st.rerun()

with st.container():
    st.write("## Add Transaction")
    id = st.slider("ID", min_value=0, max_value=1000, step=1)
    total_price = st.text_input("Total Price")
    payment_method = st.text_input("Payment Method")
    created_at = st.text_input("Created At")
    status = st.text_input("Status")
    customer_id = st.number_input("Customer ID", min_value=0, max_value=1000, step=1)

    if st.button("Add"):
        customer_model.insert(id, total_price, payment_method, created_at, status, customer_id)
        st.success("Transaction added")