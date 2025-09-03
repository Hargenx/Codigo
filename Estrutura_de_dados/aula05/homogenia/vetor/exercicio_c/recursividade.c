#include <stdio.h>

int lerEContar(int vetor[], int n) {
  if (n == 0)
    return 0; // caso base
  printf("Digite um numero: ");
  scanf("%d", &vetor[n - 1]);
  return (vetor[n - 1] > 100 ? 1 : 0) + lerEContar(vetor, n - 1);
}

int main(void) {
  int numeros[5];
  int qtd = lerEContar(numeros, 5);
  printf("\nQuantidade de numeros maiores que 100: %d\n", qtd);
  return 0;
}
