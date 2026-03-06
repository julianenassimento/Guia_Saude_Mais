import streamlit as st

from services.chat_service import responder
from utils.context_manager import ContextManager

st.set_page_config(page_title="HealthGuide AI", page_icon="🩺")
st.title("HealthGuide AI")
st.write("Assistente inteligente para dúvidas sobre planos de saúde")

if "historico" not in st.session_state:
    st.session_state.historico = []

if "contexto_data" not in st.session_state:
    st.session_state.contexto_data = {}

contexto = ContextManager(st.session_state.contexto_data)

plano_ui = st.selectbox(
    "Seu plano (opcional):",
    ["", "basico", "top", "premium"],
    index=0,
)

if plano_ui:
    contexto.salvar("plano", plano_ui)
    st.session_state.contexto_data = contexto.exportar()

pergunta = st.text_input("Digite sua pergunta")

if st.button("Enviar"):
    resposta = responder(pergunta, contexto)

    st.session_state.historico.append(("Você", pergunta))
    st.session_state.historico.append(("Assistente", resposta))
    st.session_state.contexto_data = contexto.exportar()

for autor, msg in st.session_state.historico:
    st.write(f"**{autor}:** {msg}")
