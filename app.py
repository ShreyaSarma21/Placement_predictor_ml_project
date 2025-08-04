import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# App title
st.title("🎓 Student Placement Predictor")
st.subheader("Enter CGPA and IQ to predict placement")

# User inputs
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter IQ", min_value=50, max_value=200, step=1)

# Prediction
if st.button("Predict Placement"):
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("The student is likely to be placed.")
    else:
        st.error("The student is not likely to be placed.")