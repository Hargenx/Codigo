from aereo import Aereo
from terrestre import Terrestre


def executar_simulacao(frota: list) -> None:
    """
    Recebe vários objetos diferentes, mas todos "sabem se mover".
    A função não precisa saber se é Aereo ou Terrestre.
    ISSO é polimorfismo.
    """
    for transporte in frota:
        transporte.mover()


if __name__ == "__main__":
    aviao = Aereo(combustivel=80, identificador=101, velocidade=750, rota=9001)

    carro = Terrestre(combustivel=50, identificador=202, velocidade=100, abs_nivel=2)

    onibus = Terrestre(combustivel=60, identificador=303, velocidade=60, abs_nivel=1)

    # Lista polimórfica: objetos de classes diferentes, todos tratados como "transporte"
    frota = [aviao, carro, onibus]

    print("=== Rodada 1 ===")
    executar_simulacao(frota)

    print("\n=== Rodada 2 ===")
    carro.velocidade = 120
    aviao.velocidade = 800
    executar_simulacao(frota)
