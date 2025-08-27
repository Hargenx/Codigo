#include <stdio.h>

int main() {
  int n, i;
  unsigned long long fatorial = 1;

  printf("Digite um número positivo: ");
  scanf("%d", &n);

  if (n < 0) {
    printf("Fatorial não definido para negativos.\n");
  } else {
    for (i = 1; i <= n; i++) {
      fatorial *= i;
    }
    printf("Fatorial de %d é %llu\n", n, fatorial);
  }

  return 0;
}
