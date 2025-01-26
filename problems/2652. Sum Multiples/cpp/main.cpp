#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int sumOfMultiples(int n) {
    int summed = 0;
    for (int i = 1; i <= n; i++) {
      if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0)
        summed += i;
    }
    return summed;
  }
};

int main() {
  auto s = Solution();

  assert(s.sumOfMultiples(7) == 21);
}
