#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
  bool isValidBoard(int *board, int n) {
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if ((board[i] - i) == (board[j] - j))
          return false;
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if ((board[i] + i) == (board[j] + j))
          return false;
      }
    }

    return true;
  }

  vector<string> toBoard(int *board, int n) {
    vector<string> strs;

    for (int i = 0; i < n; i++) {
      auto nw = string(n, '.');
      nw[board[i]] = 'Q';
      strs.push_back(nw);
    }

    return strs;
  }

public:
  vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> out;

    /* use c-style int vector as it allows
     * me to use next_permutation() */
    int *board = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
      board[i] = i;

    do {
      if (isValidBoard(board, n))
        out.push_back(toBoard(board, n));

    } while (next_permutation(board, board + n));

    free(board);
    return out;
  }
};

int main() {
  auto s = Solution();
  vector<vector<string>> exp;

  exp = {{".Q..", "...Q", "Q...", "..Q."}, {"..Q.", "Q...", "...Q", ".Q.."}};
  assert(s.solveNQueens(4) == exp);

  exp = {{"Q"}};
  assert(s.solveNQueens(1) == exp);

  exp = {};
  assert(s.solveNQueens(2) == exp);
  assert(s.solveNQueens(3) == exp);
}
