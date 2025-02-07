#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
  char hashStr(const string &str, int start, int stop) {
    int sum = 0;
    for (int i = start; i < stop; i++)
      sum += str[i] - 'a';

    return char(sum % 26 + 'a');
  }

public:
  string stringHash(string s, int k) {
    string hashed;
    for (int i = 0; i < (int)s.size(); i += k)
      hashed += hashStr(s, i, i + k);

    return hashed;
  }
};

int main() {
  auto s = Solution();

  assert(s.stringHash("abcd", 2) == "bf");
  assert(s.stringHash("mxz", 3) == "i");
}
