import streamlit as st
import pandas as pd
from PIL import Image


st.title('BMW N54 Maintenance Tool')

image = Image.open('./images/flick.jpg')
st.image(image, caption='Maintenance Before Full Sending',use_column_width=True)
    
st.subheader("Please answer the following:")

car_model = st.selectbox(
        'What model is your vehicle?',
        ('','135i','335i', '535i'))

car_year = st.number_input('Production year:')

trans_type = st.selectbox(
        'Transmission:',
        ('', 'Automatic', 'Manual'))

car_mileage = st.number_input('Mileage:')
st.write('Your ' + car_model + ' has a mileage of ', car_mileage)

st.subheader('Service History:')

oil_change = st.radio(
    "Has the oil been serviced within the last 5000 miles?", options=["Yes", "No"])

hpfp_check = st.radio(
    "Has the High Pressure Fuel Pump been serviced?", options=["Yes", "No"])

turbo_check = st.radio(
    "Have both turbochargers been serviced?", options=["Yes", "No"])

injector_check = st.radio(
    "Have all injectors been upgraded to Index 12?", options=["Yes", "No"])

water_pump_check = st.radio(
    "Has the water pump been serviced?", options=["Yes", "No"])

walnut_blast_check = st.radio(
    "Has a walnut-blast service been preformed?", options=["Yes", "No"])

oilpan_gasket_check = st.radio(
    "Have the oil pan and gasket been serviced?", options=["Yes", "No"])

valve_cover_check = st.radio(
    "Has the valve cover and gasket been serviced?", options=["Yes", "No"])


# syntax for later
#if car_mileage == 0:
#    st.write('')
#elif car_mileage >= 1 and car_mileage < 100000:
#    st.write('car is young af')

    

