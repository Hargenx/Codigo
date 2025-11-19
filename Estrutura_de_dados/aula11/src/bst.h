/* bst.h */
#ifndef BST_H
#define BST_H

#include <stddef.h>

/* Tipo opaco: o usuário não vê a estrutura interna da BST */
typedef struct BST BST;

/* Cria árvore vazia. Retorna NULL se faltar memória. */
BST *bst_create(void);

/* Libera todos os nós e a própria árvore. Aceita NULL. */
void bst_free(BST *tree);

/* Insere uma chave.
   - Retorna 1 em caso de sucesso.
   - Retorna 0 se faltar memória.
   (Chaves duplicadas são ignoradas: não aumentam o tamanho.) */
int bst_insert(BST *tree, int key);

/* Retorna 1 se a chave está na árvore, 0 caso contrário. */
int bst_contains(const BST *tree, int key);

/* Número de elementos armazenados. */
size_t bst_size(const BST *tree);

/* Altura da árvore.
   - Árvore vazia: -1
   - Nó único (só raiz): 0
*/
int bst_height(const BST *tree);

/* Percorrimento em ordem (in-order).
   Chama visit(key, userdata) em ordem crescente de chave. */
void bst_inorder(const BST *tree, void (*visit)(int key, void *userdata),
                 void *userdata);

#endif /* BST_H */
