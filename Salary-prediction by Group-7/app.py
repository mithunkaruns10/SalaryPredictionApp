from tkinter import HORIZONTAL
import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from home_page import show_home_page
from streamlit_option_menu import option_menu

# 1. Side-menu
# page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))


# 2. Horizontal menu
selected_option = option_menu(
    menu_title=None,
    options=["Home", "Predict", "Explore"],
    icons=["house", "search", "clipboard-data"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "20px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
        "nav-link-selected": {"background-color": "black"},
    },
)

# Link the pages
if selected_option == "Home":
    show_home_page()
if selected_option == "Predict":
    show_predict_page()
if selected_option == "Explore":
    show_explore_page()
