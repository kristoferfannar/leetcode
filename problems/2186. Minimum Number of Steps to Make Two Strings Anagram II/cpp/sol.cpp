#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minSteps(string s, string t) {
    map<char, int> sChars, tChars;
    for (auto c : s) {
      if (sChars.find(c) == sChars.end())
        sChars[c] = 0;

      sChars[c]++;
    }

    for (auto c : t) {
      if (tChars.find(c) == tChars.end())
        tChars[c] = 0;

      tChars[c]++;
    }

    int changes = 0;
    for (auto [chr, count] : sChars) {
      if (tChars.find(chr) != tChars.end())
        changes += max(0, count - tChars[chr]);
      else
        changes += count;
    }

    for (auto [chr, count] : tChars) {
      if (sChars.find(chr) != sChars.end())
        changes += max(0, count - sChars[chr]);
      else
        changes += count;
    }

    return changes;
  }
};

int main() {
  auto s = Solution();

  assert(s.minSteps("leetcode", "coats") == 7);
  assert(s.minSteps("night", "thing") == 0);
}
