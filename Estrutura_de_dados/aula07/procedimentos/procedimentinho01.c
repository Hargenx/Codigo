#include <stdio.h>

// Procedimento que imprime uma linha de separação
void linha(void) { printf("-----------\n"); }

int main(void) {
  printf("Antes da linha\n");
  linha(); // apenas executa, não retorna valor
  printf("Depois da linha\n");
  return 0;
}
