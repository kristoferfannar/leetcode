#include <bits/stdc++.h>
using namespace std;

#define sz(s) (int)s.size()

class Solution {

  private:
    vector<int> buildp(string &s) {
        vector<int> p(sz(s), 0);

        int k = 0;
        for (int i = 1; i < sz(s); i++) {
            while (k && s[i] != s[k])
                k = p[k - 1];

            if (s[i] == s[k])
                k++;
            p[i] = k;
        }
        return p;
    }

  public:
    string longestPrefix(string s) {
        auto p = buildp(s);

		string out = s.substr(0, p.back());
        return out;
    }
};

int main() {
    auto s = Solution();

    assert(s.longestPrefix("level") == "l");
	assert(s.longestPrefix("ababab") == "abab");
}
