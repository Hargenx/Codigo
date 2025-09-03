#include <math.h>
#include <stdio.h>


int main(void) {
  int A[6], B[6];

  printf("Digite 6 numeros inteiros:\n");
  for (int i = 0; i < 6; i++) {
    printf("A[%d]: ", i);
    scanf("%d", &A[i]);
    B[i] = (int)pow(A[i], 2); // pow retorna double, convertemos para int
  }

  printf("\nVetor A: ");
  for (int i = 0; i < 6; i++) {
    printf("%d ", A[i]);
  }

  printf("\nVetor B (quadrados): ");
  for (int i = 0; i < 6; i++) {
    printf("%d ", B[i]);
  }
  printf("\n");

  return 0;
}
