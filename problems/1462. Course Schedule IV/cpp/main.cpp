#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<bool> checkIfPrerequisite(int numCourses,
                                   vector<vector<int>> &prerequisites,
                                   vector<vector<int>> &queries) {

    vector<vector<bool>> graph(numCourses);
    for (int i = 0; i < numCourses; i++) {
      vector<bool> row(numCourses, false);
      graph[i] = row;
    }

    for (auto pre : prerequisites) {
      auto f = pre[0], s = pre[1];
      graph[f][s] = 1;
    }

    for (int k = 0; k < numCourses; k++)
      for (int i = 0; i < numCourses; i++)
        for (int j = 0; j < numCourses; j++)
          graph[i][j] = graph[i][j] || (graph[i][k] && graph[k][j]);

    vector<bool> out;

    for (auto q : queries) {
      auto f = q[0], s = q[1];

      out.push_back(graph[f][s]);
    }

    return out;
  }
};

int main() {
  auto s = Solution();
  vector<bool> exp;
  vector<vector<int>> pre, qs;

  pre = {{1, 0}}, qs = {{0, 1}, {1, 0}};
  exp = {false, true};
  assert(s.checkIfPrerequisite(2, pre, qs) == exp);

  pre = {}, qs = {{1, 0}, {0, 1}};
  exp = {false, false};
  assert(s.checkIfPrerequisite(2, pre, qs) == exp);

  pre = {{1, 2}, {1, 0}, {2, 0}}, qs = {{1, 0}, {1, 2}};
  exp = {true, true};
  assert(s.checkIfPrerequisite(3, pre, qs) == exp);
}
