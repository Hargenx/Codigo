#include <stdio.h>

int main(void) {
  int v[8];
  int *p = v; // ponteiro para o início
  int pares = 0, impares = 0;

  puts("Digite 8 inteiros:");
  for (int i = 0; i < 8; i++) {
    printf("v[%d]: ", i);
    scanf("%d", &v[i]);
  }

  // percorre só com ponteiro
  for (int i = 0; i < 8; i++, p++) {
    if ((*p % 2) == 0)
      pares++;
    else
      impares++;
  }

  printf("\nPares: %d | Impares: %d\n", pares, impares);
  return 0;
}
