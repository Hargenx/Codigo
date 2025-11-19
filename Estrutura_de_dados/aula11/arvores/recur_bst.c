int busca_arvore_rec(int chave, const No *ptr) {
  if (!ptr)
    return 0;
  if (chave == ptr->chave)
    return 1;
  return (chave < ptr->chave) ? busca_arvore_rec(chave, ptr->filho_esquerdo)
                              : busca_arvore_rec(chave, ptr->filho_direito);
}
