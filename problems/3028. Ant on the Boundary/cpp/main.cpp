#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int returnToBoundaryCount(vector<int> &nums) {
    int curr = 0;
    int found = 0;
    for (auto i : nums) {
      curr += i;

      if (!curr)
        found++;
    }

    return found;
  };
};

int main() {
  auto s = Solution();

  vector<int> in = {2, 3, -5};
  assert(s.returnToBoundaryCount(in) == 1);
}
