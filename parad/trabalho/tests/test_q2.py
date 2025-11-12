import os
import sys
# ensure project root is on sys.path so 'src' package can be imported during tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.q2 import q2a_comprehension, q2b_filter_map


def test_q2_resultados_iguais():
    leituras = [7, 8, 8.5, 11, 12]
    esperado = [64.0, 72.25, 121.0]
    assert q2a_comprehension(leituras) == esperado
    assert q2b_filter_map(leituras) == esperado


def test_q2_nao_altera_entrada():
    leituras = [7, 8, 8.5, 11, 12]
    _ = q2a_comprehension(leituras)
    _ = q2b_filter_map(leituras)
    assert leituras == [7, 8, 8.5, 11, 12]
