// fila_enfileirar_dinamica.c
#include <stdio.h>
#include <stdlib.h>

typedef int Elemento;

typedef struct No {
  Elemento elemento;
  struct No *prox;
} No;

typedef struct {
  No *inicio; // NULL = vazia
  No *fim;    // NULL = vazia
  size_t tam; // opcional
} Fila;

void fila_init(Fila *f) {
  f->inicio = f->fim = NULL;
  f->tam = 0;
}

/* --- ENFILEIRAR (dinâmico encadeado) ---
   Retorna 1 (ok) ou 0 (falha de memória). */
int enfileirar(Fila *f, Elemento e) {
  No *novo = malloc(sizeof *novo);
  if (!novo)
    return 0;
  novo->elemento = e;
  novo->prox = NULL;

  if (f->fim) {          // havia elementos
    f->fim->prox = novo; // liga antigo fim -> novo
  } else {               // fila estava vazia
    f->inicio = novo;
  }
  f->fim = novo;
  f->tam++;
  return 1;
}

/* utilitário: imprime a fila */
void fila_dump(const Fila *f) {
  const No *p = f->inicio;
  printf("Fila(%zu): [", f->tam);
  while (p) {
    printf("%d", p->elemento);
    p = p->prox;
    if (p)
      printf(" -> ");
  }
  puts("]");
}

/* utilitário: libera memória de todos os nós */
void fila_clear(Fila *f) {
  No *p = f->inicio;
  while (p) {
    No *nx = p->prox;
    free(p);
    p = nx;
  }
  f->inicio = f->fim = NULL;
  f->tam = 0;
}

int main(void) {
  Fila F;
  fila_init(&F);

  int dados[] = {10, 20, 30, 40};
  for (size_t i = 0; i < sizeof dados / sizeof *dados; ++i) {
    if (!enfileirar(&F, dados[i])) {
      puts("Falha de memoria ao enfileirar.");
      break;
    }
    fila_dump(&F);
  }

  fila_clear(&F);
  return 0;
}
