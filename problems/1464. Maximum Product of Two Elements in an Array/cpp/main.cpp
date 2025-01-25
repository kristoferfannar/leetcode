#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int maxProduct(vector<int> &nums) {
    int fst, scd;

    fst = max(nums[0], nums[1]);
    scd = min(nums[0], nums[1]);

    for (int i = 2; i < (int)nums.size(); i++) {
      if (nums[i] >= fst) {
        scd = fst;
        fst = nums[i];
      } else if (nums[i] > scd) {
        scd = nums[i];
      }
    }

    return (fst - 1) * (scd - 1);
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {3, 4, 5, 2};
  assert(s.maxProduct(in) == 12);

  in = {1, 5, 4, 5};
  assert(s.maxProduct(in) == 16);
}
