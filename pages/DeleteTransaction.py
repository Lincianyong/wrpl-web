import streamlit as st

# Sample transaction data
transactions = [
    {'transactionID': 'T001', 'transactionDate': '2024-03-20',
        'transactionStatus': 'Completed', 'transactionPrice': 8500000, 'customerID': 'C001'},
    {'transactionID': 'T002', 'transactionDate': '2024-03-20',
        'transactionStatus': 'Pending', 'transactionPrice': 15000000, 'customerID': 'C002'},
    {'transactionID': 'T003', 'transactionDate': '2024-03-21',
        'transactionStatus': 'Completed', 'transactionPrice': 7200000, 'customerID': 'C003'},
    {'transactionID': 'T004', 'transactionDate': '2024-03-21',
        'transactionStatus': 'Pending', 'transactionPrice': 1500000, 'customerID': 'C004'},
    {'transactionID': 'T005', 'transactionDate': '2024-03-22',
        'transactionStatus': 'Completed', 'transactionPrice': 6000000, 'customerID': 'C005'}
]

# Page title
st.title('Delete Transaction')

# Transaction ID input
transaction_id = st.text_input("Transaction ID")

# Delete button
if st.button("Delete"):
    # Check if transaction ID exists
    transaction_index = None
    for index, transaction in enumerate(transactions):
        if transaction['transactionID'] == transaction_id:
            transaction_index = index
            break

    if transaction_index is not None:
        # Remove transaction from list
        deleted_transaction = transactions.pop(transaction_index)
        st.success(f"Transaction {transaction_id} deleted successfully!")
        st.write("Deleted Transaction:", deleted_transaction)
    else:
        st.error("Transaction ID not found. Please enter a valid ID.")
