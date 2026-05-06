import streamlit as st

st.title("🏗️ Calculadora de Tempo de Obra")

st.write("Preencha os dados da obra:")

# ------------------------
# ENTRADAS
# ------------------------
area = st.number_input("Área construída (m²)", value=220.38)
pavimentos = st.number_input("Número de pavimentos", value=1)
trabalhadores = st.number_input("Número de trabalhadores", value=10)

tipo = st.selectbox("Tipo de obra", ["Casa", "Prédio"])
metodo = st.selectbox("Método construtivo", ["Alvenaria padrão", "Pré-moldado", "Estrutura metálica"])
clima = st.selectbox("Clima", ["Tropical típico", "Chuvoso", "Seco"])

# ------------------------
# CÁLCULO
# ------------------------
if st.button("⏱️ Calcular tempo"):

    # Base: produtividade média (m² por mês por trabalhador)
    produtividade = 12  

    # Ajustes
    if metodo == "Pré-moldado":
        produtividade *= 1.3
    elif metodo == "Estrutura metálica":
        produtividade *= 1.5

    if clima == "Chuvoso":
        produtividade *= 0.8
    elif clima == "Seco":
        produtividade *= 1.1

    if tipo == "Prédio":
        produtividade *= 0.7

    # Cálculo do tempo
    tempo = area / (produtividade * trabalhadores)

    # Ajuste por pavimentos
    tempo *= (1 + (pavimentos - 1) * 0.2)

    st.success(f"Tempo estimado: {tempo:.1f} meses")
