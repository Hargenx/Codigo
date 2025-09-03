#include <array>
#include <iostream>


int main() {
  std::array<std::array<int, 3>, 3> A = {
      {{10, 30, 50}, {5, 15, 25}, {2, 5, 9}}};
  std::array<std::array<int, 3>, 3> B = {{{5, 35, 70}, {1, 25, 30}, {1, 4, 7}}};
  std::array<std::array<int, 3>, 3> C;

  // Calcula os maiores valores
  for (std::size_t i = 0; i < A.size(); i++) {
    for (std::size_t j = 0; j < A[i].size(); j++) {
      C[i][j] = std::max(A[i][j], B[i][j]);
    }
  }

  // Imprime matriz C
  std::cout << "Matriz C (maiores valores):\n";
  for (const auto &linha : C) {
    for (int valor : linha) {
      std::cout << valor << "\t";
    }
    std::cout << "\n";
  }

  return 0;
}
