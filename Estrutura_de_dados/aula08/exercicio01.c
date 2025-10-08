#include <stdio.h>

#define PASSO 6.0f // média mínima para aprovação

// Função: calcula a nota final conforme as regras
float calcula_nota_final(int sm1, int sm2, float av, float avs) {
  if (avs > av)
    av = avs; // AVS substitui AV se maior
  float bonus = (sm1 ? 1.0f : 0.0f) + (sm2 ? 1.0f : 0.0f);
  float final = av + bonus;
  if (final > 10.0f)
    final = 10.0f; // nota não pode ultrapassar 10
  return final;
}

// Procedimento: imprime a situação do aluno
void mostra_resultado(float nota_final) {
  printf("\nNota final: %.2f\n", nota_final);
  if (nota_final >= PASSO) {
    puts("Situacao: APROVADO");
  } else {
    puts("Situacao: REPROVADO");
  }
}

int main(void) {
  int sm1, sm2;
  float av, avs;

  // Entradas com validação simples
  do {
    printf("SM1 (0 ou 1): ");
    if (scanf("%d", &sm1) != 1)
      return 1;
  } while (sm1 != 0 && sm1 != 1);

  do {
    printf("SM2 (0 ou 1): ");
    if (scanf("%d", &sm2) != 1)
      return 1;
  } while (sm2 != 0 && sm2 != 1);

  do {
    printf("AV (0..10): ");
    if (scanf("%f", &av) != 1)
      return 1;
  } while (av < 0.0f || av > 10.0f);

  do {
    printf("AVS (0..10): ");
    if (scanf("%f", &avs) != 1)
      return 1;
  } while (avs < 0.0f || avs > 10.0f);

  float nota_final = calcula_nota_final(sm1, sm2, av, avs);
  mostra_resultado(nota_final);
  return 0;
}
