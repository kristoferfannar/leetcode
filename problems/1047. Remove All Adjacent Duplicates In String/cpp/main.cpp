#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string removeDuplicates(string s) {
    vector<char> stk;
    for (auto i : s) {
      if (!stk.empty() && stk.back() == i)
        stk.pop_back();
      else
        stk.push_back(i);
    }

    string out;
    for (auto i : stk) {
      out += i;
    }

    return out;
  }
};

int main() {
  auto s = Solution();

  assert(s.removeDuplicates("abbaca") == "ca");
  assert(s.removeDuplicates("azxxzy") == "ay");
}
