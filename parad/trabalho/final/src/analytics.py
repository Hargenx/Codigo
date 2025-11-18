from typing import List, Dict, Tuple
from collections import Counter

import numpy as np

from models import Pedido


def _valores_pedidos(pedidos: List[Pedido]) -> np.ndarray:
    """Cria um array numpy com o valor total de cada pedido."""
    return np.array([pedido.valor_total() for pedido in pedidos], dtype=float)


def calcular_faturamento_total(pedidos: List[Pedido]) -> float:
    """Retorna o faturamento total do dia (soma do valor de todos os pedidos)."""
    if not pedidos:
        return 0.0

    valores = _valores_pedidos(pedidos)
    total = float(np.sum(valores))
    return total


def calcular_ticket_medio(pedidos: List[Pedido]) -> float:
    """Retorna o ticket médio (valor médio por pedido)."""
    if not pedidos:
        return 0.0

    faturamento = calcular_faturamento_total(pedidos)
    ticket_medio = faturamento / len(pedidos)
    return ticket_medio


def calcular_estatisticas_valores(pedidos: List[Pedido]) -> Dict[str, float]:
    """
    Calcula estatísticas simples dos valores dos pedidos
    (mínimo, máximo e média) usando numpy.
    """
    if not pedidos:
        return {"minimo": 0.0, "maximo": 0.0, "media": 0.0}

    valores = _valores_pedidos(pedidos)

    estatisticas = {
        "minimo": float(np.min(valores)),
        "maximo": float(np.max(valores)),
        "media": float(np.mean(valores)),
    }
    return estatisticas


def top_produtos_mais_vendidos(
    pedidos: List[Pedido], n: int = 3
) -> List[Tuple[str, int]]:
    """
    Retorna os N produtos mais vendidos como lista de tuplas:
    [(nome_produto, quantidade), ...]
    """
    contador = Counter()

    for pedido in pedidos:
        for produto in pedido.produtos:
            contador[produto.nome] += 1

    return contador.most_common(n)
