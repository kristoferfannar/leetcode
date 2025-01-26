#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> getConcatenation(vector<int> &nums) {
    vector<int> doubled;
    doubled.resize(nums.size() * 2);

    for (int i = 0; i < (int)nums.size(); i++) {
      doubled[i] = nums[i];
      doubled[i + nums.size()] = nums[i];
    }

    return doubled;
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {1, 2, 3};
  vector<int> got = s.getConcatenation(in);
  vector<int> exp = {1, 2, 3, 1, 2, 3};
  assert(got == exp);
};
