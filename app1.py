import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("solar_pred.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "welcome All"

def solar_predictor(Temperature,Pressure,Humidity,WindDirection,Speed):
    prediction = classifier.predict([[Temperature,Pressure,Humidity,WindDirection,Speed]])
    print(f"The predicted value is {round(prediction[0],2)} watt")
    return round(prediction[0],2)
def main():
    st.title("Hello All!")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;"> Solar Radiaton Prediction AI App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html= True)
    Temperature = st.text_input("Temperature","Type here")
    Pressure = st.text_input("Pressure","Type here")
    Humidity = st.text_input("Humidity","Type here")
    WindDirection = st.text_input("WindDirection","Type here")
    Speed = st.text_input("Speed","Type here")
    result = ""
    if st.button("Predict"):
        result = solar_predictor(Temperature,Pressure,Humidity,WindDirection,Speed)
    st.success("The predicted radiation value is {} watt".format(result))

if __name__ == "__main__":
    main()

