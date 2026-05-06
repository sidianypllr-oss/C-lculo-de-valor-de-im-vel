import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# ------------------------
# GERANDO BASE DE DADOS
# ------------------------
np.random.seed(42)

n = 100

dados = pd.DataFrame({
    "area": np.random.randint(50, 400, n),
    "quartos": np.random.randint(1, 5, n),
    "banheiros": np.random.randint(1, 5, n),
    "padrao": np.random.randint(1, 4, n),
    "piscina": np.random.randint(0, 2, n),
    "gourmet": np.random.randint(0, 2, n),
    "complexidade": np.random.randint(1, 5, n),
})

# ------------------------
# CRIANDO TEMPO REALISTA
# ------------------------
dados["tempo"] = (
    dados["area"] * 0.05 +
    dados["quartos"] * 1 +
    dados["banheiros"] * 0.8 +
    dados["padrao"] * 2 +
    dados["piscina"] * 3 +
    dados["gourmet"] * 2 +
    dados["complexidade"] * 2
)

# ------------------------
# TREINANDO MODELO
# ------------------------
X = dados.drop("tempo", axis=1)
y = dados["tempo"]

modelo = LinearRegression()
modelo.fit(X, y)

# ------------------------
# INTERFACE
# ------------------------
st.title("🏗️ Calculadora de Tempo de Obra")

area = st.number_input("Área (m²)", 50, 500)
quartos = st.number_input("Quartos", 1, 10)
banheiros = st.number_input("Banheiros", 1, 6)

padrao = st.selectbox("Padrão de acabamento", [1,2,3])

piscina = st.selectbox("Piscina", ["Não","Sim"])
piscina = 1 if piscina == "Sim" else 0

gourmet = st.selectbox("Área gourmet", ["Não","Sim"])
gourmet = 1 if gourmet == "Sim" else 0

complexidade = st.slider("Complexidade da obra", 1, 5)

# ------------------------
# CÁLCULO
# ------------------------
if st.button("⏱️ Calcular tempo"):
    entrada = [[area, quartos, banheiros, padrao, piscina, gourmet, complexidade]]
    tempo = modelo.predict(entrada)[0]

    st.success(f"Tempo estimado: {tempo:.1f} meses")
