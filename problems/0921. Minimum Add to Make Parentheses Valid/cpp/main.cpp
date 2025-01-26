#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minAddToMakeValid(string s) {
    int clsNeeded = 0, opNeeded = 0;

    for (auto ch : s) {
      if (ch == '(') {
        clsNeeded++;
      }

      if (ch == ')') {
        if (clsNeeded > 0) {
          clsNeeded--;
        } else {
          opNeeded++;
        }
      }
    }

    return clsNeeded + opNeeded;
  }
};

int main() {
  auto s = Solution();

  assert(s.minAddToMakeValid("())") == 1);
  assert(s.minAddToMakeValid("(((") == 3);
  assert(s.minAddToMakeValid("()))((") == 4);
}
