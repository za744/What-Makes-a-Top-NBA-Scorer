import streamlit as st
import numpy as np
import joblib

model=joblib.load("ppg_model_1")
feature_names=joblib.load("feature_names")

st.title("NBA PPG Predictor")
st.write("Enter player stats in terms of a per game basis")

user_input={}
for feature in feature_names:
    if(feature.startswith("Pos_")):
        continue
    user_input[feature] = st.number_input(f"{feature}", value =0.0)

position = st.selectbox("Select Position", options=["C", "PF", "SF", "SG", "PG"])
user_input["Pos_C"]  = int(position == "C")
user_input["Pos_PF"] = int(position == "PF")
user_input["Pos_SF"] = int(position == "SF")
user_input["Pos_SG"] = int(position == "SG")
user_input["Pos_PG"] = int(position == "PG")

input_array = np.array([user_input[feat] for feat in feature_names]).reshape(1, -1)

if st.button("Predict"):
    #input_array=np.array([list(user_input.values())])
    predictioon = model.predict(input_array)[0]
    st.success(f"predicted ppg: {predictioon:.2f}")

