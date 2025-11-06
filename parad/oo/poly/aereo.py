from transporte import Transporte


class Aereo(Transporte):
    """
    Transporte aéreo (avião, helicóptero etc).
    """

    def __init__(self, combustivel, identificador, velocidade, rota):
        super().__init__(combustivel, identificador, velocidade)
        self.rota = rota  # rota/código de voo
        self.altitude = 0  # metros

    def mover(self):
        """
        Implementação específica para transporte aéreo.
        Sobrescreve mover() da classe Transporte.
        """
        if self.combustivel <= 0:
            print(f"Aéreo {self.identificador}: sem combustível para voar.")
            return

        # "Decolar" ou "subir"
        if self.altitude == 0:
            self.altitude = 1000
            print(
                f"Aéreo {self.identificador}: decolando na rota {self.rota}, "
                f"subindo para {self.altitude} m a {self.velocidade} km/h."
            )
        else:
            self.altitude += 500
            print(
                f"Aéreo {self.identificador}: mantendo rota {self.rota}, "
                f"subindo para {self.altitude} m a {self.velocidade} km/h."
            )
