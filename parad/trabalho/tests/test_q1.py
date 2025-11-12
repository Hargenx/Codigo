import math
import pytest
from src.q1 import q1a_metricas_sem_builtins, q1b_metricas_com_builtins, q1a_traco_dry_run

def test_q1a_metricas_sem_builtins_basico():
    leituras = [8.5, 7.2, 9.1, 11.0, 10.4, 6.9, 8.9]
    media, mn, mx, acima = q1a_metricas_sem_builtins(leituras)
    assert media == pytest.approx(62.0 / 7.0)
    assert mn == 6.9
    assert mx == 11.0
    assert acima == 4


def test_q1b_metricas_com_builtins_basico():
    leituras = [8.5, 7.2, 9.1, 11.0, 10.4, 6.9, 8.9]
    media, mn, mx, acima = q1b_metricas_com_builtins(leituras)
    assert media == pytest.approx(62.0 / 7.0)
    assert mn == 6.9
    assert mx == 11.0
    assert acima == 4


def test_q1a_traco_dry_run_formato():
    leituras = [8.5, 7.2, 9.1]
    trace = q1a_traco_dry_run(leituras)
    assert len(trace) == 3
    # último estado esperado
    assert trace[-1]["v"] == 9.1
    assert trace[-1]["soma"] == pytest.approx(8.5 + 7.2 + 9.1)
    assert trace[-1]["min"] == min(leituras)
    assert trace[-1]["max"] == max(leituras)


def test_q1_lista_vazia_levanta_erro():
    with pytest.raises(ValueError):
        q1a_metricas_sem_builtins([])
    with pytest.raises(ValueError):
        q1b_metricas_com_builtins([])
