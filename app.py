import streamlit as st
from PIL import Image

# Variables for maintance costs. 
# cost is rough estimation of both parts price and installation labor.
oil_change_cost = 0
hpfp_cost = 0
turbos_cost = 0
injectors_cost = 0
water_pump_cost = 0
walnut_blast_cost = 0
oilpan_gasket_cost = 0
valvecover_gasket_cost = 0


st.title('BMW N54 Maintenance Tool')

image = Image.open('./images/flick.jpg')
st.image(image, caption='The German 2JZ',use_column_width=True)
    
st.subheader("Please answer the following:")

car_model = st.selectbox(
        'What model is your vehicle?',
        ('','135i','335i','535i','335is','1M','X6','Z4','740i','Alpina B3','Alpina B3 S','Alpina B3 GT3'))

car_year = st.selectbox(
    "Production Year: ", options=['',"2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016"])

trans_type = st.selectbox(
        'Transmission:',
        ('', 'Automatic', 'Manual'))

drivetrain_type = st.selectbox(
        'xDrive:',
        ('', 'Yes', 'No'))

car_mileage = st.number_input('Mileage:',min_value=0, max_value=500000, step=1)
st.write('Your ' + car_model + ' has a mileage of ', car_mileage)

st.subheader('Service History:')

oil_change = st.radio(
    "Has the oil been serviced within the last 5000 miles?", options=["Yes", "No"])

if oil_change == "Yes":
    oil_change_cost = 0
else:
    oil_change_cost = 100

hpfp_check = st.radio(
    "Has the High Pressure Fuel Pump been serviced?", options=["Yes", "No"])

if hpfp_check == "Yes":
    hpfp_cost = 0
else:
    hpfp_cost = 1000

turbos_check = st.radio(
    "Have both turbochargers been serviced?", options=["Yes", "No"])

if turbos_check == "Yes":
    turbos_cost = 0
else:
    turbos_cost = 2700

injector_check = st.radio(
    "Have all injectors been upgraded to Index 12?", options=["Yes", "No"])

if injector_check == "Yes":
    injectors_cost = 0
else:
    injectors_cost = 3000

water_pump_check = st.radio(
    "Has the water pump and thermostat been serviced?", options=["Yes", "No"])

if water_pump_check == "Yes":
    water_pump_cost = 0
else:
    water_pump_cost = 1100

walnut_blast_check = st.radio(
    "Has a walnut-blast service been preformed?", options=["Yes", "No"])

if walnut_blast_check == "Yes":
    walnut_blast_cost = 0
else:
    walnut_blast_cost = 270

oilpan_gasket_check = st.radio(
    "Have the oil pan and gasket been serviced?", options=["Yes", "No"])

if oilpan_gasket_check == "Yes":
    oilpan_gasket_cost = 0
else:
    oilpan_gasket_cost = 1100

valve_cover_gasket_check = st.radio(
    "Has the valve cover and gasket been serviced?", options=["Yes", "No"])

if valve_cover_gasket_check == "Yes":
    valve_cover_gasket_cost = 0
else:
    valve_cover_gasket_cost = 1100


    
st.subheader('Estimation of Maintenance cost:')
    
st.write(oil_change_cost + hpfp_cost + turbos_cost + injectors_cost + water_pump_cost
         + walnut_blast_cost + oilpan_gasket_cost + valve_cover_gasket_cost)

# syntax for later
#if car_mileage == 0:
#    st.write('')
#elif car_mileage >= 1 and car_mileage < 100000:
#    st.write('car is young af')

    

