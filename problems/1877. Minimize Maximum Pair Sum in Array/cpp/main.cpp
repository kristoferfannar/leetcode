#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minPairSum(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    int minSum = INT_MIN, n = (int)nums.size();

    for (int i = 0; i < n / 2; i++)
      minSum = max(nums[n - 1 - i] + nums[i], minSum);

    return minSum;
  }
};

int main() {
  auto s = Solution();
  vector<int> nums;

  nums = {3, 5, 2, 3};
  assert(s.minPairSum(nums) == 7);

  nums = {3, 5, 4, 2, 4, 6};
  assert(s.minPairSum(nums) == 8);
}
