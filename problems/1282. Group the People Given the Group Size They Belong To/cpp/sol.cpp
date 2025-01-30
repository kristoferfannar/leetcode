#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<vector<int>> groupThePeople(vector<int> &groupSizes) {
    map<int, vector<int>> groups;

    for (int i = 0; i < (int)groupSizes.size(); i++) {
      int g = groupSizes[i];
      if (groups.find(g) == groups.end())
        groups[g] = {};

      groups[g].push_back(i);
    }

    vector<vector<int>> final;
    for (auto [size, members] : groups) {

      for (int i = 0; i < (int)members.size(); i += size) {
        vector<int> sb(members.begin() + i, members.begin() + i + size);
        final.push_back(sb);
      }
    }

    return final;
  }
};

int main() {
  vector<vector<int>> exp;
  vector<int> in;
  auto s = Solution();

  in = {3, 3, 3, 3, 3, 1, 3};
  exp = {{5}, {0, 1, 2}, {3, 4, 6}};
  assert(s.groupThePeople(in) == exp);
}
