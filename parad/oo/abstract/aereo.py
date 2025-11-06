"""
Módulo aereo
Define a classe Aereo, que especializa Transporte.
"""

from __future__ import annotations
from typing import Optional
from transporte import Transporte


class Aereo(Transporte):
    """
    Meio de transporte aéreo.

    Atributos específicos:
        rota (int): código/identificador da rota aérea.
    """

    def __init__(
        self,
        combustivel: int,
        identificador: int,
        velocidade: int,
        rota: int,
    ) -> None:
        super().__init__(combustivel, identificador, velocidade)
        self._rota = rota
        self._altitude_atual: Optional[int] = None  # metros

    @property
    def rota(self) -> int:
        """Retorna o código da rota."""
        return self._rota

    def mover(self) -> None:
        """
        Implementação específica do movimento aéreo.
        Exemplo simples: ajustar altitude e "voar".
        """
        # lógica fictícia só pra dar contexto
        if self.combustivel <= 0:
            print(f"[Aereo {self.identificador}] Sem combustível para decolar.")
            return

        if self._altitude_atual is None:
            self._altitude_atual = 1000  # decolou
            print(
                f"[Aereo {self.identificador}] Decolando na rota {self._rota}, "
                f"subindo para {self._altitude_atual} m a {self.velocidade} km/h."
            )
        else:
            self._altitude_atual += 500
            print(
                f"[Aereo {self.identificador}] Mantendo rota {self._rota}, "
                f"subindo para {self._altitude_atual} m a {self.velocidade} km/h."
            )
