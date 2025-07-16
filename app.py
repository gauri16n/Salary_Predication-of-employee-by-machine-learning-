import streamlit as st
import joblib
import numpy as np
st.title("Salary Prediction App")
st.divider()




st.write("with this app,you can get estimations for the salaries of the company employee")

years=st.number_input("enter the years at company",value=1,step=1,min_value=0)
jobrate=st.number_input("enter the job rate",value=3.5,step=0.5,min_value=0.0)

x=[years,jobrate]

import joblib

model = joblib.load('linearmodel.pkl')  


predict=st.button("press the button for salary predication")


st.divider()

if predict:

    st.balloons()

    X1 = np.array([x])  # 2D array: shape (1, 2)
    prediction = model.predict(X1)   # ✅ correct


    prediction = model.predict(X1)
    st.write(f"💰 Salary prediction is ₹{prediction[0]:,.2f}")








else:
    "please press the button for app to make the predication"