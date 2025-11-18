from typing import List

from models import Produto, Pedido


def criar_pedidos_exemplo() -> List[Pedido]:
    """
    Cria alguns pedidos de exemplo para o restaurante.
    Alguns produtos se repetem entre os pedidos.
    """

    # Produtos do cardápio
    cafe = Produto("Café expresso", 5.00)
    pao_queijo = Produto("Pão de queijo", 7.50)
    suco_laranja = Produto("Suco de laranja", 9.00)
    prato_executivo = Produto("Prato executivo", 32.00)
    sobremesa = Produto("Pudim de leite", 12.00)
    refrigerante = Produto("Refrigerante lata", 6.00)

    # Pedidos do dia (exemplos)
    pedidos = [
        Pedido(1, [cafe, pao_queijo]),
        Pedido(2, [prato_executivo, suco_laranja]),
        Pedido(3, [cafe, cafe, pao_queijo, sobremesa]),
        Pedido(4, [prato_executivo, sobremesa, refrigerante]),
        Pedido(5, [suco_laranja, pao_queijo]),
    ]

    return pedidos
