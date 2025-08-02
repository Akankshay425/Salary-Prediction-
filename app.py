import streamlit as st
import joblib
import numpy as np


st.title("Salary Prediction App")

st.divider()


st.write("With this app, \you can get estimation for the the salaries of the company employeess")

years = st.number_input("Enter the years at company",value = 1,step = 1,min_value = 0)
jobrate = st.number_input("Enter the job rate",value=3.5, step = 0.5,min_value= 0.0)

X = [years,jobrate]

model = joblib.load("Linearmodel.pkl")

st.divider()


predict = st.button("Press the button for salary prediction")

st.divider()

if predict:
    st.balloons()

    X1=np.array([X])
    prediction=model.predict(X1)[0]
    st.write("Salary prediction is ", prediction:,.2f")
else:
    st.write("Please press the button for app to make the prediction")