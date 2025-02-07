#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minOperations(int n) {
    int ops = 0;

    for (int i = 0; i < n / 2; i++)
      ops += n - (i * 2 + 1);

    return ops;
  }
};

int main() {
  auto s = Solution();

  assert(s.minOperations(3) == 2);
  assert(s.minOperations(4) == 4);
  assert(s.minOperations(6) == 9);
}
