// enfileirar.c  — demo só de enfileirar (fila circular sequencial, C11)
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
  if ((f->inicio == 0 && f->fim == MAX_FILA - 1) || (f->fim + 1 == f->inicio)) {
    return 0; // cheia
  }
  if (f->inicio == -1) {
    f->inicio = f->fim = 0; // estava vazia
  } else if (f->fim == MAX_FILA - 1) {
    f->fim = 0; // wrap
  } else {
    f->fim++;
  }
  f->v[f->fim] = e;
  return 1;
}

/* só para visualizar */
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

  int dados[] = {10, 20, 30, 40, 50};
  size_t m = sizeof(dados) / sizeof(dados[0]);

  for (size_t i = 0; i < m; ++i) {
    if (enfileirar(&F, dados[i]))
      printf("enfileirar(%d) OK\n", dados[i]);
    else
      printf("enfileirar(%d) OVERFLOW\n", dados[i]);
    fila_dump(&F);
  }

  if (!enfileirar(&F, 60))
    puts("overflow detectado ao tentar 60");
  return 0;
}
