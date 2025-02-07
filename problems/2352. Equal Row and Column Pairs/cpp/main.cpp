#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int equalPairs(vector<vector<int>> &grid) {
    int n = (int)grid.size();

    map<vector<int>, int> counter;

    for (int i = 0; i < n; i++)
      counter[grid[i]]++;

    int total = 0;
    for (int c = 0; c < n; c++) {
      vector<int> col(n);
      for (int r = 0; r < n; r++)
        col[r] = grid[r][c];

      total += counter[col];
    }

    return total;
  }
};

int main() {
  auto s = Solution();
  vector<vector<int>> grid;

  grid = {{3, 2, 1}, {1, 7, 6}, {2, 7, 7}};
  assert(s.equalPairs(grid) == 1);

  grid = {{3, 1, 2, 2}, {1, 4, 4, 5}, {2, 4, 2, 2}, {2, 4, 2, 2}};
  assert(s.equalPairs(grid) == 3);

  grid = {{250, 78, 253}, {334, 252, 253}, {250, 253, 253}};
  assert(s.equalPairs(grid) == 0);
}
