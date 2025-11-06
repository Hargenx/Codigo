// fila_enfileirar_apenas.c
#include <stdio.h>

#define MAX_FILA 5
typedef int Elemento;

typedef struct {
  Elemento v[MAX_FILA];
  int inicio; // -1 = vazia
  int fim;    // -1 = vazia
} Fila;

void fila_init(Fila *f) { f->inicio = f->fim = -1; }

/* Retorna 1 (ok) ou 0 (overflow) */
int enfileirar(Fila *f, Elemento e) {
  /* cheia? (fim encostando no inicio, considerando wrap) */
  if ((f->inicio == 0 && f->fim == MAX_FILA - 1) || (f->fim + 1 == f->inicio)) {
    return 0;
  }

  if (f->inicio == -1) { // estava vazia
    f->inicio = f->fim = 0;
  } else if (f->fim == MAX_FILA - 1) {
    f->fim = 0; // wrap-around
  } else {
    f->fim++;
  }

  f->v[f->fim] = e;
  return 1;
}

/* só pra visualizar o estado atual da fila */
void fila_dump(const Fila *f) {
  if (f->inicio == -1) {
    puts("[]");
    return;
  }
  printf("[");
  int i = f->inicio;
  while (1) {
    printf("%d", f->v[i]);
    if (i == f->fim)
      break;
    i = (i + 1) % MAX_FILA;
    printf(" ");
  }
  puts("]");
}

int main(void) {
  Fila F;
  fila_init(&F);

  for (int x : (int[]){10, 20, 30, 40, 50}) {
    if (enfileirar(&F, x))
      printf("enfileirar(%d) OK\n", x);
    else
      printf("enfileirar(%d) OVERFLOW\n", x);
    fila_dump(&F);
  }

  /* tenta enfileirar além da capacidade pra mostrar overflow */
  if (!enfileirar(&F, 60))
    puts("overflow detectado ao tentar 60");

  return 0;
}
