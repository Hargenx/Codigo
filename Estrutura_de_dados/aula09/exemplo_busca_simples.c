/* busca.c */
#include <stdio.h>

typedef struct {
  int chave; /* ...outros campos opcionalmente... */
} Item;

int buscar(const Item lista[], int n, int chave) {
  for (int i = 0; i < n; i++) {
    if (lista[i].chave == chave)
      return i;
  }
  return -1; // não encontrado
}

int main(void) {
  Item v[5] = {{5}, {8}, {13}, {21}, {34}};
  int n = 5;

  printf("buscar 21 -> %d\n", buscar(v, n, 21)); // 3
  printf("buscar 99 -> %d\n", buscar(v, n, 99)); // -1
  return 0;
}
/* compile: gcc busca.c -std=c11 -Wall -Wextra -O2 -o busca */
