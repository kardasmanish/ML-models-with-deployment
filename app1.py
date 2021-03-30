import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
import base64

pickle_in = open("solar_pred.pkl","rb")
classifier = pickle.load(pickle_in)

main_bg = "rad1.jpg"
main_bg_ext = "jpg"


def welcome():
    return "welcome All"

def solar_predictor(Temperature,Pressure,Humidity,WindDirection,Speed):
    prediction = classifier.predict([[Temperature,Pressure,Humidity,WindDirection,Speed]])
    print(f"The predicted value is {round(prediction[0],2)} watt")
    return round(prediction[0],2)
def main():
    st.title("Hello All!")
    st.text("This is an webapp created using streamlit featuring an ML model hosted on Heroku")
    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
    html_temp = """
    <body background='radiation.png'>
    <div style = "background-color:DarkOrange;padding:10px">
    <h2 style = "color:white;text-align:center;"> Solar Radiaton Prediction AI App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html= True)
    Temperature = st.text_input("Temperature (Celcius)","Type here")
    Pressure = st.text_input("Pressure (Pa)","Type here")
    Humidity = st.text_input("Humidity (g/m3)","Type here")
    WindDirection = st.text_input("WindDirection in Degrees ","Type here")
    Speed = st.text_input("Speed (km/hr)","Type here")
    result = ""
    if st.button("Predict"):
        result = solar_predictor(Temperature,Pressure,Humidity,WindDirection,Speed)
    st.success("The predicted radiation value is {} watt".format(result))

if __name__ == "__main__":
    main()

