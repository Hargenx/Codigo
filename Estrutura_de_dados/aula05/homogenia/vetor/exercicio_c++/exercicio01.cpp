#include <array>
#include <iostream>


int main() {
  std::array<int, 5> numeros;
  int contador = 0;

  std::cout << "Digite 5 numeros inteiros:\n";
  for (std::size_t i = 0; i < numeros.size(); i++) {
    std::cout << "Numero " << i + 1 << ": ";
    std::cin >> numeros[i];
    if (numeros[i] > 100) {
      contador++;
    }
  }

  std::cout << "\nQuantidade de numeros maiores que 100: " << contador << '\n';
  return 0;
}
