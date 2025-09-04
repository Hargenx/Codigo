from dataclasses import dataclass
from investidor import Agente

@dataclass
class Ordem:
    tipo: str            # "compra" ou "venda"
    agente: "Agente"     # Agente que criou a ordem
    ativo: str           # Nome do ativo (ex.: "FII")
    preco_limite: float  # Preço máximo (para compra) ou mínimo (para venda)
    quantidade: int      # Quantidade a negociar