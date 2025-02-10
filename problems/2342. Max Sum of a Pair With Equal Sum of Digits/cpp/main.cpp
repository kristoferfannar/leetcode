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
    map<int, vector<int>> counter;

    for (int i = 0; i < (int)nums.size(); i++) {
      int dSum = digitSum(nums[i]);
      if (counter.find(dSum) == counter.end()) {
        counter[dSum] = {};
      }
      counter[dSum].push_back(nums[i]);
    }
    int highest = INT_MIN;
    for (auto [dSum, vals] : counter) {
      int first = INT_MIN, second = INT_MIN;

      if (vals.size() <= 1)
        continue;

      for (auto val : vals) {
        if (val > first) {
          second = first;
          first = val;
        } else if (val > second) {
          second = val;
        }
      }

      highest = max(highest, first + second);
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
