#include "insertion_sort.h"

void insertion_sort(int *a, size_t n) {
  for (size_t i = 1; i < n; ++i) {
    int x = a[i];
    size_t j = i;
    while (j > 0 && a[j - 1] > x) {
      a[j] = a[j - 1];
      --j;
    }
    a[j] = x;
  }
}
