#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<string> simplifiedFractions(int n) {
    vector<string> ret;
    char str[20];

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j < i; j++) {

        // I should probably create a vector<set<int>> of the factors of each
        // number. Instead, I'm repeating this work for every iteration
        // still, a pass is a pass
        bool uniq = i % j != 0 || j == 1;
        for (int x = 2; x <= n; x++) {
          if (!uniq)
            break;

          if (j % x == 0 && i % x == 0)
            uniq = false;
        }

        if (uniq) {
          sprintf(str, "%d/%d", j, i);
          ret.push_back(string(str));
        }
      }
    }

    return ret;
  }
};

int main() {
  auto s = Solution();
  vector<string> exp;

  exp = {"1/2", "1/3", "1/4", "2/3", "3/4"};
  auto got = s.simplifiedFractions(4);
  sort(exp.begin(), exp.end());
  sort(got.begin(), got.end());
  assert(got == exp);

  exp = {"1/2", "1/3", "1/4", "1/5", "1/6", "2/3",
         "2/5", "3/4", "3/5", "4/5", "5/6"};
  got = s.simplifiedFractions(6);
  sort(exp.begin(), exp.end());
  sort(got.begin(), got.end());
  assert(got == exp);
}
