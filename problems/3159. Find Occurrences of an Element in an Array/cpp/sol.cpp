#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> occurrencesOfElement(vector<int> &nums, vector<int> &queries,
                                   int x) {
    vector<int> occs, ret;

    for (int i = 0; i < (int)nums.size(); i++)
      if (nums[i] == x)
        occs.push_back(i);

    for (auto q : queries) {
      if (q > (int)occs.size())
        ret.push_back(-1);
      else
        ret.push_back(occs[q - 1]);
    }

    return ret;
  }
};

int main() {
  auto s = Solution();
  vector<int> nums, queries, exp;

  nums = {1, 3, 1, 7}, queries = {1, 3, 2, 4};
  exp = {0, -1, 2, -1};
  assert(s.occurrencesOfElement(nums, queries, 1) == exp);

  nums = {1, 2, 3}, queries = {10}, exp = {-1};
  assert(s.occurrencesOfElement(nums, queries, 10) == exp);
}
