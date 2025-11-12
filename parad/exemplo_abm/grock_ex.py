import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Módulo 1: Definição de Classes para Agentes
class Agent:
    def __init__(self, name, gender, role, attributes=None, money=0):
        self.name = name
        self.gender = gender
        self.role = role  # 'customer', 'cook', 'waiter', 'security', 'manager'
        self.attributes = attributes if attributes else {
            'strength': random.randint(5, 10),
            'reflex': random.randint(5, 10),
            'constitution': random.randint(5, 10),
            'agility': random.randint(5, 10),
            'speed': random.randint(5, 10)
        }
        self.money = money if role == 'customer' else float('inf')  # Equipe não gasta dinheiro
        self.alcohol_level = 0  # Nível de álcool afeta atributos
        self.location = 'outside'  # Localização: 'outside', 'bar', 'table', 'upstairs'
        self.status = 'normal'  # 'normal', 'drunk', 'fighting', 'dead'

    def consume(self, item):
        # Simula consumo de comida/bebida
        if 'alcohol' in item:
            self.alcohol_level += random.uniform(0.5, 2.0)
            if self.alcohol_level > 5:
                self.status = 'drunk'
                # Reduz atributos quando bêbado
                for attr in self.attributes:
                    self.attributes[attr] = max(1, self.attributes[attr] - 1)
        else:
            # Comida melhora constituição
            self.attributes['constitution'] = min(10, self.attributes['constitution'] + 1)
        self.money -= item['price']

    def interact(self, other):
        # Interações simples: furto, briga
        if self.status == 'drunk' and random.random() < 0.1:
            self.status = 'fighting'
            other.status = 'fighting'
            print(f"{self.name} started a fight with {other.name}!")
        elif random.random() < 0.05:  # Chance de furto
            if self.money < 10:  # Motivação para furtar
                stolen = min(20, other.money)
                other.money -= stolen
                self.money += stolen
                print(f"{self.name} stole {stolen} from {other.name}!")

    def pay_bill(self):
        # Paga a conta ao sair
        print(f"{self.name} paid their bill. Remaining money: {self.money}")

