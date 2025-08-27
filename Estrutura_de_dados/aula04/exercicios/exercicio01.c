#include <stdio.h>

int main() {
  int m = 10; // variável inteira
  int n, o;   // outras variáveis inteiras
  int *z;     // ponteiro para inteiro

  z = &m; // z guarda o endereço de m

  printf(" Ponteiro: Exibindo declaracao basica de ponteiro:\n");
  printf("-------------------------------------------------------\n");
  printf(" Aqui esta m=%d, n e o sao duas variaveis inteiras e *z e um inteiro\n\n", m);

  printf(" z armazena o endereco de m = %p\n\n", (void *)z);
  printf(" *z armazena o valor de m = %d\n\n", *z);
  printf(" &m e o endereco de m = %p\n\n", (void *)&m);
  printf(" &n armazena o endereco de n = %p\n\n", (void *)&n);
  printf(" &o armazena o endereco de o = %p\n\n", (void *)&o);
  printf(" &z armazena o endereco de z = %p\n\n", (void *)&z);

  return 0;
}
