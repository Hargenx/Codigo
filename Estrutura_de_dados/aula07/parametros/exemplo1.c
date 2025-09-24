#include <stdio.h>

// Passagem por valor
void por_valor(int x) { x = x + 10; }

// Passagem por "referência" usando ponteiro
void por_referencia(int *x) { *x = *x + 10; }

int main(void) {
  int a = 5, b = 5;

  por_valor(a);
  por_referencia(&b);

  printf("a (por valor) = %d\n", a);      // continua 5
  printf("b (por referencia) = %d\n", b); // vira 15

  return 0;
}
