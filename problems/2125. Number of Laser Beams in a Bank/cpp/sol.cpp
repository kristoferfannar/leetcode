#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int numberOfBeams(vector<string> &bank) {
    vector<int> found;

    for (auto row : bank)
      if (row.find("1") != string::npos)
        found.push_back((int)count(row.begin(), row.end(), '1'));

    int total = 0;
    for (int i = 0; i < (int)found.size() - 1; i++)
      total += found[i] * found[i + 1];

    return total;
  }
};

int main() {
  auto s = Solution();
  vector<string> in;

  in = {"011001", "000000", "010100", "001000"};
  assert(s.numberOfBeams(in) == 8);
}
