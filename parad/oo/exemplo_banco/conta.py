from datetime import datetime
from exceptions import SaldoInsuficienteError, ValorInvalidoError


class Conta:
    """
    Representa uma conta bancária genérica.

    Atributos:
        numero (int): número identificador da conta.
        saldo (float): saldo atual.
        data_abertura (datetime): data e hora de criação da conta.
    """

    def __init__(self, numero: int, saldo_inicial: float = 0.0) -> None:
        if saldo_inicial < 0:
            raise ValorInvalidoError("Saldo inicial não pode ser negativo.")

        self._numero = numero
        self._saldo = float(saldo_inicial)
        self._data_abertura = datetime.now()

    # ---------- Propriedades (encapsulamento pythonico) ----------

    @property
    def numero(self) -> int:
        """Número da conta (somente leitura)."""
        return self._numero

    @property
    def saldo(self) -> float:
        """Saldo atual da conta (somente leitura pública)."""
        return self._saldo

    @property
    def data_abertura(self) -> datetime:
        """Data de abertura da conta."""
        return self._data_abertura

    # ---------- Métodos de negócio ----------

    def depositar(self, valor: float) -> None:
        """
        Deposita um valor na conta.
        Levanta ValorInvalidoError se valor <= 0.
        """
        if valor <= 0:
            raise ValorInvalidoError("Depósito deve ser maior que zero.")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        """
        Saca um valor da conta.
        Levanta:
            ValorInvalidoError se valor <= 0
            SaldoInsuficienteError se saldo for insuficiente
        """
        if valor <= 0:
            raise ValorInvalidoError("Saque deve ser maior que zero.")

        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para saque.")

        self._saldo -= valor

    def transfere_valor(self, destino: "Conta", valor: float) -> None:
        """
        Transfere 'valor' desta conta para outra conta (destino).
        Usa sacar() e depositar() para respeitar regras e validações.
        """
        if not isinstance(destino, Conta):
            raise TypeError("Destino deve ser uma instância de Conta.")

        self.sacar(valor)
        destino.depositar(valor)

    def gerar_saldo(self) -> str:
        """
        Retorna uma string amigável com os dados essenciais da conta.
        """
        abertura_str = self._data_abertura.strftime("%d/%m/%Y %H:%M:%S")
        return (
            f"Conta {self._numero}\n"
            f"Abertura: {abertura_str}\n"
            f"Saldo atual: R$ {self._saldo:,.2f}"
        )

    # ---------- Métodos especiais / operadores ----------

    def __add__(self, other: "Conta") -> float:
        """
        Soma os saldos de duas contas.
        Exemplo: total = conta1 + conta2
        """
        if not isinstance(other, Conta):
            return NotImplemented
        return self._saldo + other._saldo

    def __repr__(self) -> str:
        """Representação útil para debug/logging."""
        cls = self.__class__.__name__
        return f"{cls}(numero={self._numero}, saldo={self._saldo:.2f})"

    def __str__(self) -> str:
        """
        Representação amigável para print().
        Usa gerar_saldo() internamente.
        """
        return self.gerar_saldo()
