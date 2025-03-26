#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> maxScoreIndices(vector<int> &nums) {
    int n = (int)nums.size();
    vector<int> l(n), r(n);

	l[0] = 0;
    r[n - 1] = nums[n - 1] == 1;
    for (int i = 1; i < n; i++) {
      l[i] = l[i - 1] + (nums[i-1] == 0);
      r[n - i - 1] = r[n - i] + (nums[n - i - 1] == 1);
    }

	vector<int> mxs{0};
	int mx = l[0] + r[0];

	for (int i = 1; i < n; i++) {
		if (l[i] + r[i] > mx) {
			mxs = {i};
			mx = l[i] + r[i];
		} else if (l[i] + r[i] == mx) {
			mxs.push_back(i);
		}
	}

	if (l[n-1] + (nums[n-1] == 0) > mx) {
		mxs = {n};
	} else if (l[n-1] + (nums[n-1] ==0) == mx) {
		mxs.push_back(n);
	}


	return mxs;
  }
};

int main() {
  auto s = Solution();
  vector<int> nums, exp;

  nums = {0, 0, 1, 0};
  exp = {2, 4};
  assert(s.maxScoreIndices(nums) == exp);

  nums = {0,0,0};
  exp = {3};
  assert(s.maxScoreIndices(nums) == exp);

  nums = {1, 1};
  exp = {0};
  assert(s.maxScoreIndices(nums) == exp);
}

