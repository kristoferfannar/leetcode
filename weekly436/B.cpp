#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> assignElements(vector<int> &groups, vector<int> &elements) {
    int n = (int)groups.size();
    vector<int> assigned(n, -1);

    map<int, int> items;
    for (int i = 0; i < (int)elements.size(); i++) {
      if (items.find(elements[i]) == items.end()) {
        items[elements[i]] = i;
      }
    }

    // for (auto [num, idx] : items) {
    //   cout << num << " -> " << idx << endl;
    // }

    for (int i = 0; i < n; i++) {
      // cout << "checking groups[" << i << "] = " << groups[i] << endl;
      for (int num = 2; num * num <= groups[i]; num++) {
        if (groups[i] % num)
          continue;
        if (items.find(num) == items.end() &&
            items.find(groups[i] / num) == items.end())
          continue;

        if (items.find(num) != items.end()) {
          // cout << "found num = " << num << endl;
          if (assigned[i] != -1) {
            assigned[i] = min(assigned[i], items[num]);
          } else {
            assigned[i] = items[num];
          }
        }

        if (items.find(groups[i] / num) != items.end()) {
          // cout << "found num = " << groups[i] / num << endl;
          if (assigned[i] != -1) {
            assigned[i] = min(assigned[i], items[groups[i] / num]);
          } else {
            assigned[i] = items[groups[i] / num];
          }
        }
      }
      if (items.find(groups[i]) != items.end()) {
        if (assigned[i] == -1) {
          assigned[i] = items[groups[i]];
        } else {
          assigned[i] = min(assigned[i], items[groups[i]]);
        }
      }

      if (items.find(1) != items.end()) {
        if (assigned[i] == -1) {
          assigned[i] = items[1];
        } else {
          assigned[i] = min(assigned[i], items[1]);
        }
      }
    }

    // cout << "assigned: ";
    // for (auto i : assigned)
    //   cout << i << " ";
    // cout << endl;

    return assigned;
  }
};

int main() {
  auto s = Solution();
  vector<int> groups, elements, exp;

  groups = {8, 4, 3, 2, 4};
  elements = {4, 2};
  exp = {0, 0, -1, 1, 0};
  assert(s.assignElements(groups, elements) == exp);

  groups = {2, 3, 5, 7};
  elements = {5, 3, 3};
  exp = {-1, 1, 0, -1};
  assert(s.assignElements(groups, elements) == exp);

  groups = {10, 21, 30, 41};
  elements = {2, 1};
  exp = {0, 1, 0, 1};
  assert(s.assignElements(groups, elements) == exp);
}
