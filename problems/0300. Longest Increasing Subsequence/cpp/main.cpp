#include <bits/stdc++.h>
using namespace std;

#define sz(a) (int)a.size()

class Solution {
  public:
    int lengthOfLIS(vector<int> &nums) {
        vector<int> dp(nums.size(), 1);

		int mx = 1;
        for (int i = 1; i < sz(nums); i++) {
            int best = 0;
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    best = max(best, dp[j]);
                }
            }
			dp[i] = best + 1;
			mx = max(mx, dp[i]);
        }

        return mx;
    }
};

int main() {
    auto s = Solution();
    vector<int> nums;

    nums = {10, 9, 2, 5, 3, 7, 101, 18};
    assert(s.lengthOfLIS(nums) == 4);

	nums = {0,1,0,3,2,3};
	assert(s.lengthOfLIS(nums) == 4);


	nums = {7,7,7,7,7,7,7};
	assert(s.lengthOfLIS(nums) == 1);

	nums = {1,3,6,7,9,4,10,5,6};
	assert(s.lengthOfLIS(nums) == 6);
}
