#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
		int n = (int)nums.size();
		int ops = 0;
		for (int i = 0; i < n - 2; i++) {
			if (nums[i] == 0) {
				ops++;
				nums[i] = 1 - nums[i];
				nums[i+1] = 1 - nums[i+1];
				nums[i+2] = 1 - nums[i+2];
			}

		}

		if (nums[n -1] && nums[n-2]) 
			return ops;
		return -1;
    }
};

int main() {
	auto s = Solution();
	vector<int> nums;


	nums = {0,1,1,1,0,0};
	assert(s.minOperations(nums) == 3);

	nums = {0, 1, 1, 1};
	assert(s.minOperations(nums) == -1);
}
