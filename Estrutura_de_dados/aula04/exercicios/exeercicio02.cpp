#include <iostream>

int main() {
  int primeiroNumero, segundoNumero, *ponteiroValor1, *ponteiroValor2, soma;

  std::cout << "\n\nUsando ponteiros: Somando dois numeros:\n";
  std::cout << "----------------------------------------\n";

  std::cout << "Digite o primeiro numero: ";
  std::cin >> primeiroNumero;

  std::cout << "Digite o segundo numero: ";
  std::cin >> segundoNumero;

  // Ponteiros recebem os enderecos
  ponteiroValor1 = &primeiroNumero;
  ponteiroValor2 = &segundoNumero;

  // Soma os valores apontados
  soma = *ponteiroValor1 + *ponteiroValor2;

  std::cout << "A soma dos valores digitados e: " << soma << "\n\n";

  return 0;
}
