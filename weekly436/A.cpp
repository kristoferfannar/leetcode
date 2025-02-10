#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  vector<vector<int>> sortMatrix(vector<vector<int>> &grid) {
    int n = (int)grid.size();

    bool isNonIncreasing = false;
    for (int shift = -n; shift < n; shift++) {
      // cout << "shift: " << shift << endl;
      if (shift == 0)
        isNonIncreasing = true;
      for (int x = 0; x < n; x++) {
        int y = x + shift;
        if (y < 0)
          continue;
        else if (y >= n)
          break;

        int currX = x - 1, currY = y - 1;
        while (currX >= 0 && currY >= 0) {
          if (!isNonIncreasing) {
            if (grid[currY][currX] <= grid[currY + 1][currX + 1])
              break;
            auto tmp = grid[currY][currX];
            grid[currY][currX] = grid[currY + 1][currX + 1];
            grid[currY + 1][currX + 1] = tmp;
            currX--;
            currY--;
          } else {
            if (grid[currY][currX] >= grid[currY + 1][currX + 1])
              break;
            auto tmp = grid[currY][currX];
            grid[currY][currX] = grid[currY + 1][currX + 1];
            grid[currY + 1][currX + 1] = tmp;
            currX--;
            currY--;
          }
        }
      }
    }

    // for (auto row : grid) {
    //   // cout << "row" << endl;
    //   for (auto i : row)
    //     cout << i << " ";
    //   cout << endl;
    // }
    return grid;
  }
};

int main() {
  auto s = Solution();
  vector<vector<int>> in, exp;

  in = {{1, 7, 3}, {9, 8, 2}, {4, 5, 6}};
  exp = {{8, 2, 3}, {9, 6, 7}, {4, 5, 1}};
  assert(s.sortMatrix(in) == exp);

  in = {{0, 1}, {1, 2}};
  exp = {{2, 1}, {1, 0}};
  assert(s.sortMatrix(in) == exp);

  in = {{1}};
  exp = {{1}};
  assert(s.sortMatrix(in) == exp);
}
