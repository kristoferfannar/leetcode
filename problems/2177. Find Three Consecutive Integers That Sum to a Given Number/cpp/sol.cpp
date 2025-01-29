#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<long long> sumOfThree(long long num) {
    if (num % 3 == 0)
      return {num / 3 - 1, num / 3, num / 3 + 1};
    return {};
  }
};

int main() {
  auto s = Solution();
  vector<long long> exp = {10, 11, 12};

  assert(s.sumOfThree(33) == exp);
  assert(s.sumOfThree(4).size() == 0);
}
