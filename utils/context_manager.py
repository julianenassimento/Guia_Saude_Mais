class ContextManager:
    def __init__(self, contexto_inicial=None):
        self.contexto = contexto_inicial or {}

    def salvar(self, chave, valor):
        self.contexto[chave] = valor

    def obter(self, chave, padrao=None):
        return self.contexto.get(chave, padrao)

    def exportar(self):
        return self.contexto
