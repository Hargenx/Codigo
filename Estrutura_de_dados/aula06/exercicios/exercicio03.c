#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int N;
  printf("Quantos valores (1..100)? ");
  if (scanf("%d", &N) != 1 || N < 1 || N > 100) {
    puts("Entrada invalida.");
    return 1;
  }

  double *v = (double *)malloc((size_t)N * sizeof *v);
  if (!v) {
    puts("Memoria insuficiente.");
    return 1;
  }

  for (int i = 0; i < N; i++) {
    printf("v[%d]: ", i);
    scanf("%lf", &v[i]);
  }

  double soma = 0.0;
  for (double *p = v; p < v + N; p++)
    soma += *p;

  printf("\nMedia = %.1f\n", soma / N);
  free(v);
  return 0;
}
