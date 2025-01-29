#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

class Solution {
public:
  int maxIceCream(vector<int> &costs, int coins) {
    map<int, ll> counter;

    for (auto i : costs) {
      if (counter.find(i) == counter.end())
        counter[i] = 0;
      counter[i]++;
    }

    auto cmp = [](pair<int, ll> a, pair<int, ll> b) {
      return a.first > b.first;
    };
    priority_queue<pair<int, ll>, vector<pair<int, ll>>, decltype(cmp)> queue(
        cmp);

    for (auto [prize, count] : counter)
      queue.push(pair(prize, count));

    int bought = 0;

    while (!queue.empty() && coins >= queue.top().first) {
      auto next = queue.top();
      queue.pop();

      if ((ll)coins < (ll)next.first * (ll)next.second) {
        bought += coins / next.first;
        coins -= (coins / next.first) * next.first;
      } else {
        bought += next.second;
        coins -= next.first * next.second;
      }
    }

    return bought;
  }
};

int main() {
  auto s = Solution();
  vector<int> in;

  in = {1, 3, 2, 4, 1};
  assert(s.maxIceCream(in, 7) == 4);

  in = {10, 6, 8, 7, 7, 8};
  assert(s.maxIceCream(in, 5) == 0);

  in = {1, 6, 3, 1, 2, 5};
  assert(s.maxIceCream(in, 20) == 6);

  in = {4, 7, 6, 4, 4, 2, 2, 4, 8, 8};
  assert(s.maxIceCream(in, 41) == 9);
}
