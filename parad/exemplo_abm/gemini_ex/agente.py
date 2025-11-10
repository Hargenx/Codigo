# agente.py
import numpy as np
import random
from config import (DINHEIRO_MIN_INICIAL, DINHEIRO_MAX_INICIAL, PRECO_BEBIDA,
                    ALCOOL_POR_BEBIDA, LIMITE_ALCOOL_CONFUSAO, PROB_CAUSAR_CONFUSAO,
                    PROB_SER_EXPULSO, PROB_IR_EMBORA_NORMAL)  # Importa todas as nossas regras


class Agente:
    """
    Representa um cliente (patron) da taverna.
    Cada agente tem seus próprios atributos e estado.
    """

    def __init__(self, id_agente):
        self.id = id_agente
        self.dinheiro = random.randint(DINHEIRO_MIN_INICIAL, DINHEIRO_MAX_INICIAL)
        self.nivel_alcool = 0.0

        # Usando NumPy para os atributos (Força, Reflexo, Const, Agil, Vel)
        self.atributos = np.array([random.randint(5, 15) for _ in range(5)])

        # Estado atual do agente
        self.estado = "consumindo"  # Pode ser 'consumindo', 'saindo', 'expulso'

    def step(self, ambiente):
        """
        Esta é a "função de decisão" do agente, chamada a cada "tick" (minuto).
        """
        # Se o agente já decidiu sair ou foi expulso, ele não faz mais nada
        if self.estado == "saindo" or self.estado == "expulso":
            return

        # --- Regra 1: Ficar bêbado e causar confusão ---
        if self.nivel_alcool > LIMITE_ALCOOL_CONFUSAO:
            if random.random() < PROB_CAUSAR_CONFUSAO:
                self.causar_confusao(ambiente)

        # --- Regra 2: Decidir consumir ---
        # Chance de 5% a cada minuto de pedir uma bebida
        if random.random() < 0.05 and self.dinheiro >= PRECO_BEBIDA:
            self.beber()

        # --- Regra 3: Decidir ir embora ---
        # Vai embora se o dinheiro acabar, ou se ficar muito bêbado, ou por chance aleatória
        if (
            self.dinheiro < PRECO_BEBIDA
            or self.nivel_alcool > 8.0
            or random.random() < PROB_IR_EMBORA_NORMAL
        ):
            self.estado = "saindo"
            # print(f"Agente {self.id} decidiu ir embora.")

    def beber(self):
        """Ação de beber: gasta dinheiro, aumenta álcool, afeta atributos."""
        self.dinheiro -= PRECO_BEBIDA
        self.nivel_alcool += ALCOOL_POR_BEBIDA

        # Álcool afeta atributos (ex: diminui reflexo e agilidade)
        self.atributos[1] *= 0.98  # Reflexo
        self.atributos[3] *= 0.98  # Agilidade
        # print(f"Agente {self.id} bebeu. Nível álcool: {self.nivel_alcool:.1f}")

    def causar_confusao(self, ambiente):
        """Ação de causar confusão (STUB)."""
        # print(f"AgAnTe {self.id} EsTÁ cAusAnDO CoNfUsÃo! (Álcool: {self.nivel_alcool:.1f})")

        # A "regra do segurança" é implementada aqui, como uma reação do ambiente
        if random.random() < PROB_SER_EXPULSO:
            # print(f"Seguranças viram e expulsaram o Agente {self.id}!")
            self.estado = "expulso"

    # --- Funções que os alunos podem implementar ---
    # def furtar(self, outro_agente):
    #    pass
    #
    # def brigar(self, outro_agente):
    #    pass
