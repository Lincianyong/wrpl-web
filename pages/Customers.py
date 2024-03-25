import streamlit as st
import pandas as pd


def main():
    # Load transaction data
    transaction_data = {
        "transactionDate": ["2024-03-20", "2024-03-20", "2024-03-21", "2024-03-21", "2024-03-22", "2024-03-22",
                            "2024-03-23", "2024-03-23", "2024-03-24", "2024-03-24", "2024-03-25", "2024-03-25",
                            "2024-03-26", "2024-03-26", "2024-03-27"],
        "transactionStatus": ["Completed", "Pending", "Completed", "Pending", "Completed", "Completed",
                              "Pending", "Completed", "Pending", "Completed", "Pending", "Completed",
                              "Pending", "Completed", "Pending"],
        "transactionPrice": [8500000, 15000000, 7200000, 1500000, 6000000, 12500000, 3000000, 800000, 10000000,
                             9500000, 12000000, 3800000, 9000000, 2200000, 1200000],
        "customerID": ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010",
                       "C011", "C012", "C013", "C014", "C015"],
        "shippingID": ["S001", "S002", "S003", "S004", "S005", "S001", "S002", "S003", "S004", "S005",
                       "S001", "S002", "S003", "S004", "S005"]
    }
    df_transactions = pd.DataFrame(transaction_data)

    # Customer details
    customer_name = "John Doe"
    customer_address = "123 Main Street"

    # Display customer page
    st.title("Customer Page")

    # Circular image
    st.image(f"https://picsum.photos/150?random=1",
             use_column_width=True, output_format="JPEG", width=100)  # Adjust width here
    st.markdown(
        f"<h2 style='font-size: 2rem;'>{customer_name}</h2>", unsafe_allow_html=True)
    st.write(customer_address)

    # Add space between customer profile and purchased items
    st.empty()

    st.write("### Purchased Items")
    for index, transaction in df_transactions.iterrows():
        if transaction['customerID'] == 'C001':
            product_name = "Smart TV 55"
            st.write(f"**Product Name:** {product_name}\n"
                     f"**Transaction Date:** {transaction['transactionDate']}\n"
                     f"**Transaction Status:** {transaction['transactionStatus']}\n"
                     f"**Transaction Price:** ${transaction['transactionPrice']/100:.2f}\n"
                     f"**Shipping ID:** {transaction['shippingID']}\n")


if __name__ == "__main__":
    main()
