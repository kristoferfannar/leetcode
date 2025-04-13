#include <bits/stdc++.h>
using namespace std;

#define sz(s) (int)s.size()


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

TreeNode *tn(vector<int> &v, int idx = 1) {
    if (idx > sz(v))
        return nullptr;

    TreeNode *t = new TreeNode(v[idx - 1]);
    t->left = tn(v, idx * 2);
    t->right = tn(v, idx * 2 + 1);

    return t;
}

vector<int> vec(TreeNode *t) {
    queue<TreeNode *> ts;
    ts.push(t);
    vector<int> out;

    while (!ts.empty()) {
        auto curr = ts.front();
        ts.pop();
        if (curr == nullptr)
            continue;

        ts.push(curr->left);
        ts.push(curr->right);
        out.push_back(curr->val);
    }

    return out;
}

class Solution {
  public:
    TreeNode *reverseOddLevels(TreeNode *root) {
        vector<TreeNode *> evens, odds;
        evens.push_back(root);

        while (!evens.empty() || !odds.empty()) {
            for (int i = 0; i < sz(evens); i++) {
                auto curr = evens[i];

                if (curr->left)
                    odds.push_back(curr->left);
                if (curr->right)
                    odds.push_back(curr->right);
            }

			evens.clear();

            for (int i = 0; i < sz(odds); i++) {
                auto curr = odds[i];

				if (i < sz(odds) / 2) {
					auto tmp = curr->val;
					int j = sz(odds) - i - 1;

					curr->val = odds[j]->val;
					odds[j]->val = tmp;
				}

                if (curr->left)
                    evens.push_back(curr->left);
                if (curr->right)
                    evens.push_back(curr->right);
            }

			odds.clear();
        }

        return root;
    }
};


int main() {
    auto s = Solution();

    vector<int> v, exp;
    TreeNode *t;

    v = {2, 3, 5, 8, 13, 21, 34};
    t = tn(v);
    exp = {2, 5, 3, 8, 13, 21, 34};

    assert(vec(s.reverseOddLevels(t)) == exp);
}
