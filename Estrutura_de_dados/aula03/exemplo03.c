#include <stdio.h>

// Variável global com alocação estática
static int a = 0;

void incrementa(void) {
  int b = 0;        // variável local automática (é recriada a cada chamada)
  static int c = 0; // variável local estática (mantém valor entre chamadas)

  printf("a: %d, b: %d, c: %d\n", a, b, c);

  a++; // persiste, porque é global estática
  b++; // não persiste, é recriada com 0 a cada chamada
  c++; // persiste entre chamadas, pois é estática local
}

int main(void) {
  for (int i = 0; i < 5; i++) {
    incrementa();
  }
  return 0;
}
