#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>


enum { MAX_NOME = 60, MAX_DATA = 11, MAX_CURSO = 40 };

typedef struct {
  int matricula;
  char nome[MAX_NOME];
  char dataNasc[MAX_DATA]; // "dd/mm/aaaa" (10 + '\0')
  char curso[MAX_CURSO];
  float cr;
} Aluno;

/*-------------------- utilitários de entrada --------------------*/

static void descarta_ate_fim_de_linha(void) {
  int c;
  while ((c = getchar()) != '\n' && c != EOF) { /* nada */
  }
}

static void rstrip(char *s) { // remove espaços/quebras à direita
  size_t n = strlen(s);
  while (n && isspace((unsigned char)s[n - 1]))
    s[--n] = '\0';
}

static void lstrip(char *s) { // remove espaços à esquerda
  size_t i = 0, n = strlen(s);
  while (i < n && isspace((unsigned char)s[i]))
    i++;
  if (i)
    memmove(s, s + i, n - i + 1);
}

static void trim(char *s) {
  lstrip(s);
  rstrip(s);
}

/* Lê uma linha (com espaços) e corta o '\n' se existir */
static int le_linha(char *buf, size_t tam) {
  if (!fgets(buf, (int)tam, stdin))
    return 0;
  rstrip(buf);
  return 1;
}

/* Lê int com validação e limpa o buffer */
static void le_int(const char *prompt, int *out) {
  for (;;) {
    printf("%s", prompt);
    if (scanf("%d", out) == 1) {
      descarta_ate_fim_de_linha();
      return;
    }
    puts("Entrada invalida. Digite um inteiro.");
    descarta_ate_fim_de_linha();
  }
}

/* Lê float com validação e limpa o buffer */
static void le_float(const char *prompt, float *out) {
  for (;;) {
    printf("%s", prompt);
    if (scanf("%f", out) == 1) {
      descarta_ate_fim_de_linha();
      return;
    }
    puts("Entrada invalida. Digite um numero real.");
    descarta_ate_fim_de_linha();
  }
}

/*-------------------- validação de data dd/mm/aaaa --------------------*/

static bool ano_bissexto(int y) {
  return (y % 400 == 0) || ((y % 4 == 0) && (y % 100 != 0));
}

static bool valida_data_str(const char *s) {
  int d, m, a;
  if (sscanf(s, "%2d/%2d/%4d", &d, &m, &a) != 3)
    return false;
  if (a < 1900 || a > 2100 || m < 1 || m > 12 || d < 1)
    return false;

  int dias_mes[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  if (m == 2 && ano_bissexto(a))
    dias_mes[2] = 29;
  return d <= dias_mes[m];
}

/* Lê string não vazia */
static void le_linha_nao_vazia(const char *prompt, char *dest, size_t tam) {
  for (;;) {
    printf("%s", prompt);
    if (!le_linha(dest, tam))
      continue;
    trim(dest);
    if (dest[0] != '\0')
      break;
    puts("Campo vazio. Tente novamente.");
  }
}

/* Lê data válida dd/mm/aaaa */
static void le_data(const char *prompt, char *dest, size_t tam) {
  for (;;) {
    printf("%s", prompt);
    if (!le_linha(dest, tam))
      continue;
    trim(dest);
    if (valida_data_str(dest))
      break;
    puts("Data invalida. Formato esperado: dd/mm/aaaa.");
  }
}

/*-------------------- programa principal --------------------*/

int main(void) {
  Aluno aluno = {0};

  le_int("Digite a matricula: ", &aluno.matricula);
  le_linha_nao_vazia("Digite o nome: ", aluno.nome, sizeof aluno.nome);
  le_data("Digite a Data de Nascimento (dd/mm/aaaa): ", aluno.dataNasc,
          sizeof aluno.dataNasc);
  le_linha_nao_vazia("Digite o curso: ", aluno.curso, sizeof aluno.curso);
  le_float("Digite o CR: ", &aluno.cr);

  puts("\n--- Dados do Aluno ---");
  printf("Nome:        %s\n", aluno.nome);
  printf("Matricula:   %d\n", aluno.matricula);
  printf("Nascimento:  %s\n", aluno.dataNasc);
  printf("Curso:       %s\n", aluno.curso);
  printf("CR:          %.1f\n", aluno.cr);

  return 0;
}
