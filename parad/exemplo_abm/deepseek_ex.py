import numpy as np
import matplotlib.pyplot as plt
import random
import time


class Agente:
    def __init__(self, id, tipo, genero):
        self.id = id
        self.tipo = tipo  # 'cliente', 'cozinheiro', 'atendente', 'seguranca', 'gerente'
        self.genero = genero
        self.forca = random.randint(1, 10)
        self.reflexo = random.randint(1, 10)
        self.constituicao = random.randint(1, 10)
        self.agilidade = random.randint(1, 10)
        self.velocidade = random.randint(1, 10)
        self.dinheiro = random.randint(20, 100) if tipo == "cliente" else 0
        self.nivel_alcool = 0
        self.feliz = True
        self.localizacao = None
        self.tempo_estadia = 0

    def consumir_bebida(self, tipo_bebida):
        if tipo_bebida == "alcoolica":
            self.nivel_alcool += random.uniform(0.1, 0.3)
            # Reduz atributos conforme fica bêbado
            self.reflexo = max(1, self.reflexo - 0.1)
            self.agilidade = max(1, self.agilidade - 0.1)
        else:
            self.nivel_alcool = max(0, self.nivel_alcool - 0.05)

    def esta_bebado(self):
        return self.nivel_alcool > 2.0

    def causar_confusao(self):
        return self.esta_bebado() and random.random() < 0.3

    def pode_ser_furtado(self):
        return self.dinheiro > 0 and not self.esta_bebado()


