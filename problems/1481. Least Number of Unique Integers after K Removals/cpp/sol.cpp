#include <bits/stdc++.h>
#include <queue>
using namespace std;

class Solution {
public:
  int findLeastNumOfUniqueInts(vector<int> &arr, int k) {

    auto cmp = [](pair<int, int> a, pair<int, int> b) {
      return a.second > b.second;
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> q(
        cmp);

    map<int, int> counter;
    for (auto i : arr)
      counter[i]++;

    for (auto [num, count] : counter)
      q.push(pair(num, count));

    while (k) {
      auto curr = q.top();
      if (k >= curr.second) {
        k -= curr.second;
        q.pop();
      }

      else
        k = 0;
    }

    return (int)q.size();
  }
};

int main() {
  auto s = Solution();
  vector<int> in;

  in = {5, 5, 4};
  assert(s.findLeastNumOfUniqueInts(in, 1) == 1);

  in = {4, 3, 1, 1, 3, 3, 2};
  assert(s.findLeastNumOfUniqueInts(in, 3) == 2);
}
