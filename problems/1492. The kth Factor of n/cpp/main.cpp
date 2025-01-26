#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int kthFactor(int n, int k) {
    int curr = 0;
    for (int i = 1; i <= n; i++) {
      if (n % i == 0)
        curr++;

      if (curr == k)
        return i;
    }

    return -1;
  }
};

int main() {
  auto s = Solution();

  assert(s.kthFactor(12, 3) == 3);
  assert(s.kthFactor(7, 2) == 7);
  assert(s.kthFactor(4, 4) == -1);
}
