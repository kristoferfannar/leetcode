#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> findLonely(vector<int> &nums) {
    map<int, int> counter;

    for (auto i : nums) {
      if (counter.find(i) == counter.end())
        counter[i] = 0;
      counter[i]++;
    }

    vector<int> out;

    for (auto [num, count] : counter) {
      if (count == 1 && counter.find(num - 1) == counter.end() &&
          counter.find(num + 1) == counter.end())
        out.push_back(num);
    }

    return out;
  }
};

int main() {
  auto s = Solution();
  vector<int> in, exp, got;

  in = {10, 6, 5, 8};
  exp = {10, 8};
  got = s.findLonely(in);
  sort(got.begin(), got.end());
  sort(exp.begin(), exp.end());
  assert(got == exp);
}
