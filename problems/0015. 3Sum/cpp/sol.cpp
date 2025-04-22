#include <bits/stdc++.h>
using namespace std;

class Solution {
  private:
    int bsearch(vector<int> &nums, int left, int target) {
        int l = left, h = nums.size() - 1, m;

        while (l <= h) {
            m = (l + h) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] > target) {
                h = m - 1;
            } else {
                l = m + 1;
            }
        }

        return -1;
    }

    const int MAX = 1e5;

  public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        sort(nums.begin(), nums.end());

        set<vector<int>> found;
        vector<vector<int>> vfound;
        vector<int> snums{nums[0]};

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i - 1])
                snums.push_back(nums[i]);
        }

        vector<int> counter(MAX * 2 + 1, 0);
        for (auto i : nums)
            counter[i + MAX]++;

        if (counter[MAX] >= 3) {
            vector<int> base{0, 0, 0};
            vfound.push_back(base);
        }

        for (int i = 0; i < snums.size(); i++) {
            for (int j = i + 1; j < snums.size(); j++) {
                int target = bsearch(snums, j,  -(snums[i] + snums[j]));

                if (target != -1) {
                    auto count = 1 + (snums[target] == snums[i]) +
                                 (snums[target] == snums[j]);

                    if (counter[snums[target] + MAX] < count) {
                        continue;
                    }

                    vector<int> f{snums[i], snums[j], snums[target]};
                    sort(f.begin(), f.end());

                    if (found.find(f) == found.end()) {
                        vfound.push_back(f);
                    }
                    found.insert(f);
                }
            }
        }

        return vfound;
    }
};

int main() {
	auto s = Solution();
	vector<int> nums;
	vector<vector<int>> out;

	out = {{-1,-1,2},{-1,0,1}};
	nums = {-1,0,1,2,-1,-4};
	assert(s.threeSum(nums) == out);

}
