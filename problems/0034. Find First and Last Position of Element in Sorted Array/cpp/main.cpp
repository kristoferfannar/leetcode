#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
  int binLo(vector<int> &nums, int target) {
    int lo = 0, hi = (int)nums.size() - 1, ret = -1;
    while (lo <= hi) {
      int mid = (lo + hi) / 2;
      if (nums[mid] == target) {
        ret = mid, hi = mid - 1;
      } else if (nums[mid] > target) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return ret;
  }

  int binHi(vector<int> &nums, int target) {
    int lo = 0, hi = (int)nums.size() - 1, ret = -1;
    while (lo <= hi) {
      int mid = (lo + hi + 1) / 2; // use ceiling division
      if (nums[mid] == target) {
        ret = mid, lo = mid + 1;
      } else if (nums[mid] > target) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return ret;
  }

public:
  vector<int> searchRange(vector<int> &nums, int target) {

    auto lo = binLo(nums, target), hi = binHi(nums, target);
    return {lo, hi};
  }
};

int main() {
  auto s = Solution();
  vector<int> nums, exp;

  nums = {5, 7, 7, 8, 8, 10};
  exp = {3, 4};
  assert(s.searchRange(nums, 8) == exp);

  nums = {5, 7, 7, 8, 8, 10};
  exp = {-1, -1};
  assert(s.searchRange(nums, 6) == exp);
}
