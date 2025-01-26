#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int countDistinctIntegers(vector<int> &nums) {
    set<int> dist;

    for (auto i : nums) {
      dist.insert(i);
      int rev = 0;

      while (i) {
        rev *= 10;
        rev += i % 10;
        i /= 10;
      }

      dist.insert(rev);
    }

    return (int)dist.size();
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {1, 13, 10, 12, 31};
  assert(s.countDistinctIntegers(in) == 6);
}
