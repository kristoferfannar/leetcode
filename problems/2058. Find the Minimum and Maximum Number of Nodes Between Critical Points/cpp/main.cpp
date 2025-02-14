#include <bits/stdc++.h>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  vector<int> nodesBetweenCriticalPoints(ListNode *head) {
    auto node = head;

    int first = -1, last = -1, curr = -1, mn = -1;
    while (node && node->next && node->next->next) {
      curr++;

      if ((node->val < node->next->val &&
           node->next->val > node->next->next->val) ||
          (node->val > node->next->val &&
           node->next->val < node->next->next->val)) {

        if (first == -1)
          first = curr;
        else if (mn == -1)
          mn = curr - last;
        else
          mn = min(mn, curr - last);

        last = curr;
      }
      node = node->next;
    }

    if (last == -1 || last == first)
      return {-1, -1};

    return {mn, last - first};
  }
};

ListNode *fromVec(vector<int> &vec) {
  ListNode *ln = new ListNode(vec[0]);
  auto curr = ln;

  for (int i = 1; i < (int)vec.size(); i++) {
    ListNode *nw = new ListNode(vec[i]);
    curr->next = nw;
    curr = nw;
  }

  return ln;
}

vector<int> toVec(ListNode *head) {
  auto curr = head;
  vector<int> out;

  while (curr) {
    out.push_back(curr->val);
    curr = curr->next;
  }

  return out;
}

int main() {
  auto s = Solution();

  vector<int> vec{3, 1}, exp;
  ListNode *ln = fromVec(vec);

  exp = {-1, -1};
  assert(s.nodesBetweenCriticalPoints(ln) == exp);

  vec = {5, 3, 1, 2, 5, 1, 2};
  ln = fromVec(vec);
  exp = {1, 3};
  assert(s.nodesBetweenCriticalPoints(ln) == exp);

  vec = {1, 3, 2, 2, 3, 2, 2, 2, 7};
  ln = fromVec(vec);
  exp = {3, 3};
  assert(s.nodesBetweenCriticalPoints(ln) == exp);
}
