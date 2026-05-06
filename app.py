import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

dados = pd.DataFrame([
    [180,3,3,4,2,1,1,1,1,1,950000],
    [160,3,2,3,2,1,0,1,0,1,780000],
    [200,4,3,4,2,1,1,1,1,1,1100000],
], columns=[
    "area_total","quartos","suites","banheiros","vagas",
    "area_gourmet","piscina","closet","jardim","cozinha_integrada","preco"
])

X = dados.drop("preco", axis=1)
y = dados["preco"]

modelo = LinearRegression()
modelo.fit(X, y)

st.title("🏠 Calculadora de Valor de Imóvel")

area = st.number_input("Área total")
quartos = st.number_input("Quartos")
suites = st.number_input("Suítes")
banheiros = st.number_input("Banheiros")
vagas = st.number_input("Vagas")

piscina = st.selectbox("Piscina", ["Não","Sim"])
piscina = 1 if piscina == "Sim" else 0

gourmet = st.selectbox("Área gourmet", ["Não","Sim"])
gourmet = 1 if gourmet == "Sim" else 0

closet = st.selectbox("Closet", ["Não","Sim"])
closet = 1 if closet == "Sim" else 0

jardim = st.selectbox("Jardim", ["Não","Sim"])
jardim = 1 if jardim == "Sim" else 0

cozinha = st.selectbox("Cozinha integrada", ["Não","Sim"])
cozinha = 1 if cozinha == "Sim" else 0

if st.button("Calcular"):
    entrada = [[area, quartos, suites, banheiros, vagas,
                gourmet, piscina, closet, jardim, cozinha]]
    
    preco = modelo.predict(entrada)[0]
    st.success(f"Valor estimado: R$ {preco:,.2f}")
