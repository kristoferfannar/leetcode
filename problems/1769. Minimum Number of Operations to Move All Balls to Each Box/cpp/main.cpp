#include <bits/stdc++.h>
using namespace std;

// Prefix Suffix array hint from
// (only read solution title before coding this bad boy up)
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/solutions/6236487/beats-100-prefix-suffix-array-detailed-explanation
class Solution {
public:
  vector<int> minOperations(string boxes) {
    if (boxes.size() == 1)
      return {0};

    vector<int> out(boxes.size());
    vector<pair<int, int>> pre(boxes.size()), suf(boxes.size());

    // initialize prefix array
    pre[0] = pair(0, boxes[0] - '0');
    for (int i = 1; i < (int)boxes.size(); i++) {
      auto [a, b] = pre[i - 1];
      int isBox = boxes[i] - '0';
      pre[i] = pair(a + b, b + isBox);
    }

    suf[(int)boxes.size() - 1] = pair(0, boxes[(int)boxes.size() - 1] - '0');

    for (int i = (int)boxes.size() - 2; i >= 0; i--) {
      auto [a, b] = suf[i + 1];
      int isBox = boxes[i] - '0';
      suf[i] = pair(a + b, b + isBox);
    }

    out[0] = suf[1].first + suf[1].second;
    for (int i = 1; i < (int)boxes.size() - 1; i++) {
      out[i] = pre[i - 1].first + pre[i - 1].second + suf[i + 1].first +
               suf[i + 1].second;
    }
    out[boxes.size() - 1] =
        pre[(int)boxes.size() - 2].first + pre[(int)boxes.size() - 2].second;

    return out;
  }
};

int main() {
  auto s = Solution();
  vector<int> exp;

  exp = {1, 1, 3};
  assert(s.minOperations("110") == exp);

  exp = {11, 8, 5, 4, 3, 4};
  assert(s.minOperations("001011") == exp);

  exp = {0};
  assert(s.minOperations("0") == exp);
}
