"""
Módulo transporte
Define a classe base abstrata Transporte.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Transporte(ABC):
    """
    Classe base para qualquer meio de transporte.

    Atributos:
        combustivel (int): quantidade atual de combustível (em % ou litros).
        identificador (int): código único do veículo.
        velocidade (int): velocidade atual em km/h.
    """

    def __init__(self, combustivel: int, identificador: int, velocidade: int) -> None:
        self._combustivel = combustivel
        self._identificador = identificador
        self._velocidade = velocidade

    @property
    def combustivel(self) -> int:
        """Retorna a quantidade de combustível."""
        return self._combustivel

    @property
    def identificador(self) -> int:
        """Retorna o identificador único do transporte."""
        return self._identificador

    @property
    def velocidade(self) -> int:
        """Retorna a velocidade atual do transporte."""
        return self._velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade: int) -> None:
        """Atualiza a velocidade atual do transporte."""
        if nova_velocidade < 0:
            raise ValueError("Velocidade não pode ser negativa.")
        self._velocidade = nova_velocidade

    @abstractmethod
    def mover(self) -> None:
        """
        Executa a lógica de movimento do transporte.
        Deve ser implementado pelas subclasses.
        """
        pass

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self._identificador}, "
            f"velocidade={self._velocidade}, combustivel={self._combustivel})"
        )
