#include <iostream>
#include <cstddef>
using namespace std;

int main() {
    // Ponteiro para inteiro
    int *p;

    // Ponteiro para um array de 5 inteiros
    int (*ptr)[5];

    // Um array de 5 inteiros
    int arr[5] = {10, 20, 30, 40, 50};

    // p aponta para o elemento 0 do array
    p = arr;

    // ptr aponta para o array inteiro
    ptr = &arr;

    cout << "p = " << p << ", ptr = " << ptr << endl;

    // Avançando os ponteiros
    p++;   // avança 1 inteiro (4 bytes normalmente)
    ptr++; // avança 1 bloco de 5 inteiros (20 bytes normalmente)

    cout << "p = " << p << ", ptr = " << ptr << endl;

    return 0;
}
