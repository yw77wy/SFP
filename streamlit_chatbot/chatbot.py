import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import google.generativeai as genai

# --- Gemini API Setup ---
GOOGLE_API_KEY = "AIzaSyD1m3uw6ZIqHXfmiB0POCc5_FfHJArOcZI"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# --- App Config ---
st.set_page_config(page_title="Draw & Guess Game", layout="wide")
st.title("🎨🧠 Multiplayer Draw & Guess Game")

# --- Session State Initialization ---
if "players" not in st.session_state:
    st.session_state.players = {}

if "messages" not in st.session_state:
    st.session_state.messages = []

if "scoreboard" not in st.session_state:
    st.session_state.scoreboard = {}

if "drawer" not in st.session_state:
    st.session_state.drawer = None

if "current_word" not in st.session_state:
    st.session_state.current_word = ""

# --- Gemini Random Animal ---
def get_random_animal():
    response = model.generate_content("Give me one random animal. Just the name only.")
    return response.text.strip().lower()

# --- Sidebar Player Login ---
with st.sidebar:
    st.header("🧑 Join the Game")
    username = st.text_input("Enter your name:")
    if st.button("Join"):
        if username:
            st.session_state.players[username] = True
            if username not in st.session_state.scoreboard:
                st.session_state.scoreboard[username] = 0
            st.success(f"✅ Welcome, {username}!")
        else:
            st.warning("Please enter a name.")

    if len(st.session_state.players) > 0:
        drawer_selected = st.selectbox("🎯 Select Drawer", list(st.session_state.players.keys()))
        st.session_state.drawer = drawer_selected

    if st.button("🔁 New Random Animal"):
        st.session_state.current_word = get_random_animal()
        st.success(f"🆕 New word generated!")

# --- Drawing Area (Drawer Only) ---
if username == st.session_state.drawer:
    st.subheader("🎨 Drawing Canvas")
    st.markdown("### Your Word: ")
    if not st.session_state.current_word:
        st.session_state.current_word = get_random_animal()
    st.info(f"✏️ Draw this: **{st.session_state.current_word.upper()}**")

    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",
        stroke_width=6,
        stroke_color="#000000",
        background_color="#ffffff",
        height=300,
        width=300,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("🧼 Clear Canvas"):
        st.rerun()

# --- Guessing Section ---
st.subheader("💬 Make a Guess")
if username and username != st.session_state.drawer:
    guess = st.text_input("Your guess:")
    if st.button("Submit Guess"):
        st.session_state.messages.append((username, guess))
        correct = guess.strip().lower() == st.session_state.current_word
        if correct:
            st.session_state.scoreboard[username] += 1
            st.success(f"🎉 {username} guessed it right!")
        else:
            st.info(f"❌ Incorrect guess.")

# --- Chat Log ---
st.write("### 📜 Recent Guesses")
for name, msg in st.session_state.messages[-10:]:
    st.write(f"**{name}**: {msg}")

# --- Scoreboard ---
st.write("### 🏆 Scoreboard")
sorted_scores = sorted(st.session_state.scoreboard.items(), key=lambda x: x[1], reverse=True)
for player, score in sorted_scores:
    st.write(f"{player}: {score} points")





