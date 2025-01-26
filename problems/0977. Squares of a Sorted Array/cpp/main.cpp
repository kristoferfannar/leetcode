#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> sortedSquares(vector<int> &nums) {
    vector<int> squared;

    for (auto num : nums)
      squared.push_back(num * num);

    sort(squared.begin(), squared.end());
    return squared;
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {-4, -1, 0, 3, 10};
  vector<int> got = s.sortedSquares(in);
  vector<int> exp = {0, 1, 9, 16, 100};
  assert(got == exp);

  in = {-7, -3, 2, 3, 11};
  got = s.sortedSquares(in);
  exp = {4, 9, 9, 49, 121};
  assert(got == exp);
}
