#include "quick_sort.h"

static inline void swap(int *x, int *y) {
  int t = *x;
  *x = *y;
  *y = t;
}

static size_t partition(int *a, size_t l, size_t r) {
  int p = a[r]; // pivô = último
  size_t i = l; // menor região
  for (size_t j = l; j < r; ++j) {
    if (a[j] <= p) {
      swap(&a[i], &a[j]);
      ++i;
    }
  }
  swap(&a[i], &a[r]);
  return i;
}

static void qrec(int *a, size_t l, size_t r) {
  if (l >= r)
    return;
  size_t m = partition(a, l, r);
  if (m > 0)
    qrec(a, l, m - 1);
  qrec(a, m + 1, r);
}

void quick_sort(int *a, size_t n) {
  if (n > 1)
    qrec(a, 0, n - 1);
}
