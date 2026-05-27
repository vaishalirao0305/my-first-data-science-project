
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn App")

age = st.number_input("Age")
monthly = st.number_input("Monthly Charges")
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

if contract == "Month-to-month":
    contract_val = 0
elif contract == "One year":
    contract_val = 1
else:
    contract_val = 2

if st.button("Predict"):
    input_data = np.array([[age, monthly, contract_val]])
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("Customer will LEAVE ❌")
    else:
        st.success("Customer will STAY ✅")
