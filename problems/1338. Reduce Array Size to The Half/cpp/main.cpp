#include <bits/stdc++.h>
#include <queue>
using namespace std;

class Solution {
public:
  int minSetSize(vector<int> &arr) {
    map<int, int> counter;

    for (auto i : arr)
      counter[i]++;

    auto cmp = [](pair<int, int> a, pair<int, int> b) {
      return a.second < b.second;
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> q(
        cmp);

    for (auto [num, count] : counter)
      q.push(pair(num, count));

    int rm = 0;

    while (rm < (int)arr.size() / 2) {
      auto [a, b] = q.top();
      q.pop();

      rm += b;
    }
    // cout << "front: " << q.top().first << ", " << q.top().second << endl;

    return counter.size() - q.size();
  }
};

int main() {
  auto s = Solution();
  vector<int> arr;

  arr = {3, 3, 3, 3, 5, 5, 5, 2, 2, 7};
  assert(s.minSetSize(arr) == 2);

  arr = {7, 7, 7, 7, 7, 7};
  assert(s.minSetSize(arr) == 1);

  arr = {1, 2};
  assert(s.minSetSize(arr) == 1);
}
