#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>


int main(void) {
  int i = 1234;

  printf("i = %d\n", i);

  // Forma correta/portável de imprimir um endereço:
  printf("&i = %p\n", (void *)&i);

  // (Opcional) endereço como número hexadecimal, de forma portável:
  uintptr_t addr = (uintptr_t)(void *)&i;
  printf("Endereco numerico (hex) = 0x%" PRIxPTR "\n", addr);

  // Informativo:
  printf("sizeof(int) = %zu, sizeof(void*) = %zu\n", sizeof i, sizeof(void *));
  return 0;
}
