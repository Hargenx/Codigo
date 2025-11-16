from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Iterable, List


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
    pelo menos uma medição no mês (unidades 'ativas').
    """

    def __init__(
        self, total_mes: float, todas_unidades: Iterable[Unidade], mes: str
    ) -> None:
        self.total_mes = total_mes
        self._ativas = [u for u in todas_unidades if u.medicoes_do_mes(mes)]
        if not self._ativas:
            raise ValueError("Nenhuma unidade ativa no mês para rateio.")

    def calcular(self, unidade: Unidade, mes: str) -> float:
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
