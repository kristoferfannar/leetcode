#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int findValueOfPartition(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    int minPartition = INT_MAX, n = (int)nums.size();

    for (int i = 0; i < n - 1; i++)
      minPartition = min(minPartition, nums[i + 1] - nums[i]);

    return minPartition;
  }
};

int main() {
  auto s = Solution();
  vector<int> nums;

  nums = {1, 3, 2, 4};
  assert(s.findValueOfPartition(nums) == 1);
}
