#include <iostream>

// Função que lê números e conta pares e ímpares
void contarParesImpares(int quantidade, int &pares, int &impares) {
  int num;
  pares = 0;
  impares = 0;

  for (int i = 1; i <= quantidade; i++) {
    std::cout << "Informe o numero " << i << ": ";
    std::cin >> num;

    if (num % 2 == 0) {
      pares++;
    } else {
      impares++;
    }
  }
}

int main() {
  int pares, impares;

  contarParesImpares(10, pares, impares);

  std::cout << "Quantidade de numeros pares: " << pares << "\n";
  std::cout << "Quantidade de numeros impares: " << impares << "\n";

  return 0;
}