class Taberna:
    def __init__(self):
        self.horario_atual = 16  # 16:00 - início do expediente
        self.agentes = []
        self.mesas = [{"capacidade": 6, "ocupantes": []} for _ in range(6)]
        self.balcão = [None] * 12
        self.quartos_individual = [None] * 4
        self.quartos_coletivo = [[] for _ in range(4)]
        self.pessoas_em_pe = 0
        self.max_pessoas_em_pe = 8
        self.fechada = False
        self.incidentes = []

        # Menu
        self.pratos_cozinheiro1 = [
            "Feijoada",
            "Churrasco",
            "Lasanha",
            "Pizza",
            "Hambúrguer",
            "Salada",
        ]
        self.pratos_cozinheiro2 = [
            "Sushi",
            "Risotto",
            "Pasta",
            "Curry",
            "Tacos",
            "Ceviche",
        ]
        self.bebidas_alcoolicas = [
            "Cerveja",
            "Vinho",
            "Whisky",
            "Vodka",
            "Gin",
            "Rum",
            "Tequila",
        ]
        self.bebidas_nao_alcoolicas = ["Suco", "Refrigerante", "Água", "Café", "Chá"]

        # Inicializar funcionários
        self.inicializar_funcionarios()

    def inicializar_funcionarios(self):
        # Cozinheiros
        self.agentes.append(Agente(1, "cozinheiro", "homem"))
        self.agentes.append(Agente(2, "cozinheiro", "mulher"))

        # Atendentes
        for i in range(4):
            self.agentes.append(Agente(3 + i, "atendente", "mulher"))

        # Seguranças
        for i in range(2):
            self.agentes.append(Agente(7 + i, "seguranca", "homem"))

        # Gerentes (casal)
        self.agentes.append(Agente(9, "gerente", "homem"))
        self.agentes.append(Agente(10, "gerente", "mulher"))

    def calcular_lotação_atual(self):
        total = 0
        # Mesas
        for mesa in self.mesas:
            total += len(mesa["ocupantes"])
        # Balcão
        total += sum(1 for lugar in self.balcão if lugar is not None)
        # Quartos individuais
        total += sum(1 for quarto in self.quartos_individual if quarto is not None)
        # Quartos coletivos
        for quarto in self.quartos_coletivo:
            total += len(quarto)
        # Pessoas em pé
        total += self.pessoas_em_pe

        return total

    def calcular_capacidade_maxima(self):
        capacidade_mesas = sum(mesa["capacidade"] for mesa in self.mesas)
        capacidade_balcao = len(self.balcão)
        capacidade_quartos_ind = len(self.quartos_individual)
        capacidade_quartos_col = sum(4 for _ in self.quartos_coletivo)

        return (
            capacidade_mesas
            + capacidade_balcao
            + capacidade_quartos_ind
            + capacidade_quartos_col
            + self.max_pessoas_em_pe
        )

    def fluxo_clientes(self):
        """Calcula quantos clientes chegam baseado no horário"""
        hora = self.horario_atual

        if 16 <= hora <= 18:  # Início da noite
            return random.randint(1, 3)
        elif 19 <= hora <= 22:  # Pico
            return random.randint(3, 6)
        elif 23 <= hora <= 1:  # Fim de semana
            return random.randint(2, 4)
        else:  # Última hora
            return random.randint(0, 2)

    def adicionar_cliente(self):
        if self.fechada:
            return None

        capacidade_atual = self.calcular_lotação_atual()
        capacidade_maxima = self.calcular_capacidade_maxima()

        # Gerentes controlam fluxo (10% de tolerância)
        if capacidade_atual >= capacidade_maxima * 1.1:
            return None

        novo_id = len(self.agentes) + 1
        genero = random.choice(["homem", "mulher"])
        cliente = Agente(novo_id, "cliente", genero)
        self.agentes.append(cliente)

        # Tentar alocar em algum lugar
        self.alocar_cliente(cliente)

        return cliente

    def alocar_cliente(self, cliente):
        # Tentar mesa primeiro
        for mesa in self.mesas:
            if len(mesa["ocupantes"]) < mesa["capacidade"]:
                mesa["ocupantes"].append(cliente)
                cliente.localizacao = "mesa"
                return

        # Tentar balcão
        for i, lugar in enumerate(self.balcão):
            if lugar is None:
                self.balcão[i] = cliente
                cliente.localizacao = "balcao"
                return

        # Tentar quarto individual
        for i, quarto in enumerate(self.quartos_individual):
            if quarto is None:
                self.quartos_individual[i] = cliente
                cliente.localizacao = "quarto_individual"
                return

        # Tentar quarto coletivo
        for quarto in self.quartos_coletivo:
            if len(quarto) < 4:
                quarto.append(cliente)
                cliente.localizacao = "quarto_coletivo"
                return

        # Ficar em pé
        if self.pessoas_em_pe < self.max_pessoas_em_pe:
            self.pessoas_em_pe += 1
            cliente.localizacao = "em_pe"

    def simular_consumo(self):
        for agente in self.agentes:
            if agente.tipo == "cliente":
                # Clientes consomem bebidas
                if random.random() < 0.6:  # 60% de chance de consumir
                    tipo_bebida = random.choice(["alcoolica", "nao_alcoolica"])
                    if tipo_bebida == "alcoolica":
                        custo = random.randint(5, 20)
                    else:
                        custo = random.randint(2, 8)

                    if agente.dinheiro >= custo:
                        agente.dinheiro -= custo
                        agente.consumir_bebida(tipo_bebida)

    def verificar_incidentes(self):
        clientes = [a for a in self.agentes if a.tipo == "cliente"]

        for cliente in clientes:
            # Verificar se causa confusão
            if cliente.causar_confusao():
                self.incidentes.append(f"Cliente {cliente.id} causou confusão!")
                # Seguranças intervêm
                segurancas = [a for a in self.agentes if a.tipo == "seguranca"]
                if segurancas:
                    seguranca = random.choice(segurancas)
                    if seguranca.forca > cliente.forca * 0.7:
                        self.expulsar_cliente(cliente)
                        self.incidentes.append(
                            f"Segurança {seguranca.id} expulsou cliente {cliente.id}"
                        )

            # Tentativa de furto
            if random.random() < 0.05 and cliente.pode_ser_furtado():
                vitima = random.choice(
                    [c for c in clientes if c != cliente and c.pode_ser_furtado()]
                )
                if vitima:
                    valor_roubado = min(vitima.dinheiro, random.randint(5, 30))
                    vitima.dinheiro -= valor_roubado
                    cliente.dinheiro += valor_roubado
                    self.incidentes.append(
                        f"Cliente {cliente.id} roubou R${valor_roubado} do cliente {vitima.id}"
                    )

    def expulsar_cliente(self, cliente):
        # Remover de todas as localizações
        for mesa in self.mesas:
            if cliente in mesa["ocupantes"]:
                mesa["ocupantes"].remove(cliente)

        for i, lugar in enumerate(self.balcão):
            if lugar == cliente:
                self.balcão[i] = None

        for i, quarto in enumerate(self.quartos_individual):
            if quarto == cliente:
                self.quartos_individual[i] = None

        for quarto in self.quartos_coletivo:
            if cliente in quarto:
                quarto.remove(cliente)

        if cliente.localizacao == "em_pe":
            self.pessoas_em_pe -= 1

        self.agentes.remove(cliente)

    def avancar_horario(self):
        self.horario_atual += 1
        if self.horario_atual >= 24:
            self.horario_atual = 0

        # Fechar às 2h
        if self.horario_atual == 2:
            self.fechada = True

        # Atualizar tempo de estadia dos clientes
        for agente in self.agentes:
            if agente.tipo == "cliente":
                agente.tempo_estadia += 1
                # Clientes podem sair voluntariamente
                if agente.tempo_estadia > random.randint(2, 6):
                    if random.random() < 0.3:
                        self.expulsar_cliente(agente)


