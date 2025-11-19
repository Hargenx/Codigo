/* bst.c */
#include "bst.h"
#include <stdlib.h>

typedef struct Node {
  int key;
  struct Node *left;
  struct Node *right;
} Node;

struct BST {
  Node *root;
  size_t size;
};

BST *bst_create(void) {
  BST *t = (BST *)malloc(sizeof *t);
  if (!t)
    return NULL;
  t->root = NULL;
  t->size = 0;
  return t;
}

static void free_node(Node *n) {
  if (!n)
    return;
  free_node(n->left);
  free_node(n->right);
  free(n);
}

void bst_free(BST *tree) {
  if (!tree)
    return;
  free_node(tree->root);
  free(tree);
}

size_t bst_size(const BST *tree) { return tree ? tree->size : 0; }

/* Inserção recursiva em nó; added=1 se inseriu, 0 se chave já existia */
static int bst_insert_node(Node **pnode, int key, int *added) {
  Node *node = *pnode;
  if (!node) {
    node = (Node *)malloc(sizeof *node);
    if (!node)
      return 0;
    node->key = key;
    node->left = node->right = NULL;
    *pnode = node;
    *added = 1;
    return 1;
  }
  if (key < node->key) {
    return bst_insert_node(&node->left, key, added);
  } else if (key > node->key) {
    return bst_insert_node(&node->right, key, added);
  } else {
    /* chave duplicada: não insere de novo */
    *added = 0;
    return 1;
  }
}

int bst_insert(BST *tree, int key) {
  if (!tree)
    return 0;
  int added = 0;
  if (!bst_insert_node(&tree->root, key, &added))
    return 0;
  if (added)
    tree->size++;
  return 1;
}

static int contains_node(const Node *node, int key) {
  if (!node)
    return 0;
  if (key < node->key)
    return contains_node(node->left, key);
  if (key > node->key)
    return contains_node(node->right, key);
  return 1; /* igual */
}

int bst_contains(const BST *tree, int key) {
  if (!tree)
    return 0;
  return contains_node(tree->root, key);
}

static int height_node(const Node *node) {
  if (!node)
    return -1; /* árvore vazia = -1; folha = 0 */
  int hl = height_node(node->left);
  int hr = height_node(node->right);
  return (hl > hr ? hl : hr) + 1;
}

int bst_height(const BST *tree) {
  if (!tree)
    return -1;
  return height_node(tree->root);
}

static void inorder_node(const Node *node, void (*visit)(int, void *),
                         void *userdata) {
  if (!node)
    return;
  inorder_node(node->left, visit, userdata);
  visit(node->key, userdata);
  inorder_node(node->right, visit, userdata);
}

void bst_inorder(const BST *tree, void (*visit)(int key, void *userdata),
                 void *userdata) {
  if (!tree || !visit)
    return;
  inorder_node(tree->root, visit, userdata);
}
