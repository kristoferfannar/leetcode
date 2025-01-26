#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int countNegatives(vector<vector<int>> &grid) {
    int negative = 0;
    for (auto y : grid)
      for (auto x : y)
        if (x < 0)
          negative++;

    return negative;
  }
};

int main() {
  auto s = Solution();

  vector<vector<int>> in = {{-1, 2, 3}, {1, 2, 3}};
  assert(s.countNegatives(in) == 1);
}
