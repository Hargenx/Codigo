class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Extrato:
    """
    O extrato pertence à conta. Ele guarda o histórico de operações.
    Essa classe NÃO faz sentido existir sem uma Conta.
    """

    def __init__(self):
        self.movimentos = []  # lista de strings

    def registrar(self, descricao):
        self.movimentos.append(descricao)

    def mostrar(self):
        print("=== EXTRATO ===")
        for linha in self.movimentos:
            print(linha)
        print("===============")


class Conta:
    """
    A Conta agrega Cliente (agregação) e compõe Extrato (composição).
    """

    def __init__(self, numero, clientes_iniciais=None):
        self.numero = numero
        self.saldo = 0.0

        # Agregação:
        # Recebemos objetos Cliente que já existem fora da classe Conta.
        # (um cliente pode ter várias contas, por exemplo)
        if clientes_iniciais is None:
            self.clientes = []
        else:
            self.clientes = list(clientes_iniciais)

        # Composição:
        # A Conta cria o seu próprio Extrato.
        # Esse Extrato "nasce" junto com a conta e é controlado por ela.
        self.extrato = Extrato()
        self.extrato.registrar(
            f"Conta {self.numero} criada com saldo inicial {self.saldo:.2f}."
        )

    def adicionar_cliente(self, cliente):
        """Associa mais um cliente a esta conta."""
        self.clientes.append(cliente)
        self.extrato.registrar(
            f"Cliente {cliente.nome} (CPF {cliente.cpf}) vinculado à conta."
        )

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return
        self.saldo += valor
        self.extrato.registrar(
            f"Depósito de {valor:.2f}. Saldo atual: {self.saldo:.2f}."
        )

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        self.extrato.registrar(f"Saque de {valor:.2f}. Saldo atual: {self.saldo:.2f}.")

    def mostrar_dados(self):
        print("=== CONTA ===")
        print(f"Número: {self.numero}")
        print(f"Saldo:  {self.saldo:.2f}")
        print("Clientes vinculados:")
        for c in self.clientes:
            print(f" - {c}")
        print("=============")

    def mostrar_extrato(self):
        self.extrato.mostrar()

if __name__ == "__main__":
    # Cria alguns clientes
    cliente1 = Cliente("123.456.789-00", "Raphael jesus", "Rua A, 123")
    cliente2 = Cliente("456.789.123-00", "Caroline Santos", "Rua B, 456")
    cliente3 = Cliente("789.123.456-00", "Gilson Sanches", "Rua C, 789")

    # Cria uma conta
    conta = Conta(1, [cliente1, cliente2])

    # Mostra os dados da conta
    conta.mostrar_dados()

    # Mostra o histórico de operações
    conta.mostrar_extrato()

    # Deposita
    conta.depositar(100.00)
    conta.mostrar_dados()
    conta.mostrar_extrato()

    # Saca
    conta.sacar(50.00)
    conta.mostrar_dados()
    conta.mostrar_extrato()

    # Adiciona um cliente
    conta.adicionar_cliente(cliente3)
    conta.mostrar_dados()
    conta.mostrar_extrato()  # o extrato é o mesmo