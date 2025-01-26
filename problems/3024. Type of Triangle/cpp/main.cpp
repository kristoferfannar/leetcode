#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string triangleType(vector<int> &nums) {
    sort(nums.begin(), nums.end());

    if (nums[0] == nums[2])
      return "equilateral";

    if (nums[0] + nums[1] <= nums[2])
      return "none";

    if (nums[0] == nums[1] || nums[1] == nums[2])
      return "isosceles";

    return "scalene";
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {3, 3, 3};
  assert(s.triangleType(in) == "equilateral");

  in = {8, 4, 4};
  assert(s.triangleType(in) == "none");
}
