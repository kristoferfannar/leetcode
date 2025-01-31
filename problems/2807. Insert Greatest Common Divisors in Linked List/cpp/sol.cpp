#include <bits/stdc++.h>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
  string display() const {
    ostringstream s;
    s << "LN(" << val << ", " << (next ? next->display() : "null") << ")";
    return s.str();
  }
};

class Solution {
public:
  ListNode *insertGreatestCommonDivisors(ListNode *head) {

    auto curr = head, next = head->next;

    while (curr && next) {
      auto mid = new ListNode(gcd(curr->val, next->val));
      curr->next = mid;
      mid->next = next;

      curr = next;
      next = curr ? curr->next : nullptr;
    }

    return head;
  }
};

ListNode *fromVec(vector<int> vec, int pos = 0) {
  if (pos >= (int)vec.size())
    return nullptr;

  ListNode *node = new ListNode();

  node->val = vec[pos];
  node->next = fromVec(vec, pos + 1);

  return node;
}

vector<int> toVec(ListNode *head) {
  vector<int> vec;

  ListNode *curr = head;

  while (curr) {
    vec.push_back(curr->val);
    curr = curr->next;
  }

  return vec;
}

int main() {
  auto s = Solution();
  vector<int> exp;

  auto head = fromVec({18, 6, 10, 3});

  exp = {18, 6, 6, 2, 10, 1, 3};
  auto got = toVec(s.insertGreatestCommonDivisors(head));
  assert(got == exp);
}
