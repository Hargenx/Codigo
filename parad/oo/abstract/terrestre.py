"""
Módulo terrestre
Define a classe Terrestre, que especializa Transporte.
"""

from __future__ import annotations
from transporte import Transporte


class Terrestre(Transporte):
    """
    Meio de transporte terrestre.

    Atributos específicos:
        abs (int): nível/versão do sistema de freio ABS (ex: 0=sem ABS).
    """

    def __init__(
        self,
        combustivel: int,
        identificador: int,
        velocidade: int,
        abs: int,
    ) -> None:
        super().__init__(combustivel, identificador, velocidade)
        self._abs = abs
        self._distancia_percorrida = 0  # km

    @property
    def abs(self) -> int:
        """Retorna o nível/versão do ABS."""
        return self._abs

    @property
    def distancia_percorrida(self) -> int:
        """Retorna a distância total percorrida em km."""
        return self._distancia_percorrida

    def mover(self) -> None:
        """
        Implementação específica do movimento terrestre.
        Exemplo simples: andar um pouco e acumular distância.
        """
        if self.combustivel <= 0:
            print(f"[Terrestre {self.identificador}] Sem combustível para andar.")
            return

        self._distancia_percorrida += self.velocidade // 10  # regra fictícia
        print(
            f"[Terrestre {self.identificador}] Rodando a {self.velocidade} km/h "
            f"({self._distancia_percorrida} km totais). ABS nível {self._abs} ativo."
        )
