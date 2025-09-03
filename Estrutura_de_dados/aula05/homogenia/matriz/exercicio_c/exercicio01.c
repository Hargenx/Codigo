#include <stdio.h>

int main(void) {
  int A[3][3] = {{10, 30, 50}, {5, 15, 25}, {2, 5, 9}};
  int B[3][3] = {{5, 35, 70}, {1, 25, 30}, {1, 4, 7}};
  int C[3][3];

  // Calcula os maiores valores
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      C[i][j] = (A[i][j] > B[i][j]) ? A[i][j] : B[i][j];
    }
  }

  // Imprime matriz C
  printf("Matriz C (maiores valores):\n");
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      printf("%4d ", C[i][j]);
    }
    printf("\n");
  }

  return 0;
}
