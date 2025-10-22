// pilha_seq.c
#include <stdio.h>

#define MAX_PILHA 100
typedef int Elemento;

typedef struct {
  Elemento v[MAX_PILHA];
  int topo; // -1 = vazia; 0..MAX_PILHA-1 = índice do topo
} Pilha;

void pilha_init(Pilha *p) { p->topo = -1; }

int push(Pilha *p, Elemento e) {
  if (p->topo < MAX_PILHA - 1) { // ainda há espaço
    p->v[++p->topo] = e;         // incrementa e grava
    return 1;                    // sucesso
  }
  return 0; // overflow
}

/* Demo rápida */
int main(void) {
  Pilha P;
  pilha_init(&P);
  push(&P, 10);
  push(&P, 20);
  push(&P, 30);

  for (int i = 0; i <= P.topo; ++i)
    printf("%d ", P.v[i]);
  puts("");
  return 0;
}
