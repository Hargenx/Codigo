#include "calculadora.h"

int somar(int a, int b) { return a + b; }

int subtrair(int a, int b) { return a - b; }

int multiplicar(int a, int b) { return a * b; }

float dividir(int a, int b) {
  if (b == 0) {
    return 0; // Simples tratamento de erro
  }
  return (float)a / b;
}
