# Mini-sistema de Análise de Pedidos de Restaurante

Este repositório contém a **solução de referência** para um trabalho valendo **3 pontos** da disciplina  
**Paradigmas de Linguagens de Programação – Python**, ofertada no período **2025.2**.

O objetivo do trabalho é implementar um **mini-sistema de análise de pedidos de um restaurante**, explorando:

- Organização em **módulos**;
- Uso de **classes** e **objetos** (Programação Orientada a Objetos – POO);
- Uso de **funções** e estilo mais **estruturado/funcional**;
- Tratamento de exceções com `try/except`;
- Uso de uma biblioteca externa simples (`numpy`) para operações numéricas.

> 📄 **Enunciado oficial**: o enunciado completo do trabalho está no arquivo  
> [`trabalho.pdf`](./trabalho.pdf), localizado neste mesmo diretório.

---

## 1. Contexto do Projeto

O sistema simula o cenário de um restaurante (“**Restaurante Bom Prato**”) que deseja analisar os pedidos realizados em um dia.  
Com base em uma lista de pedidos (pré-cadastrados em código), o sistema permite:

- Calcular o **faturamento total** do dia;
- Calcular o **ticket médio** (valor médio por pedido);
- Obter **estatísticas** simples sobre os valores dos pedidos (mínimo, máximo e média);
- Descobrir os **produtos mais vendidos**.

Todo o código foi pensado para ser usado em ambiente de entrevista/prova, com:

- Acesso apenas ao **VSCode**;
- Sem acesso à **internet**;
- Uso permitido da biblioteca **`numpy`**.

---

## 2. Estrutura do Projeto

A solução está organizada em módulos, para reforçar a separação de responsabilidades:

```text
.
├── analytics.py   # Funções de análise numérica (usa numpy)
├── dados.py       # Criação dos pedidos de exemplo
├── main.py        # Ponto de entrada da aplicação (menu de texto)
├── models.py      # Classes de domínio (Produto e Pedido)
└── trabalho.pdf   # Enunciado completo do trabalho
````

### 2.1. `models.py`

Contém as classes principais do domínio:

- `Produto`

  - Atributos: `nome`, `preco`
  - Validação simples (nome não vazio, preço não negativo)
  - Métodos de representação (`__str__`, `__repr__`)

- `Pedido`

  - Atributos: `id_pedido`, `produtos` (lista de `Produto`)
  - Método `valor_total()` que soma os preços dos produtos

### 2.2. `dados.py`

Responsável por criar **dados de exemplo**:

- Função `criar_pedidos_exemplo()`:

  -Cria alguns produtos de cardápio;
  - Cria uma lista de pedidos com combinações de produtos (incluindo repetições para permitir ranking de “mais vendidos”).

### 2.3. `analytics.py`

Contém funções de **análise numérica**, usando `numpy`:

- `calcular_faturamento_total(pedidos)`
- `calcular_ticket_medio(pedidos)`
- `calcular_estatisticas_valores(pedidos)`

  - Retorna um dicionário com `minimo`, `maximo`, `media`
- `top_produtos_mais_vendidos(pedidos, n=3)`

  - Retorna os `n` produtos mais frequentes como lista de tuplas `(nome, quantidade)`

### 2.4. `main.py`

Implementa a **interface de linha de comando**:

- Classe `Aplicacao`, que recebe a lista de pedidos e:

  - Exibe um menu de texto;
  - Lê a opção do usuário com `input()`;
  - Usa `try/except` para tratar entradas inválidas (`ValueError`);
  - Chama as funções de análise conforme a opção escolhida;
  - Exibe os resultados formatados.

---

## 3. Conceitos de Paradigmas de Programação Explorados

Este projeto foi pensado para **treinar e avaliar** conceitos da disciplina de Paradigmas de Linguagens de Programação em Python:

1. **Programação Estruturada / Funcional “light”**

   - Uso de funções puras em `analytics.py` e `dados.py`;
   - Uso de `sum`, compreensões de listas, `Counter`, etc.

2. **Programação Orientada a Objetos (POO)**

   - Modelagem de domínio com `Produto` e `Pedido`;
   - Encapsulamento de comportamento em métodos (`valor_total`, `__str__`, etc.);
   - Classe `Aplicacao` como orquestradora do fluxo.

3. **Módulos e Organização**

   - Separação por responsabilidade (`models`, `dados`, `analytics`, `main`);
   - Importação entre módulos (`from models import Pedido`, etc.).

4. **Tratamento de Exceções**

   - Uso de `try/except` para:

     - Conversão de `input()` para inteiro;
     - Validação de dados (por exemplo, pedidos vazios, IDs inválidos).

5. **Uso de Biblioteca Externa (`numpy`)**

   - Criação de arrays numéricos a partir dos valores dos pedidos;
   - Uso de operações vetorizadas (`np.sum`, `np.mean`, `np.min`, `np.max`).

---

## 4. Requisitos de Ambiente

- **Python**: versão 3.x (recomendado 3.10+)
- **Biblioteca**:

  - [`numpy`](https://numpy.org/) instalada no ambiente (para a avaliação, considera-se que já está disponível)

Exemplo de instalação (fora do contexto da prova, para rodar localmente):

```bash
pip install numpy
```

---

## 5. Como Executar

Dentro do diretório do projeto:

```bash
python main.py
```

O sistema exibirá um menu semelhante a:

```text
=== Menu Restaurante Bom Prato ===
1 - Mostrar faturamento total do dia
2 - Mostrar ticket médio dos pedidos
3 - Mostrar estatísticas dos valores dos pedidos
4 - Mostrar top 3 produtos mais vendidos
0 - Sair
----------------------------------------
Escolha uma opção:
```

Basta digitar o número da opção desejada e pressionar **Enter**.

---

## 6. Uso Didático e Avaliação (3 pontos)

Este projeto foi desenvolvido como **solução de referência** para um trabalho avaliativo da disciplina
**Paradigmas de Linguagens de Programação – Python (2025.2)**, valendo **3 pontos**.

Alguns critérios típicos de avaliação que podem ser aplicados:

- Organização do código em módulos;
- Uso correto de classes e objetos;
- Implementação das funcionalidades solicitadas no enunciado (`trabalho.pdf`);
- Uso adequado de `numpy` nas análises;
- Tratamento de erros com `try/except`;
- Clareza, legibilidade e pequenos cuidados de boas práticas (nomes de funções e variáveis, mensagens para o usuário, etc.).

---

## 7. Observações Finais

- Esta solução não pretende ser a **única** forma correta de implementar o problema, mas serve como um **modelo sólido** de referência.
- Para fins de aprendizado, recomenda-se aos estudantes:

  - Tentar implementar **primeiro a própria solução**, usando apenas o enunciado (`trabalho.pdf`);
  - Só depois comparar com este código, identificando diferenças de abordagem, estilo e organização.
