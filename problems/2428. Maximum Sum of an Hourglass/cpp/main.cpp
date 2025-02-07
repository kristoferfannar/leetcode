#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
  int calculateGrid(vector<vector<int>> &grid, int r, int c) {
    return grid[r][c] + grid[r][c + 1] + grid[r][c + 2] + grid[r + 1][c + 1] +
           grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2];
  }

public:
  int maxSum(vector<vector<int>> &grid) {
    int R = (int)grid.size() - 2;
    int C = (int)grid[0].size() - 2;
    int maxGrid = INT_MIN;

    for (int r = 0; r < R; r++)
      for (int c = 0; c < C; c++)
        maxGrid = max(maxGrid, calculateGrid(grid, r, c));

    return maxGrid;
  }
};

int main() {
  auto s = Solution();

  vector<vector<int>> grid;

  grid = {{6, 2, 1, 3}, {4, 2, 1, 5}, {9, 2, 8, 7}, {4, 1, 2, 9}};
  assert(s.maxSum(grid) == 30);

  grid = {{520626, 685427, 788912, 800638, 717251, 683428},
          {23602, 608915, 697585, 957500, 154778, 209236},
          {287585, 588801, 818234, 73530, 939116, 252369}};
  assert(s.maxSum(grid) == 5095181);
}
