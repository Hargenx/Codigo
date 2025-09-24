#include <stdbool.h>
#include <stdio.h>


// Função: retorna true se n é primo
bool eh_primo(int n) {
  if (n < 2)
    return false;
  for (int i = 2; i * i <= n; i++) {
    if (n % i == 0)
      return false;
  }
  return true;
}

// Procedimento: imprime o resultado
void mostra_resultado(int n) {
  if (eh_primo(n))
    printf("%d é primo.\n", n);
  else
    printf("%d não é primo.\n", n);
}

int main(void) {
  int numero;
  printf("Digite um numero: ");
  scanf("%d", &numero);
  mostra_resultado(numero);
  return 0;
}
