import pytest
from src.q3 import (
    Medicao,
    Unidade,
    CobrancaProporcional,
    CobrancaRateioFixo,
    Fatura,
)


def montar_cenario_basico():
    u101 = Unidade("101")
    u102 = Unidade("102")
    u101.adicionar_medicao(Medicao("2025-02", 9.2, 150))
    u102.adicionar_medicao(Medicao("2025-02", 11.5, 175))
    # outra medição em mês diferente para garantir filtragem
    u101.adicionar_medicao(Medicao("2025-03", 8.9, 140))
    return [u101, u102]


def test_proporcional_total_por_unidade():
    unidades = montar_cenario_basico()
    criterio = CobrancaProporcional(tarifa_agua=5.0, tarifa_energia=0.9)
    fatura = Fatura("2025-02", unidades, criterio)
    totais = fatura.total_por_unidade()
    # u101: 5*9.2 + 0.9*150 = 46 + 135 = 181.0
    # u102: 5*11.5 + 0.9*175 = 57.5 + 157.5 = 215.0
    assert totais["101"] == pytest.approx(181.0)
    assert totais["102"] == pytest.approx(215.0)


def test_rateio_fixo_somente_unidades_ativas():
    unidades = montar_cenario_basico()
    criterio = CobrancaRateioFixo(
        total_mes=1000.0, todas_unidades=unidades, mes="2025-02"
    )
    fatura = Fatura("2025-02", unidades, criterio)
    totais = fatura.total_por_unidade()
    # Ativas em 2025-02: 101 e 102 → 1000/2 = 500 para cada
    assert totais["101"] == pytest.approx(500.0)
    assert totais["102"] == pytest.approx(500.0)


def test_rateio_fixo_sem_ativas_erro():
    u1 = Unidade("1")
    u2 = Unidade("2")
    # sem medições no mês → erro
    with pytest.raises(ValueError):
        _ = CobrancaRateioFixo(total_mes=1000.0, todas_unidades=[u1, u2], mes="2025-02")


def test_validacoes_medicao():
    with pytest.raises(ValueError):
        _ = Medicao("2025-02", -1.0, 10.0)
    with pytest.raises(ValueError):
        _ = Medicao("202502", 1.0, 10.0)  # formato inválido
