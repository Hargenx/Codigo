# taverna.py
from config import HORA_ABERTURA, CAPACIDADE_MAXIMA, HORA_FECHAMENTO
import numpy as np


class Taverna:
    """
    Representa o ambiente da simulação.
    Controla a entrada, saída e o estado geral.
    """

    def __init__(self):
        self.capacidade_maxima = CAPACIDADE_MAXIMA
        self.agentes_presentes = []
        self.aberta = False

        # Listas para processar entradas e saídas ao final do 'tick'
        self.lista_saida = []
        self.lista_expulsos = []

    def step(self, minuto_atual):
        """
        O 'step' do ambiente. Controla o horário de funcionamento
        e chama o 'step' de cada agente dentro dele.
        """
        hora_atual_float = HORA_ABERTURA + (minuto_atual / 60)

        # --- Regra 1: Horário de Funcionamento ---
        if HORA_ABERTURA <= hora_atual_float < HORA_FECHAMENTO:
            self.aberta = True
        else:
            self.aberta = False

        # --- Regra 2: Ação dos Agentes ---
        # Se a taverna estiver aberta, os agentes agem
        if self.aberta:
            for agente in self.agentes_presentes:
                agente.step(self)  # Passa o 'self' (a taverna) como ambiente
        else:
            # Se fechou, todos são forçados a sair
            for agente in self.agentes_presentes:
                agente.estado = "saindo"

        # --- Regra 3: Processar Saídas ---
        # Limpamos as listas de quem saiu no final do 'tick'
        # Isso evita erros de modificar a lista enquanto iteramos sobre ela
        self.lista_saida = [a for a in self.agentes_presentes if a.estado == "saindo"]
        self.lista_expulsos = [
            a for a in self.agentes_presentes if a.estado == "expulso"
        ]

        self.agentes_presentes = [
            a
            for a in self.agentes_presentes
            if a.estado != "saindo" and a.estado != "expulso"
        ]

    def tentar_adicionar_agente(self, agente):
        """Tenta adicionar um novo agente ao ambiente."""
        if self.aberta and len(self.agentes_presentes) < self.capacidade_maxima:
            self.agentes_presentes.append(agente)
            return True
        else:
            # print("Taverna cheia! Agente não pode entrar.")
            return False

    def get_lotacao(self):
        """Retorna o número atual de agentes."""
        return len(self.agentes_presentes)

    def get_nivel_alcool_medio(self):
        """Calcula o nível de álcool médio (usa NumPy!)."""
        if not self.agentes_presentes:
            return 0
        niveis = [a.nivel_alcool for a in self.agentes_presentes]
        return np.mean(niveis)
