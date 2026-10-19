import streamlit as st
import streamlit.components.v1 as components

# Page title matching your assignment sheet
st.title("Question 1: GND Rail Setup")
st.write("Live simulation of the Breadboard, LED & Resistor Wiring.")


wokwi_url = "https://github.com/maicaedangalino/maicaedangalino/blob/473ecde9b5fdec2462e226369c059c7bc57f8e58/week1_q1/diagram.json."

# Embed the Wokwi project
components.iframe(wokwi_url, height=600, scrolling=True)
