import streamlit as st
import pickle 
import numpy as np
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

# st.markdown("<b>Calories Burned Calculator App</b>", unsafe_allow_html=True)
st.markdown("<h2><b>Calories Burned Calculator App</b></h2>", unsafe_allow_html=True)

gender = st.selectbox("Select Gender", ("Male", "Female"))

if (gender == "Male"):
    g = 0
else:
    g = 1

# Receiving Age from the User
age = st.number_input("Enter Age: ")

# Receiving Height from the User
height = st.number_input("Enter Height (in cm): ")

# Receiving Weight from the User
weight = st.number_input("Enter Weight (in kg): ")

# Receiving Time Duration 
duration = st.number_input("Enter Workout Duration (in mins): ")

# Receiving Heart Rate from the User
heart_rate = st.number_input("Enter Heart Rate: ")

# Receiving Body Temperature from the User
bodytemp = st.number_input("Enter Body Temperature (in Celcius): ")

# Making out the Prediction
prediction = model.predict(pd.DataFrame(
    columns = ("Gender", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"),
    data = np.array([[g, age, height, weight, duration, heart_rate, bodytemp]]).reshape(1, 7)
    ))

if st.button("Predict"):
    st.write(f"Calories Burned: {float(prediction)} cal")
    # st.write(prediction)
else:
    st.write("Click the button to predict calories burned.")