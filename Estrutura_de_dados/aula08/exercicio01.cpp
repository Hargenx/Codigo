#include <iostream>
#include <limits>
#include <iomanip>

constexpr float PASSO = 6.0f; // média mínima para aprovação

// Função: calcula a nota final conforme as regras
float calcula_nota_final(float sm1, float sm2, float av, float avs) {
  if (avs > av)
    av = avs;
  float bonus = sm1 + sm2;
  float final = av + bonus;
  if (final > 10.0f)
    final = 10.0f;
  return final;
}

// Procedimento: imprime a situação do aluno
void mostra_resultado(float nota_final) {
  std::cout << "\nNota final: " << std::fixed << std::setprecision(2)
            << nota_final << "\n";
  std::cout << "Situacao: " << (nota_final >= PASSO ? "APROVADO" : "REPROVADO")
            << "\n";
}

// Helper para ler número com validação simples
template <typename T> void le_numero(const char *prompt, T &var, T min, T max) {
  for (;;) {
    std::cout << prompt;
    if (std::cin >> var && var >= min && var <= max)
      break;
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Entrada invalida. Tente novamente.\n";
  }
}

int main() {
  float sm1, sm2, av, avs;

  le_numero("SM1 (0 ou 1): ", sm1, 0.0f, 1.0f);
  le_numero("SM2 (0 ou 1): ", sm2, 0.0f, 1.0f);
  le_numero("AV (0..10): ", av, 0.0f, 10.0f);
  le_numero("AVS (0..10): ", avs, 0.0f, 10.0f);

  float nota_final = calcula_nota_final(sm1, sm2, av, avs);
  mostra_resultado(nota_final);
  return 0;
}
