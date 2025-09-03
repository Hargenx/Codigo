#include <stdio.h>

int main(void) {
  float matriz[4][4];
  float somaImpares = 0.0, somaPares = 0.0;
  int countPares = 0;

  printf("Digite os elementos da matriz 4x4:\n");
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      printf("Elemento [%d][%d]: ", i, j);
      scanf("%f", &matriz[i][j]);

      if (j % 2 == 0) { // coluna ímpar (0,2,...)
        somaImpares += matriz[i][j];
      } else { // coluna par (1,3,...)
        somaPares += matriz[i][j];
        countPares++;
      }
    }
  }

  printf("\nSoma dos elementos das colunas impares: %.2f\n", somaImpares);
  if (countPares > 0) {
    printf("Media aritmetica das colunas pares: %.2f\n",
           somaPares / countPares);
  }

  return 0;
}
