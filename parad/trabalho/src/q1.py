from __future__ import annotations
from typing import Iterable, List, Dict, Tuple


def q1a_metricas_sem_builtins(
    leituras: Iterable[float],
) -> Tuple[float, float, float, int]:
    """
    Calcula: média, mínimo, máximo e contagem de valores acima da média
    SEM usar sum/min/max/sorted (duas passagens).
    Retorna: (media, minimo, maximo, acima_media)
    """
    it = list(leituras)
    if not it:
        raise ValueError("Lista vazia.")

    soma = 0.0
    minimo = it[0]
    maximo = it[0]
    for v in it:
        soma += v
        if v < minimo:
            minimo = v
        if v > maximo:
            maximo = v
    media = soma / len(it)

    acima_media = 0
    for v in it:
        if v > media:
            acima_media += 1

    return media, minimo, maximo, acima_media


def q1b_metricas_com_builtins(
    leituras: Iterable[float],
) -> Tuple[float, float, float, int]:
    """
    Mesma métrica, usando funções nativas: sum, min, max, len.
    Retorna: (media, minimo, maximo, acima_media)
    """
    it = list(leituras)
    if not it:
        raise ValueError("Lista vazia.")

    media = sum(it) / len(it)
    minimo = min(it)
    maximo = max(it)
    acima_media = sum(1 for x in it if x > media)
    return media, minimo, maximo, acima_media


def q1a_traco_dry_run(leituras: Iterable[float]) -> List[Dict[str, float]]:
    """
    Gera um 'trace' (lista de dicionários) da 1ª passada da versão A.
    Cada item contém os valores de v, soma, min e max após a iteração.
    """
    it = list(leituras)
    if not it:
        return []
    soma = 0.0
    minimo = it[0]
    maximo = it[0]
    trace: List[Dict[str, float]] = []
    for v in it:
        soma += v
        if v < minimo:
            minimo = v
        if v > maximo:
            maximo = v
        trace.append({"v": v, "soma": soma, "min": minimo, "max": maximo})
    return trace
