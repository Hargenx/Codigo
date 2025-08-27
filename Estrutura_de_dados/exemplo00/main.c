#include "calculadora.h"
#include <stdio.h>


int main() {
  int x = 10, y = 5;

  printf("Soma: %d\n", somar(x, y));
  printf("Subtração: %d\n", subtrair(x, y));
  printf("Multiplicação: %d\n", multiplicar(x, y));
  printf("Divisão: %.2f\n", dividir(x, y));

  return 0;
}
