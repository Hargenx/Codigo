# simulation.py
from dataclasses import dataclass, field
from typing import List
import numpy as np
import matplotlib.pyplot as plt

import config
from agents import Customer, Staff


@dataclass
class TavernState:
    customers: List[Customer] = field(default_factory=list)
    staff: List[Staff] = field(default_factory=list)
    current_tick: int = 0
    fights: int = 0
    thefts: int = 0
    expulsions: int = 0
    deaths: int = 0
    closed_by_police: bool = False

    def occupancy(self) -> int:
        """Número de clientes vivos e dentro da taberna."""
        return sum(1 for c in self.customers if c.inside and c.alive)


def create_staff() -> List[Staff]:
    staff: List[Staff] = []

    # 2 cozinheiros (1 homem, 1 mulher)
    staff.append(Staff(id=1000, role="cozinheiro", gender="M"))
    staff.append(Staff(id=1001, role="cozinheira", gender="F"))

    # 4 atendentes mulheres
    for i in range(4):
        staff.append(Staff(id=1100 + i, role="atendente", gender="F"))

    # 2 seguranças homens
    for i in range(2):
        staff.append(Staff(id=1200 + i, role="seguranca", gender="M"))

    # 2 gerentes (casal dono)
    staff.append(Staff(id=1300, role="gerente", gender="M"))
    staff.append(Staff(id=1301, role="gerente", gender="F"))

    return staff


def spawn_customers(
    rng: np.random.Generator, tick: int, next_id: int
) -> List[Customer]:
    """Cria novos clientes chegando na taberna neste tick."""
    hour_index = tick  # 0 = 16h, 1 = 17h, ...
    lam = config.ARRIVALS_PER_HOUR[hour_index]
    n_new = rng.poisson(lam)

    customers: List[Customer] = []
    for i in range(n_new):
        # força, reflexo, constituição, agilidade, velocidade
        attrs = rng.uniform(0.4, 1.0, size=5)
        money = rng.uniform(50, 200)
        customers.append(
            Customer(
                id=next_id + i,
                money=money,
                strength=attrs[0],
                reflex=attrs[1],
                constitution=attrs[2],
                agility=attrs[3],
                speed=attrs[4],
            )
        )
    return customers


def handle_fights(state: TavernState, rng: np.random.Generator) -> None:
    """Clientes bêbados podem brigar; brigas podem gerar expulsão ou morte."""
    drunk_customers = [
        c
        for c in state.customers
        if c.inside and c.alive and c.drunk_level > config.DRUNK_THRESHOLD
    ]
    if len(drunk_customers) < 2:
        return

    # Chance de ocorrer alguma briga nesse tick (quanto mais bêbados, mais chance)
    base_prob = min(0.3, 0.05 * len(drunk_customers))
    if rng.random() > base_prob:
        return

    c1, c2 = rng.choice(drunk_customers, size=2, replace=False)
    state.fights += 1

    # Segurança tenta separar (2 seguranças)
    # Chance de controlar é alta se poucos bêbados
    control_chance = 0.9 - 0.01 * len(drunk_customers)
    control_chance = max(0.5, control_chance)

    if rng.random() < control_chance:
        # Alguém é expulso se estiver muito alterado
        to_expell = c1 if c1.drunk_level >= c2.drunk_level else c2
        to_expell.inside = False
        state.expulsions += 1
    else:
        # Briga grave: alguém pode morrer
        if rng.random() < 0.3:
            # quem tem menos constituição tem maior risco
            victim = c1 if c1.constitution <= c2.constitution else c2
            victim.alive = False
            victim.inside = False
            state.deaths += 1
            state.closed_by_police = True  # taberna fecha para chegada da polícia


def handle_thefts(state: TavernState, rng: np.random.Generator) -> None:
    """Alguns clientes podem furtar outros."""
    inside_customers = [c for c in state.customers if c.inside and c.alive]
    if len(inside_customers) < 2:
        return

    # Escolhe poucos potenciais ladrões
    n_attempts = min(3, len(inside_customers))
    thieves = rng.choice(inside_customers, size=n_attempts, replace=False)
    for thief in thieves:
        victim_candidates = [c for c in inside_customers if c is not thief]
        if not victim_candidates:
            continue
        victim = rng.choice(victim_candidates)
        amount = thief.try_steal(victim, rng)
        if amount > 0:
            state.thefts += 1


def step(state: TavernState, rng: np.random.Generator, next_id: int) -> int:
    """
    Executa um passo de tempo (1 hora).
    Retorna o próximo id disponível.
    """
    if state.closed_by_police:
        return next_id

    tick = state.current_tick

    # 1) Chegada de novos clientes
    new_customers = spawn_customers(rng, tick, next_id)
    next_id += len(new_customers)

    # Se estiver lotado, parte deles é barrada na porta
    available_slots = max(0, config.MAX_CAPACITY - state.occupancy())
    allowed_new = new_customers[:available_slots]
    state.customers.extend(allowed_new)
    # os demais “não entram” no modelo

    # 2) Clientes já presentes fazem pedidos
    for c in state.customers:
        if c.inside and c.alive:
            c.time_in_tavern += 1
            order = c.choose_order(rng)
            c.apply_order_effects(order)

    # 3) Interações sociais: furtos e brigas
    handle_thefts(state, rng)
    handle_fights(state, rng)

    # 4) Clientes decidem ir embora
    for c in state.customers:
        if c.inside and c.alive and c.decide_leave(rng):
            c.inside = False

    state.current_tick += 1
    return next_id


def run_simulation() -> None:
    rng = np.random.default_rng(config.SEED)
    state = TavernState()
    state.staff = create_staff()

    occupancies = []
    fights = []
    thefts = []
    expulsions = []
    deaths = []

    next_id = 0
    for _ in range(config.N_TICKS):
        occupancies.append(state.occupancy())
        fights.append(state.fights)
        thefts.append(state.thefts)
        expulsions.append(state.expulsions)
        deaths.append(state.deaths)

        next_id = step(state, rng, next_id)
        if state.closed_by_police:
            break  # taberna fechou antes das 02h

    occupancies = np.array(occupancies)
    fights = np.array(fights)
    thefts = np.array(thefts)
    expulsions = np.array(expulsions)
    deaths = np.array(deaths)

    hours = np.arange(config.OPEN_HOUR, config.OPEN_HOUR + len(occupancies))

    # Gráfico 1: ocupação ao longo da noite
    fig, ax1 = plt.subplots()
    ax1.plot(hours, occupancies, marker="o")
    ax1.set_xlabel("Hora do dia")
    ax1.set_ylabel("Número de clientes dentro da taberna")
    ax1.set_title("ABM da Taberna: ocupação ao longo da noite")

    # Gráfico 2: eventos acumulados
    fig2, ax2 = plt.subplots()
    ax2.step(hours, fights, where="post", label="Brigas acumuladas")
    ax2.step(hours, thefts, where="post", label="Furtos acumulados")
    ax2.step(hours, expulsions, where="post", label="Expulsões acumuladas")
    ax2.step(hours, deaths, where="post", label="Mortes acumuladas")
    ax2.set_xlabel("Hora do dia")
    ax2.set_ylabel("Eventos acumulados")
    ax2.set_title("ABM da Taberna: eventos ao longo da noite")
    ax2.legend()

    plt.show()


if __name__ == "__main__":
    run_simulation()
