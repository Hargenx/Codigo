#include <iostream>

// Função que soma dois inteiros usando referências
void somaPorReferencia(const int &a, const int &b, int &resultado) {
  resultado = a + b;
}

int main() {
  int primeiroNumero, segundoNumero, resultado;

  std::cout
      << "Ponteiro: Adicionar dois numeros usando chamada por referencia:\n";
  std::cout << "-------------------------------------------------------\n";

  std::cout << "Digite o primeiro numero: ";
  std::cin >> primeiroNumero;

  std::cout << "Digite o segundo numero: ";
  std::cin >> segundoNumero;

  somaPorReferencia(primeiroNumero, segundoNumero, resultado);

  std::cout << "A soma de " << primeiroNumero << " e " << segundoNumero << " e "
            << resultado << std::endl;

  return 0;
}
