#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    vector<long long> findPrefixScore(vector<int>& nums) {
		vector<long long> score(nums.size());

		score[0] = 2 * nums[0];
		int mx = nums[0];

		for (int i = 1; i < (int)nums.size(); i++) {
			mx = max(mx, nums[i]);
			score[i] = score[i-1] + nums[i] + mx;
		}

		return score;
    }
};

int main() {
	auto s = Solution();
	vector<int> nums;
	vector<long long> out;

	nums = {2,3,7,5,10};
	out = {4,10,24,36,56};
	assert(s.findPrefixScore(nums) == out);

	nums = {1,1,2,4,8,16};
	out = {2,4,8,16,32,64};
	assert(s.findPrefixScore(nums) == out);
}
