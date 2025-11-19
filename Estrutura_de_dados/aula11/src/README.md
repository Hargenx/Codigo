# Estrutura de Dados em C — Exemplo Modular (Ordenação + Árvore BST)

Este projeto é um **exemplo didático** para a disciplina de **Estrutura de Dados em C**.
Mostra:

* **Modularização** (um `.h` por módulo com a API pública e `.c` com a implementação);
* Quatro **algoritmos de ordenação** (Insertion, Quick, Merge, Heap);
* **Árvore Binária de Busca (BST)** com tipo **opaco** e percorrimento *in-order*;
* **Medição de tempo** das ordenações e **construção** da BST.

> ⚠️ Este repositório é apenas para fins educacionais: código simples, foco em clareza e comparação de complexidade.

---

## Estrutura de pastas/arquivos

```tree
.
├─ insertion_sort.h / insertion_sort.c   // O(n^2), estável, in-place
├─ quick_sort.h     / quick_sort.c       // O(n log n) médio (pior O(n^2))
├─ merge_sort.h     / merge_sort.c       // O(n log n), estável (usa memória extra)
├─ heap_sort.h      / heap_sort.c        // O(n log n), in-place
├─ bst.h            / bst.c              // Árvore binária de busca (tipo opaco)
└─ main.c                                 // Gera dados, mede tempos, imprime prefixos
```

* **Headers** (`.h`) expõem **somente** as funções públicas.
* Funções auxiliares ficam `static` dentro do `.c` (não “vazam” símbolos).
* Em `bst.h` usamos **tipo opaco**: `typedef struct BST BST;`
  A estrutura real só é conhecida dentro de `bst.c`.

---

## Compilação

### Windows (PowerShell, MinGW)

**Objetos separados (recomendado para ver modularização):**

```powershell
gcc -std=c11 -Wall -Wextra -O2 -c .\insertion_sort.c
gcc -std=c11 -Wall -Wextra -O2 -c .\quick_sort.c
gcc -std=c11 -Wall -Wextra -O2 -c .\merge_sort.c
gcc -std=c11 -Wall -Wextra -O2 -c .\heap_sort.c
gcc -std=c11 -Wall -Wextra -O2 -c .\bst.c
gcc -std=c11 -Wall -Wextra -O2 -c .\main.c
gcc -o .\demo.exe .\main.o .\insertion_sort.o .\quick_sort.o .\merge_sort.o .\heap_sort.o .\bst.o
.\demo.exe
```

**Tudo de uma vez:**

```powershell
gcc -std=c11 -Wall -Wextra -O2 .\main.c .\insertion_sort.c .\quick_sort.c .\merge_sort.c .\heap_sort.c .\bst.c -o .\demo.exe
.\demo.exe
```

### Linux/macOS

```bash
gcc -std=c11 -Wall -Wextra -O2 main.c insertion_sort.c quick_sort.c merge_sort.c heap_sort.c bst.c -o demo
./demo
```

---

## O que o programa faz

1. Gera um vetor base de `n` inteiros aleatórios.
2. Mede o tempo (ms) para ordenar com:

   * Insertion sort — **O(n²)**
   * Quick sort — **O(n log n)** em média
   * Merge sort — **O(n log n)**
   * Heap sort — **O(n log n)**
3. Constrói uma **BST** com os mesmos dados:

   * Mede o **tempo de construção** (série de `insert`).
   * Faz **percorrimento in-order** e coleta num vetor (ordem crescente).
   * Exibe **tamanho** e **altura** da árvore.

> O `main.c` imprime apenas um **prefixo** de cada vetor ordenado (10 primeiros valores) para checagem rápida.

### Exemplo de saída (valores variam por máquina/semente)

```cmd
n = 20000 elementos
Insertion (prefixo): 2 5 14 15 17 25 34 36 36 36 ...
Quick     (prefixo): 2 5 14 15 17 25 34 36 36 36 ...
Merge     (prefixo): 2 5 14 15 17 25 34 36 36 36 ...
Heap      (prefixo): 2 5 14 15 17 25 34 36 36 36 ...

Tempos de ordenacao (ms):
Insertion sort :  182.428  (O(n^2))
Quick sort     :    2.025  (O(n log n) medio, O(n^2) pior)
Merge sort     :    2.502  (O(n log n))
Heap sort      :    3.777  (O(n log n))

BST in-order (prefixo): 2 5 14 15 17 25 34 36 36 36 ...
BST: tamanho = 20000, altura = 28
Tempo para construir BST: 11.230 ms (insercao media O(log n), pior O(n))
```

---

## Como usar em aula

* Mude `n` em `main.c` (`const size_t n = ...`) para **comparar crescimento** de tempo.
* Teste **entrada já ordenada** ou **quase ordenada**:

  * Insertion sort tende a **ir muito bem** nesses casos (quase O(n)).
* Compare **BST in-order** com o resultado do sort → reforça a **propriedade da BST**.
* Discuta **altura**: inserção aleatória costuma gerar altura ~ **O(log n)**; pior caso **O(n)** (motivação para AVL/Red-Black).

---

## Big-O (teórico)

| Algoritmo    | Melhor     | Médio      | Pior       | Estável | Memória extra  |
| ------------ | ---------- | ---------- | ---------- | ------- | -------------- |
| Insertion    | O(n)       | O(n²)      | O(n²)      | Sim     | O(1)           |
| Quick        | O(n log n) | O(n log n) | O(n²)      | Não*    | O(log n) pilha |
| Merge        | O(n log n) | O(n log n) | O(n log n) | Sim     | O(n)           |
| Heap         | O(n log n) | O(n log n) | O(n log n) | Não     | O(1)           |
| BST (insert) | O(log n)   | O(log n)   | O(n)       | —       | O(h) recursão  |

* Implementações com *stable partition* existem, mas não no quicksort padrão.

---

## API resumida da BST

```c
BST  *bst_create(void);
void  bst_free(BST *tree);
int   bst_insert(BST *tree, int key);           // 1 = ok, 0 = falta memória
int   bst_contains(const BST *tree, int key);   // 1 = existe, 0 = não
size_t bst_size(const BST *tree);
int   bst_height(const BST *tree);              // vazia = -1; folha = 0
void  bst_inorder(const BST *t, void (*visit)(int, void*), void *ud);
```

---

## Solução de problemas

* **`undefined reference`** (linker): compile e **linke todos os `.c`** (veja comandos acima).
* **`clock_t`/`printf` não encontrados**: verifique se `#include <time.h>` / `#include <stdio.h>` estão no `main.c`.
* **Saídas diferentes**: tempos variam por hardware, compilador e semente aleatória (`srand(time(NULL))`).

---

## Extensões sugeridas

* Adicionar **Radix Sort** (`radix_sort.h/.c`) com filas/buckets.
* Implementar **remoção** e **balanceamento** (AVL/Red-Black) na BST.
* Exportar tempos em CSV e plotar gráficos (n vs tempo) para visualizar crescimento.

---

**Licença:** uso livre para fins acadêmicos.
