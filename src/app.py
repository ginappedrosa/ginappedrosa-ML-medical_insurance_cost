# your code here
import streamlit as st

import pandas as pd
import json
import streamlit as st
import pickle
from pickle import load

with open("/workspaces/ginappedrosa-ML-medical_insurance_cost/src/modelo_regresion_lineal.pkl", "rb") as file:
    model = pickle.load(file)# Cargar columnas de JSON
with open("/workspaces/ginappedrosa-ML-medical_insurance_cost/src/sex_rules.json", "r") as f:
    sex_dic = json.load(f)
with open("/workspaces/ginappedrosa-ML-medical_insurance_cost/src/smoker_rules.json", "r") as f:
    smoker_dic = json.load(f)
    
st.title("Haz una predicción del coste de tu seguro médico")
st.write("Introduce tus datos:")
age = st.number_input("Edad", 18, 100, 30)
children = st.number_input("Número de hijos", 0, 10, 0)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
sex_n = st.selectbox("Sexo", ["male", "female"])
smoker_n = st.selectbox("Fumador", ["yes", "no"])
sex_n = sex_dic[sex_n]
smoker_n = smoker_dic[smoker_n]

row = [[age,sex_n,bmi,children,smoker_n]]

if st.button("Calcula el coste de tu seguro"):
    prediction = model.predict(row)[0]
    st.write(f"El coste estimado de tu seguro es de: ${prediction:,.2f}")