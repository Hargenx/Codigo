#include <array>
#include <iostream>


int main() {
  std::array<std::array<float, 4>, 4> matriz{};
  float somaImpares = 0.0f, somaPares = 0.0f;
  int countPares = 0;

  std::cout << "Digite os elementos da matriz 4x4:\n";
  for (std::size_t i = 0; i < 4; i++) {
    for (std::size_t j = 0; j < 4; j++) {
      std::cout << "Elemento [" << i << "][" << j << "]: ";
      std::cin >> matriz[i][j];

      if (j % 2 == 0) { // colunas ímpares (índice 0,2)
        somaImpares += matriz[i][j];
      } else { // colunas pares (índice 1,3)
        somaPares += matriz[i][j];
        countPares++;
      }
    }
  }

  std::cout << "\nSoma dos elementos das colunas impares: " << somaImpares
            << '\n';
  if (countPares > 0) {
    std::cout << "Media aritmetica dos elementos das colunas pares: "
              << (somaPares / countPares) << '\n';
  }

  return 0;
}
