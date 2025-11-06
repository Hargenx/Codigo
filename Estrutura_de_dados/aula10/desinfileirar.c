// desenfileirar.c  — fila circular sequencial (apenas desenfileirar)
#include <stdio.h>

#define MAX_FILA 5
typedef int Elemento;

typedef struct {
  Elemento v[MAX_FILA];
  int inicio; // -1 = vazia
  int fim;    // -1 = vazia
} Fila;

/* -------- apenas para o demo: preenche manualmente -------- */
static void fila_preenche_demo(Fila *f) {
  // vamos simular wrap-around: [ 40, 50, 60 ] começando no índice 3
  f->v[3] = 40;
  f->v[4] = 50;
  f->v[0] = 60;
  f->inicio = 3; // aponta p/ 40
  f->fim = 0;    // último é 60 (índice 0)
}

/* -------- FUNÇÃO PEDIDA: desenfileirar --------
   Retorna 1 (ok, valor em *out) ou 0 (fila vazia). */
int desenfileirar(Fila *f, Elemento *out) {
  if (f->inicio == -1)
    return 0; // vazia

  *out = f->v[f->inicio];    // lê
  if (f->inicio == f->fim) { // ficou vazia
    f->inicio = f->fim = -1;
  } else if (f->inicio == MAX_FILA - 1) { // wrap-around
    f->inicio = 0;
  } else {
    f->inicio++;
  }
  return 1;
}

/* -------- demo mínimo só com desenfileirar -------- */
int main(void) {
  Fila F = {.inicio = -1, .fim = -1};
  fila_preenche_demo(&F);

  Elemento x;
  while (desenfileirar(&F, &x))
    printf("desenfileirar -> %d\n", x); // 40, 50, 60

  if (!desenfileirar(&F, &x))
    puts("fila vazia (underflow).");
  return 0;
}
