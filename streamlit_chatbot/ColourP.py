import streamlit as st

st.title("🎨 Color Picker Tool")

# Color picker input
color = st.color_picker("Pick a color", "#00f900")

# Display the selected color
st.write("🔹 Selected HEX Color:", color)

# Convert HEX to RGB
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

rgb = hex_to_rgb(color)
st.write("🔹 RGB Value:", rgb)

# Show a color box
st.markdown(
    f"<div style='width:100px;height:100px;background-color:{color};border:1px solid #000'></div>",
    unsafe_allow_html=True
)
