class Transporte:
    """
    Classe base para qualquer transporte.
    """

    def __init__(self, combustivel, identificador, velocidade):
        self.combustivel = combustivel  # quantidade de combustível
        self.identificador = identificador  # id único
        self.velocidade = velocidade  # km/h

    def mover(self):
        """
        'Contrato' genérico de movimento.
        A intenção é que as subclasses sobrescrevam este método.
        """
        print("Metodo mover() da classe Transporte. Deve ser sobrescrito.")

    def resumo(self):
        """
        Método comum a todos os transportes.
        Não é polimórfico, só reaproveitado por herança.
        """
        return (
            f"[id={self.identificador}] "
            f"vel={self.velocidade}km/h "
            f"combustível={self.combustivel}"
        )
