class Playlist:
    def __init__(self, nome, limite=100):
        self._faixas = []
        self.nome = nome  # valida pelo setter
        self.limite = limite  # valida pelo setter

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("nome inválido")
        self._nome = valor.strip()

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        valor = int(valor)
        if valor <= 0 or valor < len(self._faixas):
            raise ValueError("limite inválido")
        self._limite = valor

    def adicionar(self, titulo, duracao_seg):
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("título inválido")
        duracao = int(duracao_seg)
        if duracao <= 0:
            raise ValueError("duração deve ser positiva")
        if len(self._faixas) >= self.limite:
            raise ValueError("playlist cheia")
        if any(titulo.strip() == t for t, _ in self._faixas):
            raise ValueError("faixa duplicada")
        self._faixas.append((titulo.strip(), duracao))

    def listar(self):
        return tuple(self._faixas)  # cópia imutável (não vaza estado)
