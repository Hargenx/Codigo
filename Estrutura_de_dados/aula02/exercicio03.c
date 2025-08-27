#include <stdio.h>

int main(void) {
  double val_dolar, cotacao, val_real;

  printf("Informe a quantidade de dolares no cofre: ");
  if (scanf("%lf", &val_dolar) != 1) {
    printf("Entrada invalida.\n");
    return 1;
  }

  printf("Informe a cotacao do dolar (em R$): ");
  if (scanf("%lf", &cotacao) != 1) {
    printf("Entrada invalida.\n");
    return 1;
  }

  if (val_dolar < 0 || cotacao < 0) {
    printf("Valores nao podem ser negativos.\n");
    return 1;
  }

  val_real = val_dolar * cotacao;

  printf("\nValor em reais: R$ %.2f\n", val_real);
  return 0;
}
