import json
import streamlit as st
import streamlit.components.v1 as components

from services.chat_service import responder
from utils.context_manager import ContextManager

st.set_page_config(page_title="Guia Saude Mais", layout="centered")

if "historico" not in st.session_state:
    st.session_state.historico = []

if "contexto_data" not in st.session_state:
    st.session_state.contexto_data = {}

if "ultima_resposta" not in st.session_state:
    st.session_state.ultima_resposta = ""

contexto = ContextManager(st.session_state.contexto_data)

st.title("Guia Saude Mais")

with st.sidebar:
    st.subheader("Acessibilidade")
    alto_contraste = st.toggle("Alto contraste", value=True)
    fonte_grande = st.toggle("Fonte grande", value=True)
    ativar_libras = st.toggle("Ativar Libras (VLibras)", value=True)
    plano_ui = st.selectbox("Plano", ["", "basico", "top", "premium"], index=0)

if plano_ui:
    contexto.salvar("plano", plano_ui)
    st.session_state.contexto_data = contexto.exportar()

bg = "#000000" if alto_contraste else "#f5f5f5"
fg = "#ffffff" if alto_contraste else "#111111"
font_size = "22px" if fonte_grande else "17px"

st.markdown(
    f"""
    <style>
    .box {{
        background: {bg};
        color: {fg};
        border-radius: 10px;
        padding: 14px;
        font-size: {font_size};
        line-height: 1.5;
        border: 2px solid #2b2b2b;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.form("chat_form", clear_on_submit=True):
    pergunta = st.text_area(
        "Digite sua pergunta (caixa única):",
        height=120,
        placeholder="Ex: Quanto recebo de reembolso de 400 no plano top?",
    )
    enviar = st.form_submit_button("Enviar")

if enviar:
    resposta = responder(pergunta, contexto)
    st.session_state.ultima_resposta = resposta
    st.session_state.historico.append(("Você", pergunta))
    st.session_state.historico.append(("Assistente", resposta))
    st.session_state.contexto_data = contexto.exportar()

st.subheader("Resposta")
st.markdown(
    f'<div class="box">{st.session_state.ultima_resposta or "Sem resposta ainda."}</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Ouvir resposta", use_container_width=True):
        texto = json.dumps(st.session_state.ultima_resposta or "Sem resposta ainda.")
        components.html(
            f"""
            <script>
            const texto = {texto};
            if ("speechSynthesis" in window) {{
              window.speechSynthesis.cancel();
              const u = new SpeechSynthesisUtterance(texto);
              u.lang = "pt-BR";
              u.rate = 1.0;
              u.pitch = 1.0;
              window.speechSynthesis.speak(u);
            }}
            </script>
            """,
            height=0,
        )

with col2:
    if st.button("Parar voz", use_container_width=True):
        components.html(
            """
            <script>
            if ("speechSynthesis" in window) {
              window.speechSynthesis.cancel();
            }
            </script>
            """,
            height=0,
        )

with st.expander("Ver histórico"):
    for autor, msg in st.session_state.historico:
        st.write(f"**{autor}:** {msg}")

if ativar_libras:
    components.html(
        """
        <div vw class="enabled">
          <div vw-access-button class="active"></div>
          <div vw-plugin-wrapper>
            <div class="vw-plugin-top-wrapper"></div>
          </div>
        </div>
        <script src="https://vlibras.gov.br/app/vlibras-plugin.js"></script>
        <script>
          new window.VLibras.Widget("https://vlibras.gov.br/app");
        </script>
        """,
        height=120,
    )
