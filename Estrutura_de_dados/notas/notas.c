#include <stdio.h>
#include <string.h>

float av(float nota) { return nota; }

int main() {
  char aluno[50] = "Nome";
  float nota = av(8.5);

  printf("A nota do aluno %s foi %.1f\n", aluno, nota);
  printf("Prova teórica com valor total de 5 (cinco) pontos;\n");
  printf("Trabalho com o valor total de 5 (cinco) pontos.\n");

  return 0;
}

