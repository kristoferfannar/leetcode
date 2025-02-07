#include <bits/stdc++.h>
#include <queue>
using namespace std;

class Solution {
public:
  int minSetSize(vector<int> &arr) {
    map<int, int> counter;

    for (auto i : arr)
      counter[i]++;

    priority_queue<int> q;
    for (auto [num, count] : counter)
      q.push(count);

    int rm = 0;

    while (rm < (int)arr.size() / 2) {
      rm += q.top();
      q.pop();
    }

    return (int)counter.size() - (int)q.size();
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
