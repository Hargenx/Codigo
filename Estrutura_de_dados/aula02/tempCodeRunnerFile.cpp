#include <iomanip>
#include <iostream>

int main() {
  double val_dolar{}, cotacao{};

  std::cout << "Informe a quantidade de dolares no cofre: ";
  if (!(std::cin >> val_dolar) || val_dolar < 0) {
    std::cerr << "Valor de dolares invalido.\n";
    return 1;
  }

  std::cout << "Informe a cotacao do dolar (em R$): ";
  if (!(std::cin >> cotacao) || cotacao < 0) {
    std::cerr << "Valor de cotacao invalido.\n";
    return 1;
  }

  double val_real = val_dolar * cotacao;
  std::cout << std::fixed << std::setprecision(2) << "\nValor em reais: R$ "
            << val_real << "\n";
}
