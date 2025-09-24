#include <iostream>

void boas_vindas(const std::string &nome) {
  std::cout << "Bem-vindo(a), " << nome << "!\n";
}

int main() {
  boas_vindas("Raphael");
  return 0;
}
