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
};

void dfs(TreeNode *node, int lvl, map<int, int> &lvls) {
  if (!node)
    return;

  if (lvls.find(lvl) == lvls.end())
    lvls[lvl] = 0;

  lvls[lvl] += node->val;

  dfs(node->left, lvl + 1, lvls);
  dfs(node->right, lvl + 1, lvls);
}

class Solution {
public:
  int maxLevelSum(TreeNode *root) {

    map<int, int> levels;

    dfs(root, 1, levels);

    int maxLvl = 0, maxScore = INT_MIN;

    for (auto [lvl, score] : levels) {

      if (score > maxScore) {
        maxLvl = lvl;
        maxScore = score;
      }
    }

    return maxLvl;
  }
};

TreeNode *fromVec(vector<int> vec, int pos = 1) {
  TreeNode *parent = new TreeNode();
  parent->val = vec[pos - 1];

  if (pos * 2 <= (int)vec.size()) {
    parent->left = fromVec(vec, pos * 2);
  }

  if (pos * 2 + 1 <= (int)vec.size()) {
    parent->right = fromVec(vec, pos * 2 + 1);
  }

  return parent;
}

int main() {
  auto vec = {1, 7, 0, 7, -8};

  for (auto i : vec)
    cout << i << " ";
  cout << endl;

  auto tn = fromVec(vec);
  // cout << tn->display() << endl;
  auto s = Solution();

  assert(s.maxLevelSum(tn) == 2);
}
