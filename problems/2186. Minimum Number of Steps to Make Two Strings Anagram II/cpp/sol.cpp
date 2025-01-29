#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minSteps(string s, string t) {
    vector<int> sChars(26), tChars(26);
    for (auto c : s)
      sChars[c - 'a']++;

    for (auto c : t)
      tChars[c - 'a']++;

    int changes = 0;
    for (int i = 0; i < 26; i++)
      changes += max(tChars[i] - sChars[i], sChars[i] - tChars[i]);

    return changes;
  }
};

int main() {
  auto s = Solution();

  assert(s.minSteps("leetcode", "coats") == 7);
  assert(s.minSteps("night", "thing") == 0);
}
