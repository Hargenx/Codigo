#include <stdio.h>

int main(void) {
  int numeros[5];
  int contador = 0;

  printf("Digite 5 numeros inteiros:\n");
  for (int i = 0; i < 5; i++) {
    printf("Numero %d: ", i + 1);
    scanf("%d", &numeros[i]);
    if (numeros[i] > 100) {
      contador++;
    }
  }

  printf("\nQuantidade de numeros maiores que 100: %d\n", contador);
  return 0;
}
