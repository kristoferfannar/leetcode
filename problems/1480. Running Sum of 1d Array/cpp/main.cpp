#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> runningSum(vector<int> &nums) {
    int currSum = 0;

    vector<int> final;

    for (auto i : nums) {
      currSum += i;
      final.push_back(currSum);
    }
    return final;
  }
};

int main() {
  auto s = Solution();

  vector<int> expected = {1, 3, 6};
  vector<int> in = {1, 2, 3};
  vector<int> got = s.runningSum(in);

  for (auto i : expected)
    cout << i << " ";
  cout << endl;

  for (auto i : got)
    cout << i << " ";
  cout << endl;

  assert(got == expected);
}
