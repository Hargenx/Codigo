#include <stdio.h>
#include <string.h>

enum { MAX_NOME = 200, MAX_DISC = 100 };

typedef struct {
    char  nome[MAX_NOME];
    char  disciplina[MAX_DISC];
    float nota;
} Aluno;

int main(void) {
    Aluno aluno_nota[10]; // vetor de 10 alunos

    // Exemplo simples de uso: leitura do 1º aluno
    printf("Nome: ");
    fgets(aluno_nota[0].nome, sizeof aluno_nota[0].nome, stdin);
    aluno_nota[0].nome[strcspn(aluno_nota[0].nome, "\n")] = '\0';

    printf("Disciplina: ");
    fgets(aluno_nota[0].disciplina, sizeof aluno_nota[0].disciplina, stdin);
    aluno_nota[0].disciplina[strcspn(aluno_nota[0].disciplina, "\n")] = '\0';

    printf("Nota: ");
    scanf("%f", &aluno_nota[0].nota);

    puts("\n--- Dados ---");
    printf("Nome: %s\n", aluno_nota[0].nome);
    printf("Disciplina: %s\n", aluno_nota[0].disciplina);
    printf("Nota: %.1f\n", aluno_nota[0].nota);

    return 0;
}
