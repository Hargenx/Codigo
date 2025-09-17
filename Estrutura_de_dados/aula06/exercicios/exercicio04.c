#include <stdio.h>
#include <string.h>

enum { MAX_NOME = 60, MAX_CURSO = 40, MAX_ALUNOS = 4 };

typedef struct {
  char nome[MAX_NOME];
  char curso[MAX_CURSO];
  float cr;
} Aluno;

static void ler_linha(char *b, size_t t) {
  if (fgets(b, (int)t, stdin)) {
    size_t n = strlen(b);
    if (n && b[n - 1] == '\n')
      b[n - 1] = '\0';
  }
}

int main(void) {
  // vetor (heterogênea)
  Aluno turma[MAX_ALUNOS] = {{"Raphael Mauricio", "Computacao", 8.6f},
                             {"Ikit Claw", "Engenharia", 7.9f},
                             {"Teclis", "Matematica", 9.2f},
                             {"Balthasar Gelt", "Fisica", 6.8f}};

  // matriz (homogênea) apenas para ilustrar impressão
  int M[2][3] = {{1, 2, 3}, {4, 5, 6}};
  puts("Matriz 2x3:");
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++)
      printf("%3d ", M[i][j]);
    puts("");
  }

  // busca por nome
  char chave[MAX_NOME];
  printf("\nNome a buscar: ");
  ler_linha(chave, sizeof chave);

  int pos = -1;
  for (int i = 0; i < MAX_ALUNOS; i++) {
    if (strcmp(chave, turma[i].nome) == 0) {
      pos = i;
      break;
    }
  }

  if (pos >= 0) {
    printf("Encontrado: %s | Curso: %s | CR: %.1f\n", turma[pos].nome,
           turma[pos].curso, turma[pos].cr);
  } else {
    puts("Aluno nao encontrado.");
  }

  return 0;
}
