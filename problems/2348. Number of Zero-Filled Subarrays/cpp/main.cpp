#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
		int curr = 0;
		long long total = 0;

		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] == 0)  
				curr++;
			else  
				curr = 0;
			
			total += curr;
		}

		return total;
    }
};

int main() {
	auto s =Solution();
	vector<int> nums;

	nums = {1,3,0,0,2,0,0,4};
	assert(s.zeroFilledSubarray(nums) == 6);

	nums = {0,0,0,2,0,0};
	assert(s.zeroFilledSubarray(nums) == 9);
}
