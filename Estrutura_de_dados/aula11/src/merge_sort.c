#include "merge_sort.h"
#include <stdlib.h>


static void merge(int *a, int *aux, size_t l, size_t m, size_t r) {
  size_t i = l, j = m + 1, k = l;
  while (i <= m && j <= r) {
    if (a[i] <= a[j])
      aux[k++] = a[i++];
    else
      aux[k++] = a[j++];
  }
  while (i <= m)
    aux[k++] = a[i++];
  while (j <= r)
    aux[k++] = a[j++];
  for (size_t t = l; t <= r; ++t)
    a[t] = aux[t];
}

static void mrec(int *a, int *aux, size_t l, size_t r) {
  if (l >= r)
    return;
  size_t m = l + (r - l) / 2;
  mrec(a, aux, l, m);
  mrec(a, aux, m + 1, r);
  merge(a, aux, l, m, r);
}

void merge_sort(int *a, size_t n) {
  if (n < 2)
    return;
  int *aux = (int *)malloc(n * sizeof *aux);
  if (!aux)
    return; // sem memória: apenas desiste silenciosamente
  mrec(a, aux, 0, n - 1);
  free(aux);
}
