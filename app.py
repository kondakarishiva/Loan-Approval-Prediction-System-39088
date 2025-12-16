import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("loan_approval_model.pkl", "rb"))

st.title("🏦 Loan Approval Prediction System")

st.write("Enter customer details to predict loan approval")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income = st.number_input("Applicant Income", 0)
loan_amount = st.number_input("Loan Amount", 0)
credit_history = st.selectbox("Credit History", [1, 0])

# Convert inputs
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

if st.button("Predict"):
    input_data = np.array([[gender, married, education, self_employed,
                             income, loan_amount, credit_history]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
