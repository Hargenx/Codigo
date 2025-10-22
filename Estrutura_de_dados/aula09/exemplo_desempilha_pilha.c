// pilha_pop_demo.c
#include <stdio.h>

#define MAX_PILHA 100
typedef int Elemento;

typedef struct {
  Elemento v[MAX_PILHA];
  int topo; // -1 = vazia
} Pilha;

/* pop: 1 = ok (valor em *out); 0 = underflow */
int pop(Pilha *p, Elemento *out) {
  if (p->topo >= 0) {
    *out = p->v[p->topo--];
    return 1;
  }
  return 0;
}

/* peek: 1 = ok (valor em *out); 0 = vazia */
int peek(const Pilha *p, Elemento *out) {
  if (p->topo >= 0) {
    *out = p->v[p->topo];
    return 1;
  }
  return 0;
}

int main(void) {
  Pilha P;

  /* --- pré-carrega a pilha sem usar push --- */
  P.v[0] = 10;
  P.v[1] = 20;
  P.v[2] = 30;
  P.topo = 2; // topo em v[2] = 30

  Elemento x;

  if (peek(&P, &x))
    printf("Topo (peek) = %d\n", x); // 30

  /* usando apenas pop */
  while (pop(&P, &x)) {
    printf("pop -> %d\n", x); // 30, 20, 10
  }

  /* tentar pop em pilha vazia */
  if (!pop(&P, &x))
    puts("Underflow: pilha vazia.");
  return 0;
}
