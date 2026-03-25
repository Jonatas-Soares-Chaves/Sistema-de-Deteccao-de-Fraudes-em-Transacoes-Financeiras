import streamlit as st
import pandas as pd
import time

time.sleep(5)
st.rerun()
# carregar dados
df = pd.read_csv("data/transacoes.csv")

# tratamento
df["data"] = pd.to_datetime(df["data"])

# regra de fraude
df["risco"] = df["valor"].apply(lambda x: 50 if x > 3000 else 0)

def classificar(score):
    if score >= 50:
        return "ALTO_RISCO"
    elif score >= 20:
        return "MEDIO_RISCO"
    return "BAIXO_RISCO"

df["classificacao"] = df["risco"].apply(classificar)

# 🎨 SIDEBAR (filtros)
st.sidebar.title("🔎 Filtros")

filtro = st.sidebar.selectbox(
    "Classificação",
    ["Todos", "ALTO_RISCO", "MEDIO_RISCO", "BAIXO_RISCO"]
)

if filtro != "Todos":
    df = df[df["classificacao"] == filtro]

# 🎯 TÍTULO
st.title("🚨 Fraud Detection Dashboard")

# 📊 MÉTRICAS
col1, col2, col3 = st.columns(3)

col1.metric("Total de Transações", len(df))
col2.metric("Fraudes Detectadas", len(df[df["classificacao"] == "ALTO_RISCO"]))
col3.metric("Ticket Médio", round(df["valor"].mean(), 2))

# 📈 GRÁFICO 1
st.subheader("Fraudes por País")
st.bar_chart(df[df["classificacao"] == "ALTO_RISCO"]["local"].value_counts())

# 📉 GRÁFICO 2 (evolução)
st.subheader("Evolução das Transações")
st.line_chart(df.groupby(df["data"].dt.date).size())

# ⚠️ INSIGHTS AUTOMÁTICOS
st.subheader("🧠 Insights Automáticos")

fraudes = df[df["classificacao"] == "ALTO_RISCO"]

if len(fraudes) > 100:
    st.error("🚨 Alto volume de fraudes detectado!")

elif len(fraudes) > 50:
    st.warning("⚠️ Volume moderado de fraudes")

else:
    st.success("✅ Baixo risco detectado")

# tabela
st.subheader("Transações Suspeitas")
st.dataframe(fraudes.sort_values(by="valor", ascending=False).head(20))