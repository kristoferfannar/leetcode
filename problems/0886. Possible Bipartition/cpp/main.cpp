#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  bool possibleBipartition(int n, vector<vector<int>> &dislikes) {
    map<int, set<int>> graph;
    vector<int> members(n, 0);

    for (auto g : dislikes) {
      // zero index
      auto a = g[0] - 1, b = g[1] - 1;

      members[a] = 0;
      members[b] = 0;

      if (graph.find(a) == graph.end()) {
        set<int> s;
        graph[a] = s;
      }
      if (graph.find(b) == graph.end()) {
        set<int> s;
        graph[b] = s;
      }
      graph[a].insert(b);
      graph[b].insert(a);
    }

    for (int i = 0; i < n; i++) {
      if (members[i] == 0) {
        vector<int> stk{i};
        members[i] = 1;

        while (!stk.empty()) {
          auto curr = stk.back();
          stk.pop_back();

          for (auto other : graph[curr]) {
            if (members[other] == members[curr]) {
              return false;
            } else if (members[other] == 0) {
              stk.push_back(other);
              members[other] = 3 - members[curr];
            }
          }
        }
      }
    }

    return true;
  }
};

int main() {
  auto s = Solution();
  vector<vector<int>> in;

  in = {{1, 2}, {1, 3}, {2, 4}};
  assert(s.possibleBipartition(4, in) == true);

  in = {{1, 2}, {1, 3}, {2, 3}};
  assert(s.possibleBipartition(3, in) == false);
}
