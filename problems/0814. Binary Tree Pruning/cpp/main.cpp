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
    std::ostringstream s;

    s << "TN(" << val << ", " << (left == nullptr ? "nullptr" : left->display())
      << ", " << (right == nullptr ? "nullptr" : right->display()) << ")";

    return s.str();
  }

  bool operator==(const TreeNode other) const {
    if ((left == nullptr) != (other.left == nullptr)) {
      cout << "!left: " << left << " - " << other.left << endl;
      return false;
    }

    if ((right == nullptr) != (other.right == nullptr)) {
      cout << "!right: " << right << " - " << other.right << endl;
      return false;
    }

    if (val != other.val) {
      cout << "!val: " << val << " - " << other.val << endl;
      return false;
    }

    if (left != nullptr && other.left != nullptr && !(*left == *other.left))
      return false;
    if (right != nullptr && other.right != nullptr && !(*right == *other.right))
      return false;

    return true;
  }
};

class Solution {
private:
  bool prune(TreeNode *node) {
    if (node == nullptr)
      return false;

    if (!prune(node->left)) {
      node->left = nullptr;
    }

    if (!prune(node->right)) {
      node->right = nullptr;
    }
    return (node->val == 1 || node->left || node->right);
  }

public:
  TreeNode *pruneTree(TreeNode *root) {
    prune(root);

    if (root->val == 0 && !root->left && !root->right)
      return nullptr;

    return root;
  }
};

int main() {
  auto s = Solution();

  auto root = new TreeNode(1, nullptr,
                           new TreeNode(0, new TreeNode(0), new TreeNode(1)));
  auto exp =
      new TreeNode(1, nullptr, new TreeNode(0, nullptr, new TreeNode(1)));

  auto got = s.pruneTree(root);
  cout << got->display() << endl;
  cout << exp->display() << endl;
  assert(*got == *exp);
}
