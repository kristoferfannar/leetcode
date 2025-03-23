#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
		int pairs = 0;

		for (int i = 0; i < nums.size(); i++) {
			for (int j = 0; j < nums.size(); j++) {
				if (j == i) continue;
				if (nums[i] + nums[j] == target) pairs++;
			}
		}

		return pairs;
    }
};

int main() {
	auto s =Solution();
	vector<string> nums;

	nums = {"777","7","77","77"};
	assert(s.numOfPairs(nums, "7777") == 4);
}
