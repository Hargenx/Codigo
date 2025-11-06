"""
Demonstração de polimorfismo:
- Temos uma lista de Transportes (tipo da classe base).
- Cada elemento pode ser Aereo ou Terrestre.
- Chamamos mover() sem precisar saber qual é qual.
"""

from __future__ import annotations
from typing import List
from aereo import Aereo
from terrestre import Terrestre
from transporte import Transporte


def executar_simulacao(frotas: List[Transporte]) -> None:
    """
    Faz todos os transportes da frota se moverem.
    Note que não precisamos diferenciar quem é aéreo e quem é terrestre.
    Isso É o polimorfismo na prática.
    """
    for transporte in frotas:
        transporte.mover()


if __name__ == "__main__":
    aviao = Aereo(
        combustivel=80,
        identificador=101,
        velocidade=750,
        rota=9001,
    )

    carro = Terrestre(
        combustivel=50,
        identificador=202,
        velocidade=100,
        abs=2,
    )

    onibus = Terrestre(
        combustivel=60,
        identificador=303,
        velocidade=60,
        abs=1,
    )

    # Lista polimórfica: todos são Transporte
    frota: List[Transporte] = [aviao, carro, onibus]

    print("=== Rodada 1 ===")
    executar_simulacao(frota)

    print("\n=== Ajustando velocidades e rodando de novo ===")
    carro.velocidade = 120
    aviao.velocidade = 800
    executar_simulacao(frota)
