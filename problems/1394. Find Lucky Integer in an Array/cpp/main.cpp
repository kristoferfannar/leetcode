#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int findLucky(vector<int> &arr) {

    map<int, int> nums;
    int curr = -1;

    for (auto i : arr) {
      if (nums.find(i) == nums.end())
        nums[i] = 1;
      else
        nums[i]++;
    }

    for (auto [num, freq] : nums)
      if (num == freq && num > curr)
        curr = num;

    return curr;
  };
};

int main() {
  auto s = Solution();

  vector<int> in = {2, 2, 3, 4};
  assert(s.findLucky(in) == 2);

  in = {2, 2, 2, 3, 3};
  assert(s.findLucky(in) == -1);
}
