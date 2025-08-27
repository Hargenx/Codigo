#include <stdio.h>

void somaPorReferencia(int *a, int *b, int *resultado) { *resultado = *a + *b; }

int main(void) {
  int primeiroNumero, segundoNumero, resultado;

  printf("Ponteiro: Adicionar dois numeros usando chamada por referencia:\n");
  printf("-------------------------------------------------------\n");

  printf("Digite o primeiro numero: ");
  scanf("%d", &primeiroNumero);

  printf("Digite o segundo numero: ");
  scanf("%d", &segundoNumero);

  somaPorReferencia(&primeiroNumero, &segundoNumero, &resultado);

  printf("A soma de %d e %d e %d\n", primeiroNumero, segundoNumero, resultado);

  return 0;
}
