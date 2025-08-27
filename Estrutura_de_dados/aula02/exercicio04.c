#include <stdio.h>

// Função para calcular a média aritmética de três notas
float calcular_media(float n1, float n2, float n3) {
  float soma = n1 + n2 + n3;
  return soma / 3; // sem parênteses extras, ordem natural das operações
}

int main(void) {
  float nota1 = 8.0;
  float nota2 = 3.5;
  float nota3 = 6.0;
  float media;

  media = calcular_media(nota1, nota2, nota3);

  printf("\nSua media eh: %.2f\n", media);

  return 0;
}
