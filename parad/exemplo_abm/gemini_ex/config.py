# config.py
# Arquivo para guardar todas as "regras" e constantes da simulação

# Regras da Taverna
CAPACIDADE_MAXIMA = (6 * 6) + 12 + 8  # 6 mesas * 6 lug + 12 balcão + 8 em pé = 56
HORA_ABERTURA = 16  # 16:00
HORA_FECHAMENTO = 26  # 02:00 da manhã (tratado como hora 26 para facilitar)
DURACAO_SIMULACAO_MINUTOS = (HORA_FECHAMENTO - HORA_ABERTURA) * 60  # 10 horas * 60 min

# Regras dos Agentes
DINHEIRO_MIN_INICIAL = 50
DINHEIRO_MAX_INICIAL = 300
PRECO_BEBIDA = 15
ALCOOL_POR_BEBIDA = 0.5
LIMITE_ALCOOL_CONFUSAO = 3.0  # Nível de álcool para começar a causar confusão
PROB_CAUSAR_CONFUSAO = 0.1  # 10% de chance por minuto (se bêbado)
PROB_SER_EXPULSO = 0.5  # 50% de chance dos seguranças pegarem
PROB_IR_EMBORA_NORMAL = 0.005  # Chance base de ir embora por minuto
