import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# sample dataset
data = {
    "age": [40, 78, 65, 50, 90, 33, 59, 70, 45, 82],
    "num_prev_adm": [0, 3, 2, 1, 5, 0, 4, 2, 1, 6],
    "length_stay": [3, 10, 7, 4, 14, 2, 9, 6, 3, 15],
    "chronic_conditions": [1, 4, 3, 2, 6, 1, 5, 3, 2, 7],
    "readmit_30": [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df.drop("readmit_30", axis=1)
y = df["readmit_30"]

model = LogisticRegression()
model.fit(X, y)

# --- Streamlit UI ---
st.title("Patient Readmission Risk Predictor")
st.caption("Predicts if a patient will be readmitted within 30 days of discharge.")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
num_prev_adm = st.number_input("Previous Admissions (past year)", 0, 20, 1)
length_stay = st.number_input("Length of Stay (days)", 1, 60, 5)
chronic_conditions = st.number_input("Number of Chronic Conditions", 0, 10, 2)

if st.button("Predict Readmission"):
    input_data = [[age, num_prev_adm, length_stay, chronic_conditions]]
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("High Risk: Patient is likely to be readmitted.")
    else:
        st.success("Low Risk: Patient unlikely to be readmitted.")
