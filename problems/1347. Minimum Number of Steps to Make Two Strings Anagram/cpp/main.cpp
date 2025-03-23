#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSteps(string s, string t) {
		vector<int> counter(26);

		for (int i= 0; i < s.size(); i++) {
			counter[s[i] - 'a']++;
			counter[t[i] - 'a']--;
		}

		int steps = 0;
		for (auto count : counter) {
			steps += abs(count);
		}

		return steps / 2;
    }
};

int main() {
	auto s = Solution();

	assert(s.minSteps("bab","aba") == 1);

	assert(s.minSteps("leetcode", "practice") == 5);

	assert(s.minSteps("anagram", "mangaar") == 0);
}
