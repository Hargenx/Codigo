#include <iostream>

// Função: verifica se n é primo
bool eh_primo(int n) {
  if (n < 2)
    return false;
  for (int i = 2; i * i <= n; i++) {
    if (n % i == 0)
      return false;
  }
  return true;
}

// Procedimento: imprime o resultado
void mostra_resultado(int n) {
  if (eh_primo(n))
    std::cout << n << " é primo.\n";
  else
    std::cout << n << " não é primo.\n";
}

int main() {
  int numero;
  std::cout << "Digite um numero: ";
  std::cin >> numero;
  mostra_resultado(numero);
  return 0;
}
