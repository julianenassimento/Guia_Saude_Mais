import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PLANOS_PATH = BASE_DIR / "data" / "planos.json"

with PLANOS_PATH.open(encoding="utf-8") as f:
    planos = json.load(f)


def calcular_reembolso(valor, plano):
    plano = plano.lower().strip()

    if plano not in planos:
        return None, "Plano não encontrado"

    limite = planos[plano]["consulta"]
    reembolso = min(float(valor), float(limite))
    return reembolso, None
