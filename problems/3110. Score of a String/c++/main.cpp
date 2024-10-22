#include <cmath>
#include <iostream>
#include <string>

using namespace std;
class Solution {
public:
  int scoreOfString(string s) {
    int score = 0;

    for (int i = 0; i < s.size() - 1; i++) {
      score += abs(s[i] - s[i + 1]);
    }
    cout << "score: " << score << "\n";
    return score;
  }
};

int main() {
  auto s = Solution();
  s.scoreOfString("hello");
}
