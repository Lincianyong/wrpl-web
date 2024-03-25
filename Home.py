import streamlit as st

def main():
    st.title("Online Electronics")
    st.subheader("Welcome to our online store!")

    products = {
        "Smart TV 55\"": {"price": 8500000, "stock": 25},
        "Laptop - Core i7": {"price": 15000000, "stock": 15},
        "Smartphone - X10": {"price": 7200000, "stock": 30},
        "Wireless Headphones": {"price": 1500000, "stock": 50},
        "Gaming Console": {"price": 6000000, "stock": 20},
        "Drone - Pro": {"price": 12500000, "stock": 10},
        "Smart Watch": {"price": 3000000, "stock": 40},
        "Bluetooth Speaker": {"price": 800000, "stock": 60},
        "DSLR Camera": {"price": 10000000, "stock": 12},
        "Tablet - iPad Air": {"price": 9500000, "stock": 18},
        "Desktop PC": {"price": 12000000, "stock": 8},
        "VR Headset": {"price": 3800000, "stock": 25},
        "Home Theater System": {"price": 9000000, "stock": 14},
        "Action Camera": {"price": 2200000, "stock": 35},
        "Wireless Router": {"price": 1200000, "stock": 45},
        "Smart Thermostat": {"price": 1700000, "stock": 55},
        "E-book Reader": {"price": 900000, "stock": 70},
        "Portable Projector": {"price": 4500000, "stock": 20},
        "Fitness Tracker": {"price": 750000, "stock": 50},
        "Wireless Earbuds": {"price": 1200000, "stock": 65}
    }

    st.write("## Products")
    col1, col2, col3 = st.columns(3)

    for i, (product, info) in enumerate(products.items()):
        col = col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3
        with col:
            st.image(f"https://picsum.photos/150?random={i}", use_column_width=True)
            st.markdown(f"#### {product}")
            st.write(f"Price: ${info['price']/100:.2f}")
            st.write(f"Stock: {info['stock']}")

if __name__ == "__main__":
    main()