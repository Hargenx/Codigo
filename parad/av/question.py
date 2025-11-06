from __future__ import annotations
from typing import List, Tuple


class Conta:
    taxa: float = 0.01  # taxa global de operação

    def __init__(
        self,
        titular: str,
        saldo: float = 0.0,
        historico: List[Tuple[str, float]] | None = None,
    ) -> None:
        if saldo < 0:
            raise ValueError("Saldo inicial não pode ser negativo")
        self.titular = titular
        self._saldo = float(saldo)
        self.historico = [] if historico is None else list(historico)

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = float(valor)

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo")
        taxa = type(self).taxa
        self._saldo += valor * (1 - taxa)
        self.historico.append(("dep", valor))

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Saque deve ser positivo")
        taxa = type(self).taxa
        total = valor * (1 + taxa)
        if total > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= total
        self.historico.append(("saq", valor))

    @classmethod
    def definir_taxa(cls, nova_taxa: float) -> None:
        if not (0.0 <= nova_taxa <= 0.1):
            raise ValueError("Taxa fora do intervalo permitido")
        cls.taxa = float(nova_taxa)
