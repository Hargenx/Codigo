from exceptions import SaldoInsuficienteError, ValorInvalidoError
from conta import Conta


class ContaEspecial(Conta):
    """
    Conta Especial:
    - Pode permitir saque acima do saldo, até um limite de crédito.
    """

    def __init__(
        self, numero: int, saldo_inicial: float = 0.0, limite: float = 1000.0
    ) -> None:
        super().__init__(numero, saldo_inicial)

        if limite < 0:
            raise ValorInvalidoError("Limite não pode ser negativo.")

        self._limite = float(limite)

    @property
    def limite(self) -> float:
        """Retorna o limite especial (espécie de cheque especial)."""
        return self._limite

    def sacar(self, valor: float) -> None:
        """
        Polimorfismo:
        - Sobrescreve (override) o sacar() da classe mãe.
        - Aqui, a ContaEspecial pode sacar até saldo + limite.
        """
        if valor <= 0:
            raise ValorInvalidoError("Saque deve ser maior que zero.")

        saldo_disponivel = self._saldo + self._limite

        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(
                "Saldo insuficiente, mesmo considerando o limite especial."
            )

        # Saca normalmente (pode deixar saldo negativo)
        self._saldo -= valor

    def gerar_saldo(self) -> str:
        """
        Polimorfismo de novo:
        - Mesma ideia de gerar_saldo() da classe mãe,
          mas incluindo informações de limite e saldo disponível total.
        """
        abertura_str = self.data_abertura.strftime("%d/%m/%Y %H:%M:%S")
        saldo_disponivel = self._saldo + self._limite
        return (
            f"Conta Especial {self.numero}\n"
            f"Abertura: {abertura_str}\n"
            f"Saldo atual: R$ {self.saldo:,.2f}\n"
            f"Limite: R$ {self._limite:,.2f}\n"
            f"Saldo disponível total: R$ {saldo_disponivel:,.2f}"
        )
