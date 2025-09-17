#include <stdio.h>
#include <string.h>

enum { MAX_NOME = 200, MAX_DISC = 100 };

typedef struct {
  char nome[MAX_NOME];
  char disciplina[MAX_DISC];
  float nota;
} Aluno;

static void ler_linha(char *buf, size_t tam) {
  if (fgets(buf, (int)tam, stdin)) {
    size_t n = strlen(buf);
    if (n && buf[n - 1] == '\n')
      buf[n - 1] = '\0';
  }
}

int main(void) {
  Aluno aluno_nota[10] = {0}; // todos os campos já ficam em '\0' ou 0.0
  for (int i = 0; i < 10; i++) {
    printf("Digite nome do aluno: ");
    ler_linha(aluno_nota[i].nome, sizeof aluno_nota[i].nome);

    printf("Digite a disciplina do aluno: ");
    ler_linha(aluno_nota[i].disciplina, sizeof aluno_nota[i].disciplina);

    printf("Digite a nota do aluno: ");
    while (scanf("%f", &aluno_nota[i].nota) != 1) {
      puts("Entrada inválida. Tente novamente:");
      int c;
      while ((c = getchar()) != '\n' && c != EOF) {
      }
    }
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {
    } // limpa buffer
  }

  puts("\n--- Resumo ---");
  for (int i = 0; i < 10; i++) {
    printf("%d) %s - %s: %.1f\n", i + 1, aluno_nota[i].nome,
           aluno_nota[i].disciplina, aluno_nota[i].nota);
  }
  return 0;
}
