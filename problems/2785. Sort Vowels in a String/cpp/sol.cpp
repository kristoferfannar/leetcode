#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string sortVowels(string s) {
    auto vowels = "aeiouAEIOU"sv;

    vector<int> pos;
    vector<int> found(128);

    for (int i = 0; i < (int)s.size(); i++) {
      if (vowels.find(s[i]) != string::npos) {
        pos.push_back(i);
        found[s[i]]++;
      }
    }

    int currPos = 0;

    for (int i = 0; i < (int)found.size(); i++) {
      while (found[i] > 0) {
        s[pos[currPos++]] = char(i);
        found[i]--;
      }
    }

    return s;
  }
};

int main() {
  auto s = Solution();

  assert(s.sortVowels("lEetcOde") == "lEOtcede");
}
