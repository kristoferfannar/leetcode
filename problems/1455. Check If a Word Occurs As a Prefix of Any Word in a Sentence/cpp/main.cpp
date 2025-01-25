#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int isPrefixOfWord(string sentence, string searchWord) {
    stringstream ss(sentence);

    string word;

    int w = 0;

    while (getline(ss, word, ' ')) {
      w++;

      if (word.compare(0, searchWord.length(), searchWord) == 0)
        return w;
    }
    return -1;
  }
};

int main() {
  auto s = Solution();

  assert(s.isPrefixOfWord("i love eating burger", "burg") == 4);
}
