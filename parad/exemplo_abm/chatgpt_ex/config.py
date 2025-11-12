# config.py
import numpy as np

# Janela de funcionamento: 16h até 02h (26 = 2h do dia seguinte)
OPEN_HOUR = 16
CLOSE_HOUR = 26
N_TICKS = CLOSE_HOUR - OPEN_HOUR  # 10 passos de tempo (1 hora cada)

# Capacidade física da taberna (apenas salão do 1º andar + em pé)
N_TABLES = 6
SEATS_PER_TABLE = 6
BAR_STOOLS = 12
STANDING_SPOTS = 8  # no máx. 8 em pé, depois superlotada

BASE_CAPACITY = N_TABLES * SEATS_PER_TABLE + BAR_STOOLS + STANDING_SPOTS
MAX_OVERFLOW = 4  # seguranças/gerentes deixam passar só um pouco
MAX_CAPACITY = BASE_CAPACITY + MAX_OVERFLOW

# Taxa média de chegada de clientes por hora (pode ajustar depois em aula)
# Índice 0 = 16h, 1 = 17h, ..., 9 = 01h
ARRIVALS_PER_HOUR = np.array([2, 4, 8, 12, 14, 10, 7, 4, 2, 1], dtype=float)

# Preços médios (cada categoria representa vários itens do menu)
PRICES = {
    "food": 25.0,  # 18 pratos
    "alcohol": 15.0,  # 14 bebidas alcoólicas
    "soft": 8.0,  # 8 não alcoólicas (22 - 14)
}

DRUNK_THRESHOLD = 4.0  # acima disso consideramos "bêbado"
MAX_DRUNK = 10.0

# Semente para reprodutibilidade (bom pra aula)
SEED = 42
