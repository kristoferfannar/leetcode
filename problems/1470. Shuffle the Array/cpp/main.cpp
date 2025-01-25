#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> shuffle(vector<int> &nums, int n) {
    vector<int> shuffled;
    int slot = (int)nums.size() / 2;

    for (int i = 0; i < slot; i++) {
      shuffled.push_back(nums[i]);
      shuffled.push_back(nums[i + n]);
    }
    return shuffled;
  }
};

int main() {
  auto s = Solution();

  vector<int> in = {2, 5, 1, 3, 4, 7};
  vector<int> got = s.shuffle(in, 3);
  vector<int> exp = {2, 3, 5, 4, 1, 7};

  // 2 5 1 3 4 7
  // 2 1 4 5 3 7
  for (auto g : got)
    cout << g << " ";
  cout << endl;

  for (auto e : exp)
    cout << e << " ";
  cout << endl;

  assert(got == exp);
}
