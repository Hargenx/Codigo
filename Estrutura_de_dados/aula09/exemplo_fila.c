// filas_e_radix.c
#include <stdio.h>
#include <stdlib.h>

typedef int Elemento;

/* -------- Fila encadeada (dinâmica) -------- */
typedef struct No {
  Elemento elemento;
  struct No *prox;
} No;

typedef struct {
  No *inicio; // cabeça (frente)
  No *fim;    // cauda (trás)
  size_t tam;
} Fila;

void fila_init(Fila *f) {
  f->inicio = f->fim = NULL;
  f->tam = 0;
}
int fila_vazia(const Fila *f) { return f->inicio == NULL; }

int enfileirar(Fila *f, Elemento e) {
  No *novo_no = (No *)calloc(1, sizeof *novo_no);
  if (!novo_no)
    return 0; // falha de memória
  novo_no->elemento = e;
  novo_no->prox = NULL;

  if (f->fim != NULL) // fila não-vazia
    f->fim->prox = novo_no;
  else // a fila estava vazia
    f->inicio = novo_no;

  f->fim = novo_no;
  f->tam++;
  return 1; // sucesso
}

int desenfileirar(Fila *f, Elemento *out) {
  if (f->inicio != NULL) {
    No *aux = f->inicio;
    f->inicio = f->inicio->prox; // avança o início
    if (f->inicio == NULL)       // esvaziou: ajusta fim
      f->fim = NULL;
    if (out)
      *out = aux->elemento;
    free(aux);
    f->tam--;
    return 1; // sucesso
  }
  return 0; // falha (fila vazia)
}

void fila_libera(Fila *f) {
  Elemento lixo;
  while (desenfileirar(f, &lixo))
    ;
}

/* -------- Ordenação por distribuição (Radix LSD) com m filas --------
   - base 'm' > 1
   - estável porque cada dígito é coletado mantendo a ordem nas filas
   - complexidade ~ O(d * (n + m)), onde d = nº de dígitos
*/
static int max_abs(const int *A, size_t n) {
  int m = 0;
  for (size_t i = 0; i < n; ++i) {
    int v = A[i] < 0 ? -A[i] : A[i];
    if (v > m)
      m = v;
  }
  return m;
}

void radix_lsd_com_filas(int *A, size_t n, int m_base) {
  if (n == 0 || m_base <= 1)
    return;

  // buckets (m filas)
  Fila *B = (Fila *)malloc((size_t)m_base * sizeof *B);
  for (int b = 0; b < m_base; ++b)
    fila_init(&B[b]);

  // Trata apenas números não negativos para simplicidade de aula
  // (negativos podem ser tratados separando sinais)
  int m = max_abs(A, n);
  for (int exp = 1; m / exp > 0; exp *= m_base) {
    // Distribui pelos dígitos (j-ésimo dígito menos significativo)
    for (size_t j = 0; j < n; ++j) {
      int dig = (A[j] / exp) % m_base;
      enfileirar(&B[dig], A[j]);
    }
    // Coleta de volta mantendo a ordem
    size_t k = 0;
    for (int d = 0; d < m_base; ++d) {
      Elemento x;
      while (desenfileirar(&B[d], &x))
        A[k++] = x;
    }
  }
  for (int b = 0; b < m_base; ++b)
    fila_libera(&B[b]);
  free(B);
}

/* ------------------ Demo ------------------ */
static void print_v(const int *v, size_t n) {
  for (size_t i = 0; i < n; ++i)
    printf("%d%c", v[i], (i + 1 == n) ? '\n' : ' ');
}

int main(void) {
  // 1) Enfileirar & 2) Desenfileirar (alocação dinâmica)
  Fila F;
  fila_init(&F);
  enfileirar(&F, 10);
  enfileirar(&F, 20);
  enfileirar(&F, 30);

  Elemento e;
  while (desenfileirar(&F, &e))
    printf("desenfileirar -> %d\n", e); // 10, depois 20, depois 30

  // 3) Ordenação por distribuição (Radix LSD) com m filas (base 10)
  int A[] = {802, 24, 2, 66, 170, 45, 75, 90};
  size_t n = sizeof A / sizeof *A;
  printf("antes : ");
  print_v(A, n);
  radix_lsd_com_filas(A, n, 10);
  printf("depois: ");
  print_v(A, n);

  return 0;
}
