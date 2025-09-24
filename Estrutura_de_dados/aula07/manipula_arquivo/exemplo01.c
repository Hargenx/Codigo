#include <stdio.h>
#include <stdlib.h>

int main(void) {
  FILE *arquivo;
  char nome[50];
  float nota;

  // --- 1) Abrindo arquivo para escrita ("w" sobrescreve se já existir)
  arquivo = fopen("notas.txt", "w");
  if (arquivo == NULL) {
    perror("Erro ao abrir arquivo para escrita");
    return 1;
  }

  // --- 2) Escrevendo no arquivo
  printf("Digite o nome do aluno: ");
  fgets(nome, sizeof nome, stdin);

  printf("Digite a nota do aluno: ");
  if (scanf("%f", &nota) != 1) {
    fprintf(stderr, "Entrada invalida!\n");
    fclose(arquivo);
    return 1;
  }

  // grava no arquivo (nome e nota)
  fprintf(arquivo, "Nome: %sNota: %.1f\n", nome, nota);
  fclose(arquivo);
  printf("\nDados gravados em 'notas.txt'\n");

  // --- 3) Abrindo arquivo para leitura ("r")
  arquivo = fopen("notas.txt", "r");
  if (arquivo == NULL) {
    perror("Erro ao abrir arquivo para leitura");
    return 1;
  }

  // --- 4) Lendo e exibindo o conteúdo do arquivo
  char linha[100];
  printf("\n--- Conteudo do arquivo ---\n");
  while (fgets(linha, sizeof linha, arquivo)) {
    printf("%s", linha);
  }
  fclose(arquivo);

  return 0;
}
