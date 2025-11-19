#include "heap_sort.h"

static inline void swap(int *x, int *y) {
  int t = *x;
  *x = *y;
  *y = t;
}

static void sift_down(int *a, size_t n, size_t i) {
  while (1) {
    size_t l = 2 * i + 1, r = 2 * i + 2, mx = i;
    if (l < n && a[l] > a[mx])
      mx = l;
    if (r < n && a[r] > a[mx])
      mx = r;
    if (mx == i)
      break;
    swap(&a[i], &a[mx]);
    i = mx;
  }
}

void heap_sort(int *a, size_t n) {
  if (n < 2)
    return;
  for (size_t i = (n / 2); i-- > 0;)
    sift_down(a, n, i); // build-heap
  for (size_t end = n; end-- > 1;) {
    swap(&a[0], &a[end]);
    sift_down(a, end, 0);
  }
}
