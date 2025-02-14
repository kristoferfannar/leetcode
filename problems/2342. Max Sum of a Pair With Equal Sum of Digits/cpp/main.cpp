#include <bits/stdc++.h>
using namespace std;

int digitSum(int num) {
  int out = 0;
  while (num) {
    out += num % 10;
    num /= 10;
  }
  return out;
}
class Solution {
public:
  int maximumSum(vector<int> &nums) {
    map<int, int> counter;
    int highest = INT_MIN;

    for (int i = 0; i < (int)nums.size(); i++) {
      int dSum = digitSum(nums[i]);
      if (counter.find(dSum) == counter.end()) {
        counter[dSum] = nums[i];
      } else {
        highest = max(highest, counter[dSum] + nums[i]);
        counter[dSum] = max(counter[dSum], nums[i]);
      }
    }

    if (highest == INT_MIN)
      highest = -1;

    return highest;
  }
};

int main() {
  auto s = Solution();
  vector<int> nums;

  nums = {18, 43, 36, 13, 7};
  assert(s.maximumSum(nums) == 54);

  nums = {10, 12, 19, 14};
  assert(s.maximumSum(nums) == -1);
}
