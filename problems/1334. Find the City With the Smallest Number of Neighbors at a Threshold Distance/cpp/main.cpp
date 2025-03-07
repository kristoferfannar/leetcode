#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int findTheCity(int n, vector<vector<int>> &edges, int distanceThreshold) {

    vector<vector<long long>> graph(n);
    for (int i = 0; i < n; i++) {
      vector<long long> row(n, INT_MAX);
      graph[i] = row;
      graph[i][i] = 0;
    }

    for (auto edge : edges) {
      auto f = edge[0], s = edge[1], cost = edge[2];
      graph[f][s] = cost;
      graph[s][f] = cost;
    }

    for (int k = 0; k < n; k++)
      for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
          graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);

    int bestCity = -1;
    int bestCount = INT_MAX;
    for (int city = 0; city < n; city++) {
      int currCount = 0;

      for (int neighbor = 0; neighbor < n; neighbor++) {
        if (graph[city][neighbor] <= distanceThreshold)
          currCount++;
      }

      if (currCount <= bestCount) {
        bestCity = city;
        bestCount = currCount;
      }
    }

    return bestCity;
  }
};

int main() {
  auto s = Solution();
  vector<vector<int>> edges;

  edges = {{0, 1, 3}, {1, 2, 1}, {1, 3, 4}, {2, 3, 1}};
  assert(s.findTheCity(4, edges, 4) == 3);

  edges = {{0, 1, 2}, {0, 4, 8}, {1, 2, 3}, {1, 4, 2}, {2, 3, 1}, {3, 4, 1}};
  assert(s.findTheCity(5, edges, 2) == 0);
}
