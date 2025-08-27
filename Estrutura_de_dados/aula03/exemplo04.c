#include <stdio.h>

// Função com dois ponteiros simples
void exemplo_um(void) {
  int a = 10, b = 20, c;
  int *p, *q;

  p = &a; // p aponta para a
  q = &b; // q aponta para b

  c = *p + *q; // soma os valores apontados

  printf("=== Exemplo 1: Ponteiros Simples ===\n");
  printf("a = %d, b = %d\n", a, b);
  printf("*p = %d, *q = %d\n", *p, *q);
  printf("c = *p + *q = %d\n\n", c);
}

// Função com ponteiro para ponteiro
void exemplo_dois(void) {
  int a = 15, b = 25, c;
  int *p;
  int **r;

  p = &a; // p aponta para a
  r = &p; // r aponta para p (logo, **r acessa a)

  c = **r + b; // soma o valor de a (via **r) com b

  printf("=== Exemplo 2: Ponteiro para Ponteiro ===\n");
  printf("a = %d, b = %d\n", a, b);
  printf("*p = %d, **r = %d\n", *p, **r);
  printf("c = **r + b = %d\n", c);
}

int main(void) {
  exemplo_um();
  exemplo_dois();
  return 0;
}
