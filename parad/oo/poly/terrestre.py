from transporte import Transporte


class Terrestre(Transporte):
    """
    Transporte terrestre (carro, ônibus, moto etc).
    """

    def __init__(self, combustivel, identificador, velocidade, abs_nivel):
        # Reaproveita atributos comuns
        super().__init__(combustivel, identificador, velocidade)
        self.abs_nivel = abs_nivel  # ex.: 0 = sem ABS, 1 = básico, 2 = avançado
        self.distancia = 0  # km já percorridos

    def mover(self):
        """
        Implementação específica para transporte terrestre.
        Sobrescreve mover() da classe Transporte.
        """
        if self.combustivel <= 0:
            print(f"Terrestre {self.identificador}: sem combustível para andar.")
            return

        # anda um pouco
        self.distancia += self.velocidade // 10  # regra simples só pra exemplo
        print(
            f"Terrestre {self.identificador}: rodando a {self.velocidade} km/h, "
            f"ABS nível {self.abs_nivel}, distância total = {self.distancia} km."
        )
