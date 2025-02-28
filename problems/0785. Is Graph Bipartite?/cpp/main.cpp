#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  bool isBipartite(vector<vector<int>> &graph) {
    vector<int> teams(graph.size(), 0);
    vector<int> frontier;

    for (int i = 0; i < graph.size(); i++) {
      if (teams[i] == 0) {
        teams[i] = 1;
        frontier.push_back(i);
        while (!frontier.empty()) {
          auto curr = frontier.back();
          frontier.pop_back();
          for (auto n : graph[curr]) {
            if (teams[n] == teams[curr]) {
              return false;
            }

            if (teams[n] == 0) {
              teams[n] = 3 - teams[curr];
              frontier.push_back(n);
            }
          }
        }
      }
    }

    return true;
  }
};
