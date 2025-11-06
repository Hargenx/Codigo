from typing import Iterable
import math

def media(valores: Iterable[float], ndigits: int | None = None) -> float:
    """
    Calcula a média aritmética de `valores`.
    ARGs:
        valores: iterável de números (lista, tupla, conjunto ou gerador).
        ndigits: se fornecido, número de casas decimais para arredondar.
    Return:
        float: média aritmética.
    Raises:
        ValueError: se `valores` estiver vazio.
    """
    dados = tuple(float(v) for v in valores)
    if not dados:
        raise ValueError("sequência vazia: média indefinida")

    m = math.fsum(dados) / len(dados)
    return round(m, ndigits) if ndigits is not None else m

print(media([10, 20, 30]))  # Exemplo de uso