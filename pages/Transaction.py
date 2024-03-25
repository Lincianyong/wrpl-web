import streamlit as st


def main():
    st.title("Transaction Page")

    # Sample product data
    products = [
        {"name": "Smart TV 55", "price": 8500000,
            "image": "https://picsum.photos/150?random=1"},
        {"name": "Laptop - Core i7", "price": 15000000,
            "image": "https://picsum.photos/150?random=2"},
        {"name": "Smartphone - X10", "price": 7200000,
            "image": "https://picsum.photos/150?random=3"}
    ]

    # Sample shipping options
    shipping_options = {
        "FastShip": 8000,
        "SwiftDelivery": 7000,
        "QuickShip": 6000,
        "RapidTransit": 5500,
        "ExpressShip": 6500
    }

    # Cart list
    st.header("Cart")

    for idx, product in enumerate(products):
        col1, col2, col3 = st.columns([1, 2, 1])
        amount = col3.number_input(
            label="", min_value=0, step=1, key=f"amount_{idx}")
        col1.image(product['image'], width=150)
        col2.write(f"**Product Name:** {product['name']}\n"
                   f"**Price:** Rp {product['price']}\n")
        col3.write(f"**Amount:** {amount}")

    # Calculate subtotal
    total_price = sum(
        product['price'] * st.session_state[f"amount_{idx}"] for idx, product in enumerate(products))

    st.write(f"**Subtotal:** Rp {total_price}")

    # Shipping option
    st.header("Shipping")
    selected_shipping = st.selectbox(
        "Select Shipping Option", list(shipping_options.keys()))
    shipping_fee = shipping_options[selected_shipping]
    st.write(f"**Selected Shipping:** {selected_shipping}")
    st.write(f"**Shipping Fee:** Rp {shipping_fee}")

    # Total purchase
    total_purchase = total_price + shipping_fee
    st.write(f"**Total Purchase:** Rp {total_purchase}")

    # Checkout button
    if st.button("Checkout"):
        payment_option = st.radio("Select Payment Option", [
                                  "Credit Card", "Bank Transfer", "E-Wallet"])
        st.write(f"Selected Payment Option: {payment_option}")


if __name__ == "__main__":
    main()
