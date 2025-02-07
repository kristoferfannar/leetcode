#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string longestPalindrome(string s) {

    // odd sizes
    int size;
    int largest = 0, largestIdx = 0;

    for (int i = 0; i < (int)s.size(); i++) {
      size = 0;
      while (i + size < (int)s.size() && i - size >= 0 &&
             s[i + size] == s[i - size]) {
        size++;
      }
      size--;

      if (1 + 2 * size >= largest) {
        largest = 1 + 2 * size;
        largestIdx = i - size;
      }
    }

    // even sizes
    for (int i = 0; i < (int)s.size() - 1; i++) {
      size = 0;
      if (s[i] != s[i + 1])
        continue;

      while (i + 1 + size < (int)s.size() && i - size >= 0 &&
             s[i + 1 + size] == s[i - size]) {
        size++;
      }
      size--;

      if (2 + 2 * size >= largest) {
        largest = 2 + 2 * size;
        largestIdx = i - size;
      }
    }

    return s.substr(largestIdx, largest);
  }
};

int main() {
  auto s = Solution();

  assert(s.longestPalindrome("babad").length() == 3);
  assert(s.longestPalindrome("babbad").length() == 4);
}
