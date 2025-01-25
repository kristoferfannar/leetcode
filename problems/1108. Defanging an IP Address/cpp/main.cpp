#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string defangIPaddr(string address) {
    string defanged;

    stringstream ss(address);
    string tmp;

    vector<string> numbers;

    while (getline(ss, tmp, '.')) {
      numbers.push_back(tmp);
    }

    bool first = true;
    for (auto i : numbers) {
      if (!first)
        defanged += "[.]";

      defanged += i;
      first = false;
    }

    return defanged;
  }
};

int main() {
  auto s = Solution();
  assert(s.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1");
  assert(s.defangIPaddr("255.20.100.1") == "255[.]20[.]100[.]1");
}
