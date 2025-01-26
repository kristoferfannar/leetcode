#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int maximumBags(vector<int> &capacity, vector<int> &rocks,
                  int additionalRocks) {
    map<int, int> needed;
    vector<int> keys;
    int diff;

    for (int i = 0; i < (int)capacity.size(); i++) {
      diff = capacity[i] - rocks[i];

      if (needed.find(diff) == needed.end()) {
        needed[diff] = 0;
        keys.push_back(diff);
      }
      needed[diff]++;
    }

    sort(keys.begin(), keys.end());

    int full = needed[0];

    for (auto key : keys) {
      if (key == 0)
        continue;

      if (additionalRocks < key)
        break;

      int adding = min(additionalRocks / key, needed[key]);
      full += adding;
      additionalRocks -= adding * key;
    }

    return full;
  }
};

int main() {
  auto s = Solution();
  vector<int> inCap, inRocks;

  inCap = {2, 3, 4, 5}, inRocks = {1, 2, 4, 4};
  assert(s.maximumBags(inCap, inRocks, 2) == 3);
  inCap = {10, 2, 2}, inRocks = {2, 2, 0};
  assert(s.maximumBags(inCap, inRocks, 100) == 3);

  inCap = {54, 18, 91, 49, 51, 45, 58, 54,  47, 91, 90, 20, 85, 20, 90,
           49, 10, 84, 59, 29, 40, 9,  100, 1,  64, 71, 30, 46, 91},
  inRocks = {14, 13, 16, 44, 8,  20, 51, 15, 46, 76, 51, 20, 77, 13, 14,
             35, 6,  34, 34, 13, 3,  8,  1,  1,  61, 5,  2,  15, 18};
  assert(s.maximumBags(inCap, inRocks, 77) == 13);
}
