
#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
  string join(vector<string> &strs, string delim) {
    string out = strs[0];
    for (int i = 1; i < (int)strs.size(); i++) {
      out += delim + strs[i];
    }
    return out;
  }

public:
  string arrangeWords(string text) {
    text[0] += 32;
    map<int, vector<string>> lengths;

    stringstream ss(text);

    string tmp;

    while (getline(ss, tmp, ' ')) {
      int len = (int)tmp.length();
      if (lengths.find(len) == lengths.end()) {
        lengths[len] = {};
      }

      lengths[len].push_back(tmp);
    }

    string out;
    bool first = true;
    for (auto &[len, strs] : lengths) {
      if (!first) {
        out += " ";
      }
      out += join(strs, " ");
      first = false;
    }
    out[0] -= 32;

    return out;
  }
};
int main() {
  auto s = Solution();

  assert(s.arrangeWords("Leetcode is cool") == "Is cool leetcode");
  assert(s.arrangeWords("Keep calm and code on") == "On and keep calm code");
}
