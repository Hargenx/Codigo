#include <iostream>
#include <new> // std::nothrow

int main() {
  // Aloca 1 int; use nothrow para não lançar exceção em falta de memória
  int *ptr_a = new (std::nothrow) int;

  if (ptr_a == nullptr) {
    std::cerr << "Memoria insuficiente!\n";
    return 1;
  }

  // Mostra o endereço do bloco alocado
  std::cout << "Endereco de ptr_a: " << static_cast<const void *>(ptr_a)
            << '\n';

  *ptr_a = 90;
  std::cout << "Conteudo apontado por ptr_a: " << *ptr_a << '\n';

  delete ptr_a;    // libera
  ptr_a = nullptr; // evita dangling pointer
  return 0;
}