class Simulador:
    def __init__(self):
        self.taberna = Taberna()
        self.historico_lotacao = []
        self.historico_clientes = []
        self.historico_incidentes = []

    def executar_simulacao(self, horas=10):
        print("Iniciando simulação da Taberna...")

        for passo in range(horas):
            hora_atual = (self.taberna.horario_atual + passo) % 24

            print(f"\n--- Hora: {hora_atual:02d}:00 ---")

            # Fluxo de clientes
            if not self.taberna.fechada:
                novos_clientes = self.taberna.fluxo_clientes()
                for _ in range(novos_clientes):
                    self.taberna.adicionar_cliente()

            # Simular consumo
            self.taberna.simular_consumo()

            # Verificar incidentes
            self.taberna.verificar_incidentes()

            # Coletar estatísticas
            lotacao_atual = self.taberna.calcular_lotação_atual()
            num_clientes = len([a for a in self.taberna.agentes if a.tipo == "cliente"])

            self.historico_lotacao.append(lotacao_atual)
            self.historico_clientes.append(num_clientes)
            self.historico_incidentes.append(len(self.taberna.incidentes))

            print(f"Clientes na taberna: {num_clientes}")
            print(f"Lotacao atual: {lotacao_atual}")
            print(f"Incidentes hoje: {len(self.taberna.incidentes)}")

            # Mostrar últimos incidentes
            if self.taberna.incidentes[-3:]:
                print("Últimos incidentes:")
                for incidente in self.taberna.incidentes[-3:]:
                    print(f"  - {incidente}")

            time.sleep(0.5)

    def plotar_resultados(self):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

        # Gráfico de lotação
        ax1.plot(self.historico_lotacao)
        ax1.set_title("Lotação da Taberna")
        ax1.set_xlabel("Horas")
        ax1.set_ylabel("Número de Pessoas")
        ax1.grid(True)

        # Gráfico de clientes
        ax2.plot(self.historico_clientes)
        ax2.set_title("Número de Clientes")
        ax2.set_xlabel("Horas")
        ax2.set_ylabel("Clientes")
        ax2.grid(True)

        # Gráfico de incidentes acumulados
        ax3.plot(np.cumsum(self.historico_incidentes))
        ax3.set_title("Incidentes Acumulados")
        ax3.set_xlabel("Horas")
        ax3.set_ylabel("Total de Incidentes")
        ax3.grid(True)

        # Distribuição de localizações
        locais = ["Mesas", "Balcão", "Quartos Ind.", "Quartos Col.", "Em Pé"]
        contagem = [
            sum(len(mesa["ocupantes"]) for mesa in self.taberna.mesas),
            sum(1 for lugar in self.taberna.balcão if lugar is not None),
            sum(1 for quarto in self.taberna.quartos_individual if quarto is not None),
            sum(len(quarto) for quarto in self.taberna.quartos_coletivo),
            self.taberna.pessoas_em_pe,
        ]

        ax4.bar(locais, contagem)
        ax4.set_title("Distribuição por Localização")
        ax4.set_ylabel("Número de Pessoas")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


# Exemplo de uso
if __name__ == "__main__":
    simulador = Simulador()
    simulador.executar_simulacao(horas=10)
    simulador.plotar_resultados()

    # Mostrar estatísticas finais
    print("\n=== ESTATÍSTICAS FINAIS ===")
    print(f"Total de incidentes: {len(simulador.taberna.incidentes)}")
    print(f"Máxima lotação: {max(simulador.historico_lotacao)}")
    print(f"Clientes atendidos: {sum(simulador.historico_clientes)}")
