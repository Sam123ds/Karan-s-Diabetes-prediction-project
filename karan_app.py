import streamlit as st
import pandas as pd
import numpy as np
import joblib

Pregnancies = st.number_input("Enter No. of Pregnancies",0,17,1)
Glucose = st.number_input("Enter Glucose level",0,17,5)
BloodPressure = st.number_input("Enter your BloodPressure",69,120,80)
SkinThickness = st.number_input("Enter SkinThickness: ",10,100,25)
Insulin = st.number_input("Enter Insulin",100,850,150)
BMI = st.number_input("Enter BMI",22,67,25)
DiabetesPedigreeFunction = st.number_input("Enter your DiabetesPedigreeFunction",0.078,2.42,1.00)
Age = st.number_input("Enter Age: ",21,81,70)

if st.button("Press to get your prediction"):
    input1 = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    arr=np.array(input1).reshape(1,8)
    SCALED_INPUT = ss.transform(arr)
    ypred_user = Karan_model.predict(SCALED_INPUT)
    if ypred_user[0] == 0:
        st.success("User has low risk of Diabetes")
    else:
        st.error("User has high risk of Diabetes")