#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<vector<int>> sortTheStudents(vector<vector<int>> &score, int k) {

    sort(score.begin(), score.end(),
         [&k](vector<int> &a, vector<int> &b) { return a[k] > b[k]; });

    return score;
  }
};

int main() {
  auto s = Solution();

  vector<vector<int>> score, exp;

  score = {{10, 6, 9, 1}, {7, 5, 11, 2}, {4, 8, 3, 15}};
  exp = {{7, 5, 11, 2}, {10, 6, 9, 1}, {4, 8, 3, 15}};
  assert(s.sortTheStudents(score, 2) == exp);
}
