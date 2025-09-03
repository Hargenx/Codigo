#include <array>
#include <cmath>
#include <iostream>


int main() {
  std::array<int, 6> A;
  std::array<int, 6> B;

  std::cout << "Digite 6 numeros inteiros:\n";
  for (std::size_t i = 0; i < A.size(); i++) {
    std::cout << "A[" << i << "]: ";
    std::cin >> A[i];
    B[i] = static_cast<int>(std::pow(A[i], 2));
  }

  std::cout << "\nVetor A: ";
  for (int valor : A) {
    std::cout << valor << " ";
  }

  std::cout << "\nVetor B (quadrados): ";
  for (int valor : B) {
    std::cout << valor << " ";
  }
  std::cout << "\n";

  return 0;
}
