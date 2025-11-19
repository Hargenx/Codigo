#include "bst.h"
#include "heap_sort.h"
#include "insertion_sort.h"
#include "merge_sort.h"
#include "quick_sort.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


static void copy_arr(int *dst, const int *src, size_t n) {
  for (size_t i = 0; i < n; ++i)
    dst[i] = src[i];
}

/* mede tempo em milissegundos:
   - copia base -> buf
   - chama o sort
   - retorna o tempo gasto */
static double medir_tempo(void (*sort_fn)(int *, size_t), int *buf,
                          const int *base, size_t n) {
  copy_arr(buf, base, n);
  clock_t ini = clock();
  sort_fn(buf, n);
  clock_t fim = clock();
  return 1000.0 * (double)(fim - ini) / CLOCKS_PER_SEC;
}

/* mostra prefixo do vetor */
static void print_prefix(const char *label, const int *v, size_t n) {
  printf("%s", label);
  size_t limite = n < 10 ? n : 10;
  for (size_t i = 0; i < limite; ++i) {
    printf("%s%d", (i ? " " : ""), v[i]);
  }
  if (n > limite)
    printf(" ...");
  puts("");
}

/* callback para coletar resultado do percorrimento em ordem da BST */
typedef struct {
  int *arr;
  size_t idx;
} CollectCtx;

static void collect_visit(int key, void *userdata) {
  CollectCtx *ctx = (CollectCtx *)userdata;
  ctx->arr[ctx->idx++] = key;
}

int main(void) {
  const size_t n = 20000;

  int *base = malloc(n * sizeof *base);
  int *a = malloc(n * sizeof *a);
  int *b = malloc(n * sizeof *b);
  int *c = malloc(n * sizeof *c);
  int *d = malloc(n * sizeof *d);
  int *tree_sorted = malloc(n * sizeof *tree_sorted);

  if (!base || !a || !b || !c || !d || !tree_sorted) {
    fprintf(stderr, "Erro de memoria\n");
    free(base);
    free(a);
    free(b);
    free(c);
    free(d);
    free(tree_sorted);
    return 1;
  }

  /* gera dados aleatórios */
  srand((unsigned)time(NULL));
  for (size_t i = 0; i < n; ++i) {
    base[i] = rand() % 100000;
  }

  printf("n = %zu elementos\n", n);

  double t_ins = medir_tempo(insertion_sort, a, base, n);
  double t_quick = medir_tempo(quick_sort, b, base, n);
  double t_merge = medir_tempo(merge_sort, c, base, n);
  double t_heap = medir_tempo(heap_sort, d, base, n);

  print_prefix("Insertion (prefixo): ", a, n);
  print_prefix("Quick     (prefixo): ", b, n);
  print_prefix("Merge     (prefixo): ", c, n);
  print_prefix("Heap      (prefixo): ", d, n);

  puts("");
  puts("Tempos de ordenacao (ms):");
  printf("Insertion sort : %8.3f  (O(n^2))\n", t_ins);
  printf("Quick sort     : %8.3f  (O(n log n) medio, O(n^2) pior)\n", t_quick);
  printf("Merge sort     : %8.3f  (O(n log n))\n", t_merge);
  printf("Heap sort      : %8.3f  (O(n log n))\n", t_heap);

  /* -------- Agora: Arvore Binaria de Busca (BST) -------- */
  BST *tree = bst_create();
  if (!tree) {
    fprintf(stderr, "Erro ao criar BST\n");
    free(base);
    free(a);
    free(b);
    free(c);
    free(d);
    free(tree_sorted);
    return 1;
  }

  clock_t tb0 = clock();
  for (size_t i = 0; i < n; ++i) {
    if (!bst_insert(tree, base[i])) {
      fprintf(stderr, "Erro ao inserir na BST\n");
      bst_free(tree);
      free(base);
      free(a);
      free(b);
      free(c);
      free(d);
      free(tree_sorted);
      return 1;
    }
  }
  clock_t tb1 = clock();
  double t_bst_build = 1000.0 * (double)(tb1 - tb0) / CLOCKS_PER_SEC;

  CollectCtx ctx = {.arr = tree_sorted, .idx = 0};
  bst_inorder(tree, collect_visit, &ctx);

  print_prefix("BST in-order (prefixo): ", tree_sorted, n);
  printf("\nBST: tamanho = %zu, altura = %d\n", bst_size(tree),
         bst_height(tree));
  printf("Tempo para construir BST: %.3f ms (insercao media O(log n), pior "
         "O(n))\n",
         t_bst_build);

  bst_free(tree);
  free(base);
  free(a);
  free(b);
  free(c);
  free(d);
  free(tree_sorted);
  return 0;
}
