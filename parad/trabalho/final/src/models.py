from typing import List


class Produto:
    """Representa um produto do cardápio do restaurante."""

    def __init__(self, nome: str, preco: float) -> None:
        if not nome:
            raise ValueError("Nome do produto não pode ser vazio.")
        if preco < 0:
            raise ValueError("Preço do produto não pode ser negativo.")

        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"{self.nome} (R$ {self.preco:.2f})"

    def __repr__(self) -> str:
        return f"Produto(nome={self.nome!r}, preco={self.preco!r})"


class Pedido:
    """Representa um pedido realizado no restaurante."""

    def __init__(self, id_pedido: int, produtos: List[Produto]) -> None:
        if id_pedido <= 0:
            raise ValueError("id_pedido deve ser positivo.")
        if not produtos:
            raise ValueError("Um pedido deve conter pelo menos um produto.")

        self.id_pedido = id_pedido
        self.produtos = produtos

    def valor_total(self) -> float:
        """Retorna a soma dos preços de todos os produtos do pedido."""
        return sum(produto.preco for produto in self.produtos)

    def __str__(self) -> str:
        return f"Pedido #{self.id_pedido} - {len(self.produtos)} itens - Total R$ {self.valor_total():.2f}"
