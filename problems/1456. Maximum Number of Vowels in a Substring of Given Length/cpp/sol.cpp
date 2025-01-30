#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int maxVowels(string s, int k) {
    string_view vowels = "aeiou"sv;
    int score = 0, maxScore = 0;

    for (int i = 0; i < (int)s.size(); i++) {

      if (i >= k && vowels.find(s[i - k]) != string_view::npos)
        score--;

      if (vowels.find(s[i]) != string_view::npos)
        score++;

      maxScore = max(score, maxScore);
    }

    return maxScore;
  }
};

int main() {
  auto s = Solution();

  assert(s.maxVowels("abciiidef", 3) == 3);
}
