#include <stdio.h>
#include <string.h>

enum { MAX_NOME = 60, MAX_DATA = 11, MAX_CURSO = 40 };

typedef struct {
  int matricula;
  char nome[MAX_NOME];
  char dataNasc[MAX_DATA]; // dd/mm/aaaa
  char curso[MAX_CURSO];
  float cr;
} Aluno;

/* lê linha com espaços e remove '\n' se existir */
static void le_linha(char *buf, size_t tam) {
  if (fgets(buf, (int)tam, stdin)) {
    size_t n = strlen(buf);
    if (n && buf[n - 1] == '\n')
      buf[n - 1] = '\0';
  }
}

/* descarta resto da linha (para usar após scanf de números) */
static void limpa_buffer(void) {
  int c;
  while ((c = getchar()) != '\n' && c != EOF) {
  }
}

int main(void) {
  Aluno a = {0};

  printf("Matricula: ");
  while (scanf("%d", &a.matricula) != 1) {
    printf("Valor invalido. Tente novamente: ");
    limpa_buffer();
  }
  limpa_buffer(); // consume '\n'

  printf("Nome: ");
  le_linha(a.nome, sizeof a.nome);

  printf("Data de nascimento (dd/mm/aaaa): ");
  le_linha(a.dataNasc, sizeof a.dataNasc);

  printf("Curso: ");
  le_linha(a.curso, sizeof a.curso);

  printf("CR: ");
  while (scanf("%f", &a.cr) != 1) {
    printf("Valor invalido. Tente novamente: ");
    limpa_buffer();
  }

  puts("\n--- Dados do Aluno ---");
  printf("Nome:       %s\n", a.nome);
  printf("Matricula:  %d\n", a.matricula);
  printf("Nascimento: %s\n", a.dataNasc);
  printf("Curso:      %s\n", a.curso);
  printf("CR:         %.1f\n", a.cr);
  return 0;
}
