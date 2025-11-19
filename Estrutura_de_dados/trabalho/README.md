# Trabalho – Estrutura de Dados (C) — **valendo 3 pontos**

Este trabalho é **rápido (30 minutos)** e deve ser feito **em linguagem C**. O objetivo é verificar domínio de **módulos**, **estruturas homogêneas e heterogêneas** e **ponteiros**.

## Objetivos de aprendizagem

* Organizar código em “módulos” (mesmo que num arquivo, separar por seções/headers lógicos).
* Modelar **estrutura heterogênea** com `enum` + `union`.
* Usar **estrutura homogênea** (vetor de `Item`).
* Empregar **ponteiros** em funções (passagem por referência e retorno de ponteiros).

## Enunciado (resumo)

Implemente um mini-cadastro de **itens de uma taberna**:

* Cada `Item` é **COMIDA** (guarda `kcal`) ou **BEBIDA** (guarda `teor_alcoolico`).
* Todos os itens têm `id`, `nome`, `preco` e `tipo`.
* Armazene os itens em um **vetor (homogêneo)** `Item vet[MAX]`.
* Implemente funções:

  1. `inserir(Item vet[], int *n, Item x)` – insere no fim (usa ponteiro para `n`);
  2. `buscar(Item vet[], int n, int id)` – retorna `Item*` ou `NULL`;
  3. `listar(const Item vet[], int n)` – imprime todos.

## Especificação técnica mínima

* `enum ItemTipo { T_COMIDA, T_BEBIDA };`
* `union { int kcal; float teor_alcoolico; };` dentro de `struct Item`.
* Uso de **ponteiros**:

  * `int *n` para atualizar tamanho do vetor;
  * retorno de **`Item*`** na busca;
  * parâmetros `const Item*` quando só leitura.
* Organização por **módulos/seções** (ex.: comentários `/* modulo: tipos */`, `/* modulo: lista */`, `/* modulo: app */` ou headers se fizer em arquivos).

## Entrega

* **Formato “no papel” (preferido)**: escreva o código legível em 1–2 páginas, com seções organizadas e assinadas.
* **Opcional (digitado)**: entregar `main.c` (ou arquivos separados).

  * Compilação sugerida: `gcc -std=c11 -Wall -Wextra -O2 main.c -o taberna`

## Avaliação (3,0 pontos)

1. **Modelagem heterogênea (enum + union)** – 0,8
2. **Estrutura homogênea (vetor de `Item`)** – 0,6
3. **Ponteiros corretamente empregados** – 0,8

   * `int *n` em `inserir`, retorno `Item*` em `buscar`, `const Item*` em impressão
4. **Modularização/organização do código** – 0,4
5. **Compilabilidade/lógica geral** – 0,4
   **Bônus (até +0,2):** implementar **remover por id** *ou* **média de preços por tipo**.

## Restrições

* **Tempo total:** 30 minutos.
* Não usar bibliotecas externas além de `<stdio.h>`, `<string.h>` e similares da libc.
* Nomes de variáveis e funções claros; comentários concisos.

## Esqueleto (opcional, para guiar a escrita)

```c
/* ===== modulo: tipos/item ===== */
typedef enum { T_COMIDA=0, T_BEBIDA=1 } ItemTipo;

typedef struct {
    int id; char nome[16]; float preco; ItemTipo tipo;
    union { int kcal; float teor_alcoolico; } extra;
} Item;

void imprimir_item(const Item *p);

/* ===== modulo: lista (vetor homogeneo) ===== */
#define MAX 20
int   inserir(Item vet[], int *n, Item x);
Item* buscar(Item vet[], int n, int id);
void  listar(const Item vet[], int n);

/* ===== modulo: app (main) ===== */
int main(void) { /* montar 2-3 itens, listar, buscar */ }
```

## Dicas rápidas

* Escreva primeiro as **definições** (`enum/struct/union`), depois as **funções de lista** e por fim o `main`.
* Use `const` para funções que **não** alteram dados.
* Teste mentalmente com 2–3 itens: inserir → listar → buscar.

## Melhorias (opcional)

* Escreva cada **função separadamente** em arquivos separados.
* Crie um **header** para cada módulo.
* Faça **testes** com `assert` e `check`.
