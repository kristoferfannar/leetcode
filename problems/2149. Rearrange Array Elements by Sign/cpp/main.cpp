#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> rearrangeArray(vector<int> &nums) {
    int pos = 0, neg = 0;
    vector<int> arr;
    arr.resize(nums.size());

    for (int i = 0; i < (int)nums.size(); i++) {
      if (nums[i] > 0) {
        arr[pos * 2] = nums[i];
        pos++;
      } else {
        arr[1 + neg * 2] = nums[i];
        neg++;
      }
    }

    return arr;
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {3, 1, -2, -5, 2, -4};
  vector<int> exp = {3, -2, 1, -5, 2, -4};
  vector<int> got = s.rearrangeArray(in);
  assert(got == exp);
}
