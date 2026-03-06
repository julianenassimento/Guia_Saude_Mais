import json
import re
from pathlib import Path

from models.intent_classifier import prever_intencao
from services.simulador_reembolso import calcular_reembolso
from utils.context_manager import ContextManager

BASE_DIR = Path(__file__).resolve().parent.parent
FAQ_PATH = BASE_DIR / "data" / "faq_data.json"

with FAQ_PATH.open(encoding="utf-8") as f:
    faq = json.load(f)


def extrair_valor(texto):
    texto = texto.replace("R$", "").replace("r$", "")
    padrao = r"\d+(?:[.,]\d{1,2})?"
    match = re.search(padrao, texto)

    if not match:
        return None

    valor_txt = match.group(0).replace(",", ".")
    try:
        return float(valor_txt)
    except ValueError:
        return None


def extrair_plano(texto):
    texto = texto.lower()
    for plano in ("premium", "top", "basico"):
        if plano in texto:
            return plano
    return None


def responder(pergunta, contexto=None):
    if contexto is None:
        contexto = ContextManager()

    pergunta = (pergunta or "").strip()
    if not pergunta:
        return "Digite uma pergunta para eu te ajudar."

    pergunta_lower = pergunta.lower()
    intencao = prever_intencao(pergunta_lower)

    contexto.salvar("ultima_pergunta", pergunta)

    plano_mencionado = extrair_plano(pergunta_lower)
    if plano_mencionado:
        contexto.salvar("plano", plano_mencionado)

    if intencao == "reembolso" or "reembolso" in pergunta_lower:
        valor = extrair_valor(pergunta)
        plano = contexto.obter("plano", "premium")

        if valor is None:
            return f"Me informe o valor da consulta para simular o reembolso do plano {plano}."

        resultado, erro = calcular_reembolso(valor, plano)
        if erro:
            return erro

        return f"Estimativa de reembolso ({plano.title()}): R${resultado:.2f}"

    return faq.get(intencao, faq["geral"])