# Módulo 2: Definição do Ambiente (Taberna)
class Tavern:
    def __init__(self):
        self.open_time = datetime.strptime('16:00', '%H:%M')
        self.close_time = datetime.strptime('02:00', '%H:%M') + timedelta(days=1)  # Próximo dia
        self.current_time = self.open_time
        self.staff = self._initialize_staff()
        self.customers = []
        self.menu = self._generate_menu()
        self.capacity = {
            'tables': 6 * 6,  # 6 mesas x 6 pessoas
            'bar': 12,        # 12 cadeiras no balcão
            'standing': 8,    # Máximo 8 em pé
            'upstairs_individual': 4,  # 4 dormitórios individuais
            'upstairs_collective': 4 * 4  # 4 coletivos x 4 pessoas
        }
        self.occupancy = {'bar': 0, 'tables': 0, 'standing': 0, 'upstairs': 0}
        self.closed = False  # Fecha se houver morte

    def _initialize_staff(self):
        # Cria equipe conforme especificado
        staff = [
            Agent('Cook_M', 'male', 'cook'),
            Agent('Cook_F', 'female', 'cook'),
            Agent('Waiter1', 'female', 'waiter'),
            Agent('Waiter2', 'female', 'waiter'),
            Agent('Waiter3', 'female', 'waiter'),
            Agent('Waiter4', 'female', 'waiter'),
            Agent('Security1', 'male', 'security'),
            Agent('Security2', 'male', 'security'),
            Agent('Manager_M', 'male', 'manager'),
            Agent('Manager_F', 'female', 'manager')
        ]
        return staff

    def _generate_menu(self):
        # Menu simples: varia por cozinheiro, mas para simplicidade, fixo
        dishes = [f'Dish_{i}' for i in range(1, 19)]
        drinks_non_alc = [f'NonAlc_{i}' for i in range(1, 9)]
        drinks_alc = [f'Alc_{i}' for i in range(1, 15)]
        menu = {}
        for item in dishes:
            menu[item] = {'type': 'food', 'price': random.randint(10, 30)}
        for item in drinks_non_alc:
            menu[item] = {'type': 'drink', 'price': random.randint(5, 15)}
        for item in drinks_alc:
            menu[item] = {'type': 'drink', 'alcohol': True, 'price': random.randint(8, 20)}
        return menu

    def customer_arrival(self):
        # Fluxo varia com horário: mais à noite
        hour = self.current_time.hour
        arrival_prob = 0.1 if hour < 18 else 0.3 if hour < 22 else 0.2
        if random.random() < arrival_prob and sum(self.occupancy.values()) < sum(self.capacity.values()) + 5:  # Pode exceder um pouco
            new_customer = Agent(f'Customer_{len(self.customers)+1}', random.choice(['male', 'female']), 'customer', money=random.randint(50, 200))
            self.customers.append(new_customer)
            self._assign_location(new_customer)
            print(f"{new_customer.name} arrived at {self.current_time.strftime('%H:%M')}")

    def _assign_location(self, agent):
        # Atribui localização baseada em disponibilidade
        if self.occupancy['tables'] < self.capacity['tables']:
            agent.location = 'table'
            self.occupancy['tables'] += 1
        elif self.occupancy['bar'] < self.capacity['bar']:
            agent.location = 'bar'
            self.occupancy['bar'] += 1
        elif self.occupancy['standing'] < self.capacity['standing']:
            agent.location = 'standing'
            self.occupancy['standing'] += 1
        else:
            # Tenta upstairs se disponível (para simplicidade, assume alguns vão dormir)
            if random.random() < 0.1 and self.occupancy['upstairs'] < self.capacity['upstairs_individual'] + self.capacity['upstairs_collective']:
                agent.location = 'upstairs'
                self.occupancy['upstairs'] += 1
            else:
                print("Tavern is full! Customer turned away.")

    def simulate_step(self):
        # Avança tempo em 30 minutos
        self.current_time += timedelta(minutes=30)
        if self.current_time >= self.close_time:
            self.closed = True
            return

        # Chegada de clientes
        self.customer_arrival()

        # Interações entre agentes
        all_agents = self.staff + self.customers
        for agent in self.customers:
            if agent.status == 'dead':
                self.closed = True
                print("A death occurred! Tavern closing for police.")
                return
            if agent.status == 'drunk' and random.random() < 0.2:
                # Expulsão por segurança
                security = [s for s in self.staff if s.role == 'security']
                if security:
                    agent.location = 'outside'
                    self._update_occupancy(agent, -1)
                    print(f"{agent.name} was expelled for being drunk.")
            else:
                # Consome algo
                item = random.choice(list(self.menu.keys()))
                agent.consume(self.menu[item])
                # Interage com outro agente aleatório
                other = random.choice(all_agents)
                if other != agent:
                    agent.interact(other)
                    if random.random() < 0.01:  # Rara chance de morte em briga
                        if agent.status == 'fighting':
                            agent.status = 'dead'

        # Saída aleatória de clientes
        for agent in self.customers[:]:
            if random.random() < 0.05:
                agent.pay_bill()
                self._update_occupancy(agent, -1)
                self.customers.remove(agent)
                print(f"{agent.name} left at {self.current_time.strftime('%H:%M')}")

    def _update_occupancy(self, agent, delta):
        if agent.location == 'table':
            self.occupancy['tables'] += delta
        elif agent.location == 'bar':
            self.occupancy['bar'] += delta
        elif agent.location == 'standing':
            self.occupancy['standing'] += delta
        elif agent.location == 'upstairs':
            self.occupancy['upstairs'] += delta

# Módulo 3: Simulação e Visualização
def run_simulation(steps=20):
    tavern = Tavern()
    times = []
    occupancies = []
    
    for _ in range(steps):
        if tavern.closed:
            break
        tavern.simulate_step()
        times.append(tavern.current_time.strftime('%H:%M'))
        occupancies.append(sum(tavern.occupancy.values()))
    
    # Visualização com Matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(times, occupancies, marker='o')
    plt.xlabel('Time')
    plt.ylabel('Occupancy')
    plt.title('Tavern Occupancy Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Executar a simulação
if __name__ == "__main__":
    run_simulation(steps=30)  # Simula cerca de 15 horas em passos de 30 min