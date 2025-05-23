import streamlit as st
import pandas as pd
import joblib

st.set_page_config(layout="wide",
    page_title="Heart Problem Detector",
    page_icon="❤️")

model = joblib.load("heart_pipeline.pkl")


st.title("Preditor de Doença Cardíaca ❤️")
st.write("Preencha os dados abaixo para prever a chance de doença cardíaca.")


cp_dict = {
    "Angina típica": 0,
    "Angina atípica": 1,
    "Dor não anginosa": 2,
    "Assintomático": 3
}

restecg_dict = {
    "Normal": 0,
    "Com anomalia ST-T": 1,
    "Hipertrofia ventricular esquerda": 2
}

slope_dict = {
    "Ascendente": 2,
    "Plano": 1,
    "Descendente": 0
}

thal_dict = {
    "Normal": 2,
    "Defeito fixo": 1,
    "Defeito reversível": 3
}


age = st.number_input("Idade", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sexo", ("Masculino", "Feminino"))
cp = st.selectbox("Tipo de dor no peito", list(cp_dict.keys()))
trestbps = st.number_input("Pressão arterial em repouso (mm Hg)", min_value=50, max_value=250, value=130)
chol = st.number_input("Colesterol sérico (mg/dl)", min_value=100, max_value=600, value=230)
fbs = st.selectbox("Açúcar no sangue em jejum > 120 mg/dl", ("Não", "Sim"))
restecg = st.selectbox("Resultado do eletrocardiograma", list(restecg_dict.keys()))
thalach = st.number_input("Frequência cardíaca máxima alcançada", min_value=60, max_value=250, value=150)
exang = st.selectbox("Angina induzida por exercício?", ("Não", "Sim"))
oldpeak = st.number_input("Depressão do ST induzida por exercício", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Inclinação do segmento ST", list(slope_dict.keys()))
ca = st.number_input("Número de vasos principais com fluoroscopia colorida", min_value=0, max_value=4, value=0)
thal = st.selectbox("Talassemia", list(thal_dict.keys()))


data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == "Masculino" else 0],
    'cp': [cp_dict[cp]],
    'trestbps': [trestbps],
    'chol': [chol],
    'fbs': [1 if fbs == "Sim" else 0],
    'restecg': [restecg_dict[restecg]],
    'thalach': [thalach],
    'exang': [1 if exang == "Sim" else 0],
    'oldpeak': [oldpeak],
    'slope': [slope_dict[slope]],
    'ca': [ca],
    'thal': [thal_dict[thal]]
})


if st.button("Prever"):
    prediction = model.predict(data)[0]
    if prediction == 0:
        st.error("🚨 Alta probabilidade de doença cardíaca.")
    else:
        st.success("✅ Baixa probabilidade de doença cardíaca.")
