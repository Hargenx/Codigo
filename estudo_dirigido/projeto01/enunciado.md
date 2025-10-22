# 💻 Tarefa — Folha de Pagamento (2,0 pts)

## 🎯 Objetivo

Praticar os fundamentos de **POO em Java** a partir de um **modelo UML**:

* Classe/Objeto • Encapsulamento • Herança
* Interface • Polimorfismo • Override

Implemente o código **a partir dos diagramas** abaixo.

---

## 🧩 Descrição

Criar um mini sistema de **folha de pagamento** com dois tipos de funcionários:

* **CLT** (salário fixo com desconto didático)
* **Horista** (valor hora × horas no mês)

---

## 📦 Diagrama de **Classes** (Mermaid)

```mermaid
classDiagram
    direction TB

    class Pagavel {
        <<interface>>
        +calcularPagamentoMensal() double
    }

    class Funcionario {
        <<abstract>>
        - static SEQ : int
        - id : int
        - nome : String
        +Funcionario(nome: String)
        +getId() int
        +getNome() String
        +setNome(nome: String) void
        +toString() String
        +calcularPagamentoMensal() double
    }

    class FuncionarioCLT {
        - salarioMensal : double
        +FuncionarioCLT(nome: String, salarioMensal: double)
        +getSalarioMensal() double
        +setSalarioMensal(v: double) void
        +calcularPagamentoMensal() double
    }

    class FuncionarioHorista {
        - valorHora : double
        - horasNoMes : int
        +FuncionarioHorista(nome: String, valorHora: double, horasNoMes: int)
        +setValorHora(v: double) void
        +setHorasNoMes(h: int) void
        +calcularPagamentoMensal() double
    }

    class Main {
        +main(args: String[]) void
    }

    %% Relações
    Pagavel <|.. Funcionario
    Funcionario <|-- FuncionarioCLT
    Funcionario <|-- FuncionarioHorista
    Main ..> Pagavel : usa (List<Pagavel>)

    %% Notas (regras de negócio)
    note for Funcionario "Encapsular nome (não nulo/nem vazio). toString(): 'id - nome (Tipo)'. ID gerado por SEQ."
    note for FuncionarioCLT "Pagamento = salarioMensal * 0.95 (desconto didático). Validar salarioMensal > 0."
    note for FuncionarioHorista "Pagamento = valorHora * horasNoMes. Validar valorHora > 0 e 0 <= horasNoMes <= 220."
```

---

## 🔄 Diagrama de **Sequência** — Polimorfismo em ação

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Main
    participant Lista as List<Pagavel>
    participant CLT as FuncionarioCLT("Ana")
    participant HOR as FuncionarioHorista("Bruno")

    Usuario->>Main: executar()
    Main->>Lista: criar lista vazia
    Main->>Lista: add(CLT)
    Main->>Lista: add(HOR)

    loop para cada Pagavel p em Lista
        alt p é CLT
            Main->>CLT: calcularPagamentoMensal()
            CLT-->>Main: valorCLT
        else p é HOR
            Main->>HOR: calcularPagamentoMensal()
            HOR-->>Main: valorHorista
        end
    end
    Main->>Main: somar valores
    Main-->>Usuario: imprimir linhas e total da folha
```

---

## ✅ Requisitos de Implementação (a partir do UML)

1. **Interface `Pagavel`**

   * Método: `double calcularPagamentoMensal()`.

2. **Classe abstrata `Funcionario`**

   * Atributos: `id` (gerado por `SEQ`), `nome`.
   * Encapsulamento: `get/set` com **validação** de `nome`.
   * `toString()` no formato: `id - nome (Tipo)`.
   * Implementa `Pagavel`.

3. **`FuncionarioCLT`**

   * Atributo: `salarioMensal` (> 0).
   * Implementação: `calcularPagamentoMensal() = salarioMensal * 0.95`.

4. **`FuncionarioHorista`**

   * Atributos: `valorHora` (> 0), `horasNoMes` (0..220).
   * Implementação: `calcularPagamentoMensal() = valorHora * horasNoMes`.

5. **`Main`**

   * Criar `List<Pagavel>` com pelo menos um CLT e um Horista.
   * Iterar chamando `calcularPagamentoMensal()` (polimorfismo).
   * Imprimir a linha de cada funcionário e o **total da folha**.

---

## 📝 Critérios de Avaliação (2,0 pts)

| Critério                                          | Peso    |
| ------------------------------------------------- | ------- |
| Encapsulamento + validações                       | 0,4     |
| Herança (abstrata + 2 concretas)                  | 0,4     |
| Interface + Polimorfismo no `Main`                | 0,4     |
| Override (`toString` e `calcularPagamentoMensal`) | 0,4     |
| Execução correta e clareza de saídas              | 0,4     |
| **Total**                                         | **2,0** |

---

## 💡 Dicas

* Não precisa de `Scanner`; valores fixos no `Main` são suficientes.
* Comente no código onde aparecem **encapsulamento**, **herança**, **interface**, **polimorfismo** e **override**.
* Siga fielmente o UML para manter a coerência do design.
