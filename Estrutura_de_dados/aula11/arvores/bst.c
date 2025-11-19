#include <stdio.h>
#include <stdlib.h>

/* Nó da árvore binária de busca */
typedef struct No {
  int chave;
  struct No *filho_esquerdo;
  struct No *filho_direito;
} No;

/* ---------- BUSCA (versão iterativa) ----------
   Retorna 1 se encontrar a chave; 0 caso contrário.
   Complexidade: O(h), onde h é a altura da árvore. */
int busca_arvore(int chave, const No *ptr) {
  while (ptr != NULL) {
    if (ptr->chave == chave)
      return 1; /* chave encontrada */
    else if (chave < ptr->chave)
      ptr = ptr->filho_esquerdo; /* vai à esquerda */
    else
      ptr = ptr->filho_direito; /* vai à direita  */
  }
  return 0; /* chave não encontrada */
}

/* --- Abaixo, apenas um pequeno demo opcional --- */
static No *novo_no(int chave) {
  No *n = (No *)malloc(sizeof *n);
  if (!n)
    return NULL;
  n->chave = chave;
  n->filho_esquerdo = n->filho_direito = NULL;
  return n;
}

int main(void) {
  /* Monta manualmente uma BST pequena:
           8
          / \
         3   10
        / \    \
       1   6    14
  */
  No *raiz = novo_no(8);
  raiz->filho_esquerdo = novo_no(3);
  raiz->filho_direito = novo_no(10);
  raiz->filho_esquerdo->filho_esquerdo = novo_no(1);
  raiz->filho_esquerdo->filho_direito = novo_no(6);
  raiz->filho_direito->filho_direito = novo_no(14);

  printf("Busca 6:  %s\n",
         busca_arvore(6, raiz) ? "encontrou" : "não encontrou");
  printf("Busca 13: %s\n",
         busca_arvore(13, raiz) ? "encontrou" : "não encontrou");

  /* (omiti free para brevidade) */
  return 0;
}
