#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
		string out;
		// out.reserve(s.size() + spaces.size());

		int  idx = 0;

		for (int i = 0; i < s.size(); i++) {
			if (idx < spaces.size() && i == spaces[idx]) {
				out += " ";
				idx++;
			}
			out += s[i];
		}

		return out;
    }
};


int main() {
	auto s = Solution();
	vector<int> spaces;

	spaces = {8, 13, 15};
	assert(s.addSpaces("LeetcodeHelpsMeLearn", spaces) ==  "Leetcode Helps Me Learn");

	spaces = {1,5,7,9};
	assert(s.addSpaces("icodeinpython", spaces) == "i code in py thon");

	spaces = {0,1,2,3,4,5,6};
	assert(s.addSpaces("spacing", spaces) == " s p a c i n g");
}
