for (int i = 0; i < TAM; i++) {
  if (strcmp(nomeBuscado, vetor[i].nome) == 0) {
    printf("Aluno encontrado: %s\n", vetor[i].nome);
    // aqui pode exibir os outros campos também
    break;
  }
}
