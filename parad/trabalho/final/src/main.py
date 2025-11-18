from typing import List

from dados import criar_pedidos_exemplo
from analytics import (
    calcular_faturamento_total,
    calcular_ticket_medio,
    calcular_estatisticas_valores,
    top_produtos_mais_vendidos,
)
from models import Pedido


class Aplicacao:
    """Classe principal da aplicação (menu e interação com o usuário)."""

    def __init__(self, pedidos: List[Pedido]) -> None:
        self.pedidos = pedidos

    def executar(self) -> None:
        """Loop principal do menu."""
        while True:
            self._exibir_menu()

            try:
                opcao_str = input("Escolha uma opção: ")
                opcao = int(opcao_str)
            except ValueError:
                print("Opção inválida: digite um número inteiro.\n")
                continue

            if opcao == 0:
                print("Encerrando o sistema. Até logo!")
                break
            elif opcao == 1:
                self._mostrar_faturamento_total()
            elif opcao == 2:
                self._mostrar_ticket_medio()
            elif opcao == 3:
                self._mostrar_estatisticas()
            elif opcao == 4:
                self._mostrar_top_produtos()
            else:
                print("Opção não reconhecida. Tente novamente.\n")

    @staticmethod
    def _exibir_menu() -> None:
        print("=== Menu Restaurante Bom Prato ===")
        print("1 - Mostrar faturamento total do dia")
        print("2 - Mostrar ticket médio dos pedidos")
        print("3 - Mostrar estatísticas dos valores dos pedidos")
        print("4 - Mostrar top 3 produtos mais vendidos")
        print("0 - Sair")
        print("-" * 40)

    def _mostrar_faturamento_total(self) -> None:
        total = calcular_faturamento_total(self.pedidos)
        print(f"Faturamento total do dia: R$ {total:.2f}\n")

    def _mostrar_ticket_medio(self) -> None:
        ticket = calcular_ticket_medio(self.pedidos)
        print(f"Ticket médio dos pedidos: R$ {ticket:.2f}\n")

    def _mostrar_estatisticas(self) -> None:
        estat = calcular_estatisticas_valores(self.pedidos)
        print("Estatísticas dos valores dos pedidos:")
        print(f"  Valor mínimo: R$ {estat['minimo']:.2f}")
        print(f"  Valor máximo: R$ {estat['maximo']:.2f}")
        print(f"  Valor médio:  R$ {estat['media']:.2f}\n")

    def _mostrar_top_produtos(self) -> None:
        top = top_produtos_mais_vendidos(self.pedidos, n=3)
        print("Top 3 produtos mais vendidos:")
        if not top:
            print("  Nenhum produto encontrado.\n")
            return

        for nome, qtd in top:
            print(f"  {nome}: {qtd}x")
        print()


def main() -> None:
    pedidos = criar_pedidos_exemplo()
    app = Aplicacao(pedidos)
    app.executar()


if __name__ == "__main__":
    main()
