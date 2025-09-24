#include <iostream>

// Passagem por valor
void por_valor(int x) { x = x + 10; }

// Passagem por referência (referência C++)
void por_referencia(int &x) { x = x + 10; }

int main() {
  int a = 5, b = 5;

  por_valor(a);
  por_referencia(b);

  std::cout << "a (por valor) = " << a << "\n";      // continua 5
  std::cout << "b (por referencia) = " << b << "\n"; // vira 15
}
