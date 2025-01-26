#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  bool kLengthApart(vector<int> &nums, int k) {
    int last = -k - 1;

    for (int i = 0; i < (int)nums.size(); i++)
      if (nums[i] == 1) {
        if (i - last < k + 1)
          return false;

        last = i;
      }

    return true;
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {1, 0, 0, 0, 1, 0, 0, 1};
  assert(s.kLengthApart(in, 2) == true);

  in = {1, 0, 0, 1, 0, 1};
  assert(s.kLengthApart(in, 2) == false);
}
