#include <stdio.h>
#include <string.h>

enum { MAX_NOME = 60, MAX_CURSO = 40, MAX_ALUNOS = 5 };

typedef struct {
  char nome[MAX_NOME];
  char curso[MAX_CURSO];
  float cr;
} Aluno;

static void ler_linha(char *buf, size_t tam) {
  if (fgets(buf, (int)tam, stdin)) {
    size_t n = strlen(buf);
    if (n && buf[n - 1] == '\n')
      buf[n - 1] = '\0';
  }
}

static void limpa_buffer(void) {
  int c;
  while ((c = getchar()) != '\n' && c != EOF) {
  }
}

int main(void) {
  int N;
  Aluno a[MAX_ALUNOS];

  do {
    printf("Quantos alunos (1..5)? ");
    if (scanf("%d", &N) != 1) {
      limpa_buffer();
      N = 0;
    }
  } while (N < 1 || N > MAX_ALUNOS);
  limpa_buffer();

  for (int i = 0; i < N; i++) {
    printf("\nAluno %d\n", i + 1);
    printf("Nome: ");
    ler_linha(a[i].nome, sizeof a[i].nome);
    printf("Curso: ");
    ler_linha(a[i].curso, sizeof a[i].curso);

    printf("CR: ");
    while (scanf("%f", &a[i].cr) != 1) {
      puts("Valor invalido. Tente novamente:");
      limpa_buffer();
    }
    limpa_buffer();
  }

  int idx = 0;
  for (int i = 1; i < N; i++)
    if (a[i].cr > a[idx].cr)
      idx = i;

  printf("\nMelhor CR: %.2f\nAluno: %s (%s)\n", a[idx].cr, a[idx].nome,
         a[idx].curso);
  return 0;
}
