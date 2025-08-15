import streamlit as st
import numpy as np
import joblib
import os

st.set_page_config(page_title="Loan Approval Prediction", layout="centered")

st.title("Loan Approval Prediction")

# Try to load the trained model
model_path = 'loan_approval_model.pkl'
if not os.path.exists(model_path):
    st.error("Model file not found. Please ensure 'loan_approval_model.pkl' is in the same directory.")
    st.stop()

model = joblib.load(model_path)

st.markdown("**Please enter the following details as per your dataset's encoding:**")

# Input fields (adjust the options to match your label encoding)
gender = st.selectbox("Gender", [("Male", 1), ("Female", 0)])
married = st.selectbox("Married", [("Yes", 1), ("No", 0)])
dependents = st.selectbox("Dependents", [("0", 0), ("1", 1), ("2", 2), ("3+", 3)])
education = st.selectbox("Education", [("Graduate", 0), ("Not Graduate", 1)])
self_employed = st.selectbox("Self Employed", [("No", 0), ("Yes", 1)])
property_area = st.selectbox("Property Area", [("Urban", 2), ("Semiurban", 1), ("Rural", 0)])
loan_amount_log = st.number_input("Loan Amount (log transformed)", min_value=0.0, format="%.4f")
credit_history = st.selectbox("Credit History", [("Yes", 1.0), ("No", 0.0)])
loan_amount_term_log = st.number_input("Loan Amount Term (log transformed)", min_value=0.0, format="%.4f")
applicant_income_log = st.number_input("Applicant Income (log transformed)", min_value=0.0, format="%.4f")
total_income_log = st.number_input("Total Income (log transformed)", min_value=0.0, format="%.4f")
loan_amount = st.number_input("Loan Amount (original)", min_value=0.0, format="%.2f")

# Prepare input in the order your model expects
input_data = np.array([[ 
    gender[1],
    married[1],
    dependents[1],
    education[1],
    self_employed[1],
    property_area[1],
    loan_amount_log,
    credit_history[1],
    loan_amount_term_log,
    applicant_income_log,
    total_income_log,
    loan_amount
]])

if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.success("Loan Approved!")
        else:
            st.error("Loan Not Approved.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")