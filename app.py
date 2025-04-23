import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Loan Status Predictor",
    page_icon="💰",
)

with open("model7.pkl", "rb") as file:
    model7 = pickle.load(file)


st.title("Loan Status Predictor 💰")
with st.expander("Enter Your Details"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Loan_ID = st.text_input("Loan ID", value="LP001")
    with col2:
        Gender = st.selectbox("Select Your Gender", ["Male", "Female"])
    with col3:
        Married = st.selectbox("Marriage Status", ["Yes", "No"])

    col4, col5, col6 = st.columns(3)
    with col4:
        Dependents = st.selectbox("Number of Childrens", ["0", "1", "2", "3+"], index=0)
    with col5:
        Education = st.selectbox("Education level", ["Graduate", "Not-Graduate"])
    with col6:
        Self_Employed = st.selectbox("Self-Employment Status", ["Yes", "No"])

    col7, col8, col9 = st.columns(3)
    with col7:
        ApplicantIncome = st.number_input(
            "Enter Applicant Income", min_value=0.0, step=1.0, max_value=81000.0
        )
    with col8:
        CoapplicantIncome = st.number_input(
            "Enter Co-Applicant Income", min_value=0.0, step=1.0, max_value=41667.0
        )
    with col9:
        LoanAmount = st.number_input(
            "Enter Your On-going Loan Amount", min_value=0.0, step=1.0, max_value=700.0
        )

    col10, col11, col12 = st.columns(3)
    with col10:
        Loan_Amount_Term = st.selectbox(
            "Select Loan Term (in days)",
            [360.0, 180.0, 480.0, 342.0, 300.0, 240.0, 84.0, 120.0, 60.0, 36.0, 12.0],
        )
    with col11:
        Credit_History = st.selectbox("Credit History", [1.0, 0.0])
    with col12:
        Property_Area = st.selectbox(
            "Select Your Region", ["Semiurban", "Urban", "Rural"]
        )


data = {
    "Loan_ID": Loan_ID,
    "Gender": 1 if Gender == "Male" else 0,  # if gender is male then 1 else 0
    "Married": 1 if Married == "Yes" else 0,  # if married is yes then 1 else 0
    "Dependents": (
        3 if Dependents == "3+" else int(Dependents)
    ),  # if dependents is "3+" then 3 else int(dependents)means(0,1,2)
    "Education": (
        1 if Education == "Graduate" else 0
    ),  # if education is "Graduate" then 1 else 0
    "Self_Employed": (
        1 if Self_Employed == "Yes" else 0
    ),  # if self employed is "Yes" then 1 else 0
    "ApplicantIncome": ApplicantIncome,
    "CoapplicantIncome": CoapplicantIncome,
    "LoanAmount": LoanAmount,
    "Loan_Amount_Term": Loan_Amount_Term,
    "Credit_History": Credit_History,  # if the credit_history is 0.0(negative) loan will not be approved
    "Property_Area": (
        2
        if Property_Area == "Urban"
        else (
            1 if Property_Area == "Semiurban" else 0
        )  # if property area is urban then 2 else (if property_area in semi urban then 1 else 0)
    ),
}


input_text = pd.DataFrame([data])

if st.button("Predict Loan Status"):
    prediction = model7.predict(input_text.drop(columns=["Loan_ID"]))[
        0
    ]  # Exclude Loan_ID for prediction
    result = (
        "The Loan is Approved" if prediction == 1 else "The Loan is Not Approved"
    )  # if else condition just like above
    st.write(f"Loan ID: {Loan_ID}")
    st.write(f"Loan Status: {result}")
