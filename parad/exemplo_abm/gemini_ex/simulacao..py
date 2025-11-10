# simulacao.py
import matplotlib.pyplot as plt
import random
from config import DURACAO_SIMULACAO_MINUTOS, HORA_ABERTURA, CAPACIDADE_MAXIMA
from agente import Agente
from taverna import Taverna


class Simulacao:
    """
    Controla o 'relógio' (loop principal) e a criação de agentes.
    Coleta dados para visualização.
    """

    def __init__(self):
        self.taverna = Taverna()
        self.total_minutos = DURACAO_SIMULACAO_MINUTOS
        self.proximo_id_agente = 0

        # Listas para guardar os dados para o Matplotlib
        self.historico_lotacao = []
        self.historico_alcool_medio = []
        self.historico_expulsos = []

    def rodar(self):
        """Inicia e executa a simulação minuto a minuto."""
        print(f"Iniciando simulação da Taverna... ({self.total_minutos} minutos)")

        for minuto in range(self.total_minutos):

            # --- 1. Novos Agentes Chegando ---
            # A probabilidade de chegada varia com o horário (Regra de Fluxo)
            hora_atual_float = HORA_ABERTURA + (minuto / 60)
            prob_chegada = self.calcular_prob_chegada(hora_atual_float)

            if random.random() < prob_chegada:
                novo_agente = Agente(self.proximo_id_agente)
                self.proximo_id_agente += 1
                self.taverna.tentar_adicionar_agente(novo_agente)

            # --- 2. O Ambiente "roda" ---
            # O step da taverna vai cuidar de chamar o step de cada agente
            self.taverna.step(minuto)

            # --- 3. Coleta de Dados ---
            self.historico_lotacao.append(self.taverna.get_lotacao())
            self.historico_alcool_medio.append(self.taverna.get_nivel_alcool_medio())
            self.historico_expulsos.append(len(self.taverna.lista_expulsos))

        print("Simulação concluída. Gerando gráficos...")
        self.plotar_resultados()

    def calcular_prob_chegada(self, hora_float):
        """
        Define o fluxo de pessoas (Regra de Negócio).
        Baixo no início, pico às 20h, diminui no final.
        Retorna a PROBABILIDADE POR MINUTO.
        """
        if hora_float < 18:  # 16:00 - 18:00
            return 0.2 / 60  # Baixa
        elif hora_float < 22:  # 18:00 - 22:00
            return 0.8 / 60  # PICO
        elif hora_float < 25:  # 22:00 - 01:00
            return 0.4 / 60  # Média
        else:  # 01:00 - 02:00
            return 0.1 / 60  # Baixa

    def plotar_resultados(self):
        """Usa Matplotlib para mostrar o que aconteceu."""

        # Prepara os eixos do tempo
        tempo_minutos = list(range(self.total_minutos))

        # Cria a figura com 3 subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

        # Gráfico 1: Lotação
        ax1.plot(
            tempo_minutos,
            self.historico_lotacao,
            label="Lotação na Taverna",
            color="blue",
        )
        ax1.axhline(
            y=CAPACIDADE_MAXIMA,
            color="red",
            linestyle="--",
            label=f"Capacidade Máx. ({CAPACIDADE_MAXIMA})",
        )
        ax1.set_ylabel("Nº de Patrons")
        ax1.set_title("Evolução da Lotação da Taverna")
        ax1.legend()
        ax1.grid(True)

        # Gráfico 2: Nível de Álcool
        ax2.plot(
            tempo_minutos,
            self.historico_alcool_medio,
            label="Nível Médio de Álcool",
            color="green",
        )
        ax2.set_ylabel("Nível Médio (0-X)")
        ax2.set_title("Nível Médio de Álcool dos Patrons")
        ax2.legend()
        ax2.grid(True)

        # Gráfico 3: Expulsões
        ax3.bar(
            tempo_minutos,
            self.historico_expulsos,
            label="Patrons Expulsos (por min)",
            color="orange",
        )
        ax3.set_xlabel("Minutos desde a Abertura (16:00)")
        ax3.set_ylabel("Nº de Expulsões")
        ax3.set_title("Eventos de Expulsão (Bêbados)")
        ax3.legend()

        plt.tight_layout()
        plt.show()


# --- Ponto de Entrada Principal ---
if __name__ == "__main__":
    sim = Simulacao()
    sim.rodar()
