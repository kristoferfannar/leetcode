#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numSub(string s) {
		int total = 0, curr = 0;


		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '1') curr++;
			else curr = 0;

			total += curr;
			total = total % (int)(1e9 + 7);
		}


		return total;
    }
};

int main() {
	auto s = Solution();

	assert(s.numSub("0110111") == 9);
	assert(s.numSub("111111") == 21);
}
