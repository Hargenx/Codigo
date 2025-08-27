#include <iostream>
#include <memory>

int main() {
  auto ptr_a = std::make_unique<int>(); // aloca e inicializa
  *ptr_a = 90;

  std::cout << "Endereco: " << static_cast<const void *>(ptr_a.get()) << '\n';
  std::cout << "Conteudo: " << *ptr_a << '\n';

  // nada de delete: liberação automática ao sair do escopo
}
