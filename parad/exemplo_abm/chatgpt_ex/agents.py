# agents.py
from dataclasses import dataclass
from typing import TYPE_CHECKING
import numpy as np
import config

if TYPE_CHECKING:  # só pra type checker entender o tipo Customer dentro de Customer
    from typing import Generator


@dataclass
class BaseAgent:
    id: int


@dataclass
class Customer(BaseAgent):
    money: float
    strength: float
    reflex: float
    constitution: float
    agility: float
    speed: float
    drunk_level: float = 0.0
    alive: bool = True
    inside: bool = True
    time_in_tavern: int = 0
    robbed_amount: float = 0.0

    def choose_order(self, rng: np.random.Generator) -> str:
        """
        Decide o que consumir nesse passo de tempo.
        Retorna: "food", "alcohol", "soft" ou "none".
        """
        if (not self.alive) or (not self.inside):
            return "none"

        # Sem dinheiro suficiente, não consome mais nada
        if self.money < min(config.PRICES.values()):
            return "none"

        # Probabilidades simples (poderia virar parâmetro depois)
        p_drink = 0.6
        p_food = 0.3
        x = rng.random()

        if x < p_drink:
            # Se ainda não está muito bêbado, tende a pedir bebida alcoólica
            if (
                self.drunk_level < config.DRUNK_THRESHOLD
                and self.money >= config.PRICES["alcohol"]
            ):
                return "alcohol"
            elif self.money >= config.PRICES["soft"]:
                return "soft"
            else:
                return "none"
        elif x < p_drink + p_food and self.money >= config.PRICES["food"]:
            return "food"
        else:
            return "none"

    def apply_order_effects(self, order: str) -> None:
        """Atualiza dinheiro e nível de embriaguez."""
        if order == "alcohol":
            price = config.PRICES["alcohol"]
            if self.money >= price:
                self.money -= price
                # Constituição reduz um pouco o efeito do álcool
                self.drunk_level += 2.0 * (1.1 - self.constitution)

        elif order == "soft":
            price = config.PRICES["soft"]
            if self.money >= price:
                self.money -= price
                # Bebida não alcoólica ajuda a reduzir levemente
                self.drunk_level = max(0.0, self.drunk_level - 0.5)

        elif order == "food":
            price = config.PRICES["food"]
            if self.money >= price:
                self.money -= price
                # Comer “segura a onda”
                self.drunk_level = max(0.0, self.drunk_level - 1.0)

        self.drunk_level = min(self.drunk_level, config.MAX_DRUNK)

    def decide_leave(self, rng: np.random.Generator) -> bool:
        """Decide se o cliente vai embora neste passo."""
        if not self.inside or not self.alive:
            return False

        base_prob = 0.02 + 0.02 * self.time_in_tavern

        if self.money < 10:
            base_prob += 0.10
        if self.drunk_level > config.DRUNK_THRESHOLD:
            base_prob += 0.05

        return rng.random() < base_prob

    def try_steal(self, other: "Customer", rng: np.random.Generator) -> float:
        """
        Tenta furtar outro cliente.
        Retorna o valor roubado (0.0 se falhar).
        """
        if (not self.inside) or (not self.alive):
            return 0.0
        if (not other.inside) or (not other.alive):
            return 0.0
        if self is other:
            return 0.0

        # Pequena chance de tentar furto, maior se for ágil
        attempt_prob = 0.01 + 0.04 * self.agility
        if rng.random() > attempt_prob:
            return 0.0

        # Sucesso depende da agilidade do ladrão e reflexo da vítima
        success_chance = 0.5 * self.agility + 0.2 - 0.4 * other.reflex
        if rng.random() < success_chance and other.money > 0:
            amount = min(other.money * rng.uniform(0.1, 0.3), other.money)
            other.money -= amount
            self.money += amount
            other.robbed_amount += amount
            return amount

        return 0.0


@dataclass
class Staff(BaseAgent):
    role: str  # cozinheiro, atendente, segurança, gerente
    gender: str
