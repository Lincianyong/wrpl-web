import streamlit as st


def main():
    st.title("Sign Up / Sign In")

    # Sign up / Sign in option
    sign_up = st.checkbox("Sign Up")
    sign_in = st.checkbox("Sign In")

    if sign_up:
        st.header("Sign Up")
        # Input fields
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone_number = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        recheck_password = st.text_input("Re-enter Password", type="password")

        # Sign up button
        if st.button("Sign Up"):
            if name and email and phone_number and password and recheck_password:
                if password == recheck_password:
                    # Process sign up
                    st.success("Sign up successful!")
                    st.write(f"Name: {name}")
                    st.write(f"Email: {email}")
                    st.write(f"Phone Number: {phone_number}")
                    # You can add code here to store user information in a database
                else:
                    st.warning("Passwords do not match.")
            else:
                st.warning("Please fill in all the fields.")

    if sign_in:
        st.header("Sign In")
        # Input fields
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # Sign in button
        if st.button("Sign In"):
            if email and password:
                # You can add code here to check user credentials from a database
                st.success("Sign in successful!")
                st.write(f"Email: {email}")
            else:
                st.warning("Please fill in all the fields.")


if __name__ == "__main__":
    main()
