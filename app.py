import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image

def senior_simplifier(title):
    if title == "Senior":
        return 1
    else:
        return 0
    
def lang_simplifier(title):
    if title == "Yes":
        return 1
    else:
        return 0


df = pd.read_csv('cs_data_cleaned.csv')



st.title('BMW N54 Maintance Check Tool')


image = Image.open('C:/Users/Mario/Desktop/bmw_prototype/covid19_software_salary_app-master/images/flick.jpg')
st.image(image, caption='Maintance Before Full Sending',use_column_width=True)

# Use pickle to load in the pre-trained model
with open(f'model.pkl', 'rb') as f:
    model = pickle.load(f)
    
st.subheader("Maintance")

car_model = st.selectbox(
        'What model is your car?',
        ('135i','335i', '535i'))

st.write('You selected:', car_model)

car_mileage = st.number_input('Mileage')
st.write('Your ' + car_model + ' has a mileage of ', car_mileage)

st.subheader('Job Attributes:')

jobhq_num = st.radio(
    "Would you like the position to be located at the company headquarters ? ", options=["Yes", "No"])

jobhq_yn = lang_simplifier(jobhq_num)


seniority_num = st.radio("Senior role?", options=["Senior", "Not Senior"])
senior_yn = senior_simplifier(seniority_num)


st.subheader('Experience with:')
python_num = st.radio("Python:", options=["Yes", "No"])
java_num = st.radio("Java:", options=["Yes", "No"])
C_plus_plus_num = st.radio("C++:", options=["Yes", "No"])
C_sharp_num = st.radio("C#:", options=["Yes", "No"])
PHP_num = st.radio("PHP:", options=["Yes", "No"])
swift_num = st.radio("Swift:", options=["Yes", "No"])
ruby_num = st.radio("Ruby:", options=["Yes", "No"])
javascript_num = st.radio("Javascript:", options=["Yes", "No"])
SQL_num = st.radio("SQL:", options=["Yes", "No"])


python_yn = lang_simplifier(python_num)
java_yn = lang_simplifier(java_num)
C_plus_plus_yn = lang_simplifier(C_plus_plus_num)
C_sharp_yn = lang_simplifier(C_sharp_num)
PHP_yn = lang_simplifier(PHP_num)
swift_yn = lang_simplifier(swift_num)
ruby_yn = lang_simplifier(ruby_num)
javascript_yn = lang_simplifier(javascript_num)
SQL_yn = lang_simplifier(SQL_num)

features = [rating, jobhq_yn,  age, python_yn, java_yn, C_plus_plus_yn, C_sharp_yn, PHP_yn,
            swift_yn, ruby_yn, javascript_yn, SQL_yn, senior_yn]
    
final_features = np.array(features).reshape(1, -1)

if st.button('Predict'):
    prediction = model.predict(final_features)
    st.balloons()
    st.success(f'Your predicted salary is US$ {round(prediction[0],2)} ')
  

