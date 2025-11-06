from conta import Conta
from conta_especial import ContaEspecial
from exceptions import SaldoInsuficienteError, ValorInvalidoError


def main() -> None:
    # Criação das contas
    conta_normal = Conta(numero=101, saldo_inicial=500.0)
    conta_especial = ContaEspecial(numero=202, saldo_inicial=100.0, limite=1000.0)

    print("--- Situação inicial ---")
    print(conta_normal)
    print()
    print(conta_especial)
    print()

    # Depósito
    conta_normal.depositar(250.0)

    # Saque normal (conta comum tem que ter saldo suficiente)
    try:
        conta_normal.sacar(900.0)
    except SaldoInsuficienteError as err:
        print(f"[ERRO] Saque na conta normal falhou: {err}")
    print()

    # Saque que usa limite especial (pode deixar saldo negativo)
    try:
        conta_especial.sacar(800.0)  # permitido: 100 saldo + 1000 limite >= 800
    except (ValorInvalidoError, SaldoInsuficienteError) as err:
        print(f"[ERRO] Saque na conta especial falhou: {err}")

    print("--- Depois dos saques ---")
    print(conta_normal)
    print()
    print(conta_especial)
    print()

    # Transferência entre contas
    try:
        # transfere_valor usa sacar() internamente.
        # Se a origem for ContaEspecial, vale a regra especial de saque.
        conta_especial.transfere_valor(destino=conta_normal, valor=200.0)
    except (ValorInvalidoError, SaldoInsuficienteError, TypeError) as err:
        print(f"[ERRO] Transferência falhou: {err}")

    print("--- Depois da transferência ---")
    print(conta_normal)
    print()
    print(conta_especial)
    print()

    # Uso do operador +
    total_saldos = conta_normal + conta_especial
    print(f"Soma dos saldos das contas (operador +): R$ {total_saldos:,.2f}")


if __name__ == "__main__":
    main()
