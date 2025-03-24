#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minimumRounds(vector<int> &tasks) {
    map<int, int> counter;
    int rounds = 0;

    for (auto i : tasks)
      counter[i]++;

    for (auto [num, count] : counter) {
      if (count % 3 == 0)
        rounds += count / 3;
      else if (count % 3 == 2)
        rounds += (count / 3) + 1;
      else if (count % 3 == 1) {
        if (count < 3)
          return -1;
        rounds += (count / 3) + 1;
      }
    }

    return rounds;
  }
};

int main() {
  auto s = Solution();
  vector<int> tasks;

  tasks = {2, 2, 3, 3, 2, 4, 4, 4, 4, 4};
  assert(s.minimumRounds(tasks) == 4);

  tasks = {2, 3, 3};
  assert(s.minimumRounds(tasks) == -1);

  tasks = {5, 5, 5, 5};
  assert(s.minimumRounds(tasks) == 2);
}
