#include <iostream>
#include <vector>

std::string evaluate(int a, int b) {
  if (a < b)
    return "a < b";
  else if (a > b)
    return "a > b";

  return "a == b";
}

int main() {
  int n = 2;
  std::vector<int> numbers(n);
  std::string result = "";

  for (int i = 0; i < n; ++i) {
    std::cin >> numbers[i];
  }

  result = evaluate(numbers[0], numbers[1]);

  std::cout << result << std::endl;

  return 0;
}
