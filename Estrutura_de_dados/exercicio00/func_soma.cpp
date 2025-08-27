#include <iostream>
using namespace std;

int soma(int a, int b) { return a + b; }

int main() {
  int x, y;
  cout << "Digite dois números: ";
  cin >> x >> y;

  cout << "Soma = " << soma(x, y) << endl;
  return 0;
}
