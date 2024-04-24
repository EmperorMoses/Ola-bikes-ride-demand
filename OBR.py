import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open("model.pkl", 'rb'))

st.title('OLA BIKE RIDE DEMAND')
st.sidebar.header('MODEL FEATURE SELECTION')
bike_image = Image.open("C:\\Users\\USER\\OneDrive\\Documents\\MY DATA SCIENCE DOCS\\PROJECT\\s1-pro6405e906c37fe.webp")
st.image(bike_image)
bike_image2 = Image.open("C:\\Users\\USER\\OneDrive\\Documents\\MY DATA SCIENCE DOCS\\PROJECT\\pexels-sofianunezph-19684606.jpg")
st.sidebar.image(bike_image2)

def user_report():
    instant = st.sidebar.number_input('Ride Instant', 0,750)
    season = st.sidebar.selectbox('Seasons', ['Spring', 'Summer', 'Fall', 'Winter'])
    if (season=='Spring'):
        Seasons = 1
    elif(season=='Summer'):
        Seasons = 2
    elif(season=='Fall'):
        Seasons = 3
    else:
        Seasons = 4
    year = st.sidebar.radio("Select Year", [2011, 2012])
    month = st.sidebar.selectbox('Month', [1,2,3,4,5,6,7,8,9,10,11,12])
    holidays = st.sidebar.radio('Holidays', ('No', 'Yes'))
    if (holidays == 'Yes'):
        Holidays = 0
    else:
        Holidays = 1
    weekday = st.sidebar.selectbox('Weekdays', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sumday'])
    if (weekday=='Monday'):
        Weekdays = 0
    elif (weekday=='Yuesday'):
        Weekday = 1
    elif (weekday=='Wednessday'):
        Weekdaya = 2
    elif (weekday=='Thursdat'):
        Weekdays = 3
    elif (weekday=='Friday'):
        Weekdays = 4
    elif (weekday=='Saturady'):
        Weekdays = 5
    else:
        Weekdays = 6
    workingday = st.sidebar.radio('Workingday', ('No', 'Yes'))
    if (workingday == 'Yes'):
        Workingday = 0
    else:
        Workingday = 1
    weather = st.sidebar.selectbox('Weather', ['Clear', 'Mist', 'Light', 'Heavy rain'])
    if (weather == 'Clear'):
        Weather = 1
    elif (weather == 'Mist'):
        Weather = 2
    elif (weather == 'Light'):
        Weather = 3
    else:
        Weathers = 4
    temp = st.sidebar.slider('Temperature', 0.000,1.00)
    atemp = st.sidebar.slider('AveTemperature', 0.000,1.00)
    humidity = st.sidebar.slider('Humidity', 0.000,1.00)
    windspeed = st.sidebar.slider('Windspeed', 0.000,1.00)
    casual = st.sidebar.number_input('Casual', 1,4500)
    registered = st.sidebar.number_input('Registered', 10,7500)
    day = st.sidebar.number_input('Date', min_value=1, max_value=31)

    user_report_data = {
        "instant": instant,
        "season": Seasons,
        "year": year,
        "month": month,
        "holidays": Holidays,
        "weekday": Weekdays,
        "workingday": Workingday,
        "weather": Weather,
        'temp': temp,
        'atemp': atemp,
        'humidity': humidity,
        'windspeed': windspeed,
        'casual': casual,
        'registered': registered,
        'day': day
    }
    report_data = pd.DataFrame(user_report_data, index = [0])
    return report_data

user_data = user_report()
st.subheader('Ola Bike ride')
st.write(user_data)

count = model.predict(user_data)
st.subheader('Number of bikes demanded')
st.markdown(f"<p style='color:red; font-weight:bold; font-size:25px;'>{np.round(count[0], 1)} bikes</p>", unsafe_allow_html=True)

if st.sidebar.button("Show Samples of OLa Bikes"):
    image_paths = ["C:\\Users\\USER\\OneDrive\\Documents\\MY DATA SCIENCE DOCS\\PROJECT\\s1-air64d5dd80d0382.webp", "C:\\Users\\USER\\OneDrive\\Documents\\MY DATA SCIENCE DOCS\\PROJECT\\s1-air64d5dd8377a1b.webp"]
    for path in image_paths:
        st.sidebar.image(path, caption='Samples of Olabikes', use_column_width=True)
