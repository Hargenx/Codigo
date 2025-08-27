#include <stdio.h>
#include <stdlib.h>

int main() {
    float base, altura, area, perimetro;

    // Entrada de dados
    printf("Por favor, informe a base da sala (em metros): ");
    scanf("%f", &base);

    printf("Por favor, informe a altura da sala (em metros): ");
    scanf("%f", &altura);

    // Cálculos
    area = base * altura;
    perimetro = 2 * (base + altura);

    // Saída formatada
    printf("\nA area da sala eh: %.2f m²", area);
    printf("\nO perimetro da sala eh: %.2f m\n", perimetro);

    return 0;
}
