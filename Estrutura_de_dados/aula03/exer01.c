#include <stdio.h>

// Definição do tipo struct Data
typedef struct {
  int dia;
  int mes;
  int ano;
} Data;

int main(void) {
  printf("sizeof(Data) = %zu bytes\n", sizeof(Data));
  return 0;
}
