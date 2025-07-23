import streamlit as st
import pandas as pd
import random

st.title("🎯 Number Guessing Game")
st.header("Welcome to the game")
st.write("This is a simple game where you try to guess a number between 1 and 100.")

# Set up session state to remember values across interactions
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False

# User input
guess = st.number_input("Guess a number between 1 and 100", min_value=1, max_value=100, step=1)

# Check guess
if st.button("Submit"):
    if not st.session_state.finished:
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"🎉 Correct! The number was {st.session_state.number}.")
            st.info(f"You guessed it in {st.session_state.attempts} attempts.")
            st.session_state.finished = True

# Restart the game
if st.session_state.finished:
    if st.button("Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.finished = False

