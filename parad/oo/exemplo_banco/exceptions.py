class SaldoInsuficienteError(Exception):
    """Lançada quando não há saldo (ou limite) suficiente para a operação."""

    pass


class ValorInvalidoError(Exception):
    """Lançada quando é informado um valor inválido (<= 0, por exemplo)."""

    pass
