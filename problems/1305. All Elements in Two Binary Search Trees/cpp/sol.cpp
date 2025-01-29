#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
  string display() const {
    ostringstream s;
    s << "TN(" << val << ", " << (left ? left->display() : "null") << ", "
      << (right ? right->display() : "null") << ")";
    return s.str();
  }
};

class Solution {
public:
  vector<int> getAllElements(TreeNode *root1, TreeNode *root2) {
    vector<int> nums;
    queue<TreeNode *> q;

    if (root1)
      q.push(root1);
    if (root2)
      q.push(root2);

    while (!q.empty()) {
      auto curr = q.front();
      q.pop();

      nums.push_back(curr->val);

      if (curr->left)
        q.push(curr->left);

      if (curr->right)
        q.push(curr->right);
    }

    sort(nums.begin(), nums.end());

    return nums;
  }
};

TreeNode *fromVec(vector<int> vec, int pos = 1) {
  if (vec[pos - 1] == -1)
    return nullptr;

  TreeNode *node = new TreeNode();
  node->val = vec[pos - 1];

  if (pos * 2 <= (int)vec.size())
    node->left = fromVec(vec, pos * 2);

  if (pos * 2 + 1 <= (int)vec.size())
    node->right = fromVec(vec, pos * 2 + 1);

  return node;
}

int main() {
  auto s = Solution();
  vector<int> exp;

  auto root1 = fromVec({2, 1, 4});
  auto root2 = fromVec({1, 0, 3});

  exp = {0, 1, 1, 2, 3, 4};
  assert(s.getAllElements(root1, root2) == exp);

  root1 = fromVec({1, -1, 8});
  root2 = fromVec({8, 1});
  exp = {1, 1, 8, 8};
  assert(s.getAllElements(root1, root1) == exp);
}
