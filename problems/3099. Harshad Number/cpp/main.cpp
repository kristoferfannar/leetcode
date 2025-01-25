#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int sumOfTheDigitsOfHarshadNumber(int x) {
    int harshad = 0, curr = x;

    while (curr) {
      harshad += curr % 10;
      curr /= 10;
    }

    return x % harshad == 0 ? harshad : -1;
  }
};

int main() {
  auto s = Solution();
  assert(s.sumOfTheDigitsOfHarshadNumber(18) == 9);
  assert(s.sumOfTheDigitsOfHarshadNumber(14) == -1);
}
