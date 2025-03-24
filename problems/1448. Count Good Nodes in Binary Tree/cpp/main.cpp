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
};

class Solution {
public:
  int goodNodes(TreeNode *root, int mx = INT_MIN) {
    if (root == nullptr)
      return 0;

    return (root->val >= mx) + goodNodes(root->left, max(root->val, mx)) +
           goodNodes(root->right, max(root->val, mx));
  }
};

TreeNode *tn(vector<int> &vec, int idx = 1) {
  if (idx > (int)vec.size())
    return nullptr;
  if (vec[idx - 1] == INT_MIN)
    return nullptr;

  TreeNode *root = new TreeNode(vec[idx - 1]);

  root->left = tn(vec, idx * 2);
  root->right = tn(vec, idx * 2 + 1);

  return root;
}

int main() {
  auto s = Solution();
  vector<int> vec;

  vec = {3, 1, 4, 3, INT_MIN, 1, 5};
  TreeNode *root = tn(vec);
  // cout << "got " << s.goodNodes(root) << endl;
  assert(s.goodNodes(root) == 4);

  vec = {3, 3, INT_MIN, 4, 2};
  root = tn(vec);
  assert(s.goodNodes(root) == 3);
}
