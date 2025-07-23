import streamlit as st

st.title("🔤 String Formatter Tool")

# Input from user
user_input = st.text_input("Enter your text:")

# Choose formatting option
format_option = st.selectbox("Choose a formatting option", [
    "UPPERCASE",
    "lowercase",
    "Capitalize First Letter",
    "Remove Spaces"
])

# Button to process
if st.button("Format Text"):
    if format_option == "UPPERCASE":
        st.write("🔹 Result:", user_input.upper())
    elif format_option == "lowercase":
        st.write("🔹 Result:", user_input.lower())
    elif format_option == "Capitalize First Letter":
        st.write("🔹 Result:", user_input.capitalize())
    elif format_option == "Remove Spaces":
        st.write("🔹 Result:", user_input.replace(" ", ""))
