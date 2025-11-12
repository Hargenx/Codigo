from __future__ import annotations
from typing import Iterable, Iterator, List


def q2a_comprehension(leituras: Iterable[float]) -> List[float]:
    """
    Estilo funcional com compreensão:
    filtra 8 <= x <= 11 e retorna x^2 arredondado em 2 casas.
    """
    return [round(x * x, 2) for x in leituras if 8 <= x <= 11]


def q2b_filter_map(leituras: Iterable[float]) -> List[float]:
    """
    Estilo funcional com filter + map (puro).
    """
    filtrados: Iterator[float] = filter(lambda x: 8 <= x <= 11, leituras)
    mapeados: Iterator[float] = map(lambda x: round(x * x, 2), filtrados)
    return list(mapeados)
