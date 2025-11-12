from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Iterator, List, Dict, Tuple


# =========================================================
# Q1 — Estruturada
#  A) sem sum/min/max  |  B) com funções nativas
# =========================================================


def q1a_metricas_sem_builtins(
    leituras: Iterable[float],
) -> Tuple[float, float, float, int]:
    """
    Calcula média, mínimo, máximo e contagem de valores acima da média
    SEM usar sum/min/max/sorted. Faz duas passagens (claro e didático).

    Retorna: (media, minimo, maximo, acima_media)
    """
    it = list(leituras)
    if not it:
        raise ValueError("Lista vazia.")

    # 1ª passada: soma, min, max
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

    # 2ª passada: contar acima da média
    acima_media = 0
    for v in it:
        if v > media:
            acima_media += 1

    return media, minimo, maximo, acima_media


def q1b_metricas_com_builtins(
    leituras: Iterable[float],
) -> Tuple[float, float, float, int]:
    """
    Mesma métrica, mas usando funções nativas: sum, min, max, len.
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
    Gera um 'trace' da 1ª passada da versão A (útil para corrigir no papel).
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


# =========================================================
# Q2 — Funcional (versões puras)
# =========================================================


def q2a_comprehension(leituras: Iterable[float]) -> List[float]:
    """
    Versão funcional com compreensão de listas:
    filtra 8 <= x <= 11 e retorna x^2 arredondado em 2 casas.
    """
    return [round(x * x, 2) for x in leituras if 8 <= x <= 11]


def q2b_filter_map(leituras: Iterable[float]) -> List[float]:
    """
    Versão funcional com filter + map (pura).
    """
    filtrados: Iterator[float] = filter(lambda x: 8 <= x <= 11, leituras)
    mapeados: Iterator[float] = map(lambda x: round(x * x, 2), filtrados)
    return list(mapeados)


# =========================================================
# Q3 — POO (modelagem com polimorfismo)
# =========================================================


@dataclass(slots=True)
class Medicao:
    mes: str
    agua_m3: float
    energia_kwh: float

    def __post_init__(self) -> None:
        if self.agua_m3 < 0 or self.energia_kwh < 0:
            raise ValueError("Consumos não podem ser negativos.")
        # validação simples do formato AAAA-MM
        if len(self.mes) != 7 or self.mes[4] != "-":
            raise ValueError("Formato de mês inválido. Esperado: 'YYYY-MM'.")


class Unidade:
    __slots__ = ("numero", "_medicoes")

    def __init__(self, numero: str) -> None:
        self.numero = numero
        self._medicoes: List[Medicao] = []

    def adicionar_medicao(self, m: Medicao) -> None:
        self._medicoes.append(m)

    def medicoes_do_mes(self, mes: str) -> List[Medicao]:
        return [m for m in self._medicoes if m.mes == mes]


class CriterioCobranca(ABC):
    @abstractmethod
    def calcular(self, unidade: Unidade, mes: str) -> float:
        """Retorna o valor devido pela unidade no mês."""


class CobrancaProporcional(CriterioCobranca):
    """
    Cobra por consumo real (tarifas fixas fornecidas no construtor).
    """

    def __init__(self, tarifa_agua: float, tarifa_energia: float) -> None:
        self.tarifa_agua = tarifa_agua
        self.tarifa_energia = tarifa_energia

    def calcular(self, unidade: Unidade, mes: str) -> float:
        medicoes = unidade.medicoes_do_mes(mes)
        agua = sum(m.agua_m3 for m in medicoes)
        energia = sum(m.energia_kwh for m in medicoes)
        return self.tarifa_agua * agua + self.tarifa_energia * energia


class CobrancaRateioFixo(CriterioCobranca):
    """
    Divide um valor total fixo igualmente entre unidades que possuem
    pelo menos uma medição no mês.
    """

    def __init__(
        self, total_mes: float, todas_unidades: Iterable[Unidade], mes: str
    ) -> None:
        self.total_mes = total_mes
        self._ativas = [u for u in todas_unidades if u.medicoes_do_mes(mes)]
        if not self._ativas:
            raise ValueError("Nenhuma unidade ativa no mês para rateio.")

    def calcular(self, unidade: Unidade, mes: str) -> float:
        # Se a unidade não tem medição no mês, cobra 0 (ou poderia lançar erro, conforme regra)
        if unidade not in self._ativas:
            return 0.0
        return self.total_mes / len(self._ativas)


class Fatura:
    """
    Agrega cálculo por unidade via despacho polimórfico de 'criterio.calcular'.
    """

    __slots__ = ("mes", "unidades", "criterio")

    def __init__(
        self, mes: str, unidades: Iterable[Unidade], criterio: CriterioCobranca
    ) -> None:
        self.mes = mes
        self.unidades = list(unidades)
        self.criterio = criterio

    def total_por_unidade(self) -> Dict[str, float]:
        return {u.numero: self.criterio.calcular(u, self.mes) for u in self.unidades}


# =========================================================
# Demonstração rápida (pode remover/ajustar)
# =========================================================

if __name__ == "__main__":
    leituras = [8.5, 7.2, 9.1, 11.0, 10.4, 6.9, 8.9]

    print("Q1A — sem builtins:")
    media, mn, mx, acima = q1a_metricas_sem_builtins(leituras)
    print(f"  média={media:.6f}  min={mn}  max={mx}  acima_da_média={acima}")

    print("\nQ1B — com builtins:")
    media2, mn2, mx2, acima2 = q1b_metricas_com_builtins(leituras)
    print(f"  média={media2:.6f}  min={mn2}  max={mx2}  acima_da_média={acima2}")

    print("\nQ1A — dry run (1ª passada):")
    for row in q1a_traco_dry_run(leituras):
        print(row)

    print("\nQ2 — funcional:")
    print("  comprehension:", q2a_comprehension([7, 8, 8.5, 11, 12]))
    print("  filter+map   :", q2b_filter_map([7, 8, 8.5, 11, 12]))

    print("\nQ3 — POO:")
    # monta cenário simples
    u101 = Unidade("101")
    u102 = Unidade("102")

    u101.adicionar_medicao(Medicao("2025-02", 9.2, 150))
    u102.adicionar_medicao(Medicao("2025-02", 11.5, 175))
    u101.adicionar_medicao(
        Medicao("2025-03", 8.9, 140)
    )  # mês diferente só para mostrar filtragem

    unidades = [u101, u102]

    # Critério proporcional (ex.: R$ 5/m³ de água e R$ 0.9/kWh)
    criterio_prop = CobrancaProporcional(tarifa_agua=5.0, tarifa_energia=0.9)
    fatura_prop = Fatura("2025-02", unidades, criterio_prop)
    print("  Proporcional:", fatura_prop.total_por_unidade())

    # Critério rateio fixo (ex.: R$ 1000 para o mês, divide entre unidades ativas)
    criterio_rateio = CobrancaRateioFixo(
        total_mes=1000.0, todas_unidades=unidades, mes="2025-02"
    )
    fatura_rateio = Fatura("2025-02", unidades, criterio_rateio)
    print("  Rateio fixo :", fatura_rateio.total_por_unidade())
