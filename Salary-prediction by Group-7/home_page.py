# Import all the needed modules
import streamlit as st


def show_home_page():
    st.header("Software developer salary prediction")
    st.subheader("About")
    st.write("A web application that predicts the average salary in a particular country based on the educational qualifications and year of experience of an individual.")

    st.subheader("Features")
    st.write(""" 
        - Predict Page
            - Predict salary by country
            - Predict salary by educational level
            - Predict salary by year of experience
            """)
    st.write(""" 
        - Explore Page
            - Pie chart for different data collected by different countries
            - Interactive Bar chart for average salary by country
            - Interactive Line chart for average salary by experience
            """)
    st.subheader("Design of machine learning model")
    st.write(""" 
        We implemented following three machine learning models to predict the best salary results.
        - Linear Regression    
        - Decision Tree Regressor
        - Random Forest Regressor
            """)
