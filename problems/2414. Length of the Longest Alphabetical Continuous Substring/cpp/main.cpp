#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int longestContinuousSubstring(string s) {
    int longest = 0, curr = 0, last = -1;

    for (int i = 0; i < (int)s.length(); i++) {
      curr++;
      if (s[i] != last + 1) {
        longest = max(longest, curr);
        curr = 0;
      }
      last = s[i];
    }

    curr++;

    return max(longest, curr);
  };
};

int main() {
  auto s = Solution();

  assert(s.longestContinuousSubstring("abacaba") == 2);
  assert(s.longestContinuousSubstring("abcde") == 5);
  assert(s.longestContinuousSubstring("babcde") == 5);
  assert(s.longestContinuousSubstring("z") == 1);
  assert(s.longestContinuousSubstring("ayz") == 2);
  assert(s.longestContinuousSubstring("yrpjofyzubfsiypfre") == 2);
}
