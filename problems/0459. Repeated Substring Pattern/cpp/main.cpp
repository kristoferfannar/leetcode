#include <bits/stdc++.h>
using namespace std;

#define sz(s) (int)s.size()

class Solution {
  private:
    /* KMP: cracked linear time solution */
    vector<int> buildp(string &s) {
        vector<int> p(sz(s));

        int k = 0;
        for (int i = 1; i < sz(s); i++) {
            while (k && s[i] != s[k])
                k = p[k-1];

            if (s[i] == s[k])
                k++;
            p[i] = k;
        }

        return p;
    }

    /* boring naive solution */
    bool naive(string s) {
        for (int i = 1; i <= sz(s) / 2; i++) {
            if (sz(s) % i == 0) {
                auto success = true;
                for (int j = 1; j < sz(s) / i; j++) {
                    if (s.substr(0, i) != s.substr(j * i, i)) {
                        success = false;
                        break;
                    }
                }

                if (success)
                    return true;
            }
        }
        return false;
    }

  public:
    bool repeatedSubstringPattern(string s) { 
		// return naive(s);

        auto p = buildp(s);
        return p.back() && sz(s) % (sz(s) - p.back()) == 0;
    }
};

int main() {
    auto s = Solution();

    assert(s.repeatedSubstringPattern("ababab") == true);
    assert(s.repeatedSubstringPattern("abab") == true);
    assert(s.repeatedSubstringPattern("aba") == false);
    assert(s.repeatedSubstringPattern("abcabcabcabc") == true);
    assert(s.repeatedSubstringPattern("abcabc") == true);
    assert(s.repeatedSubstringPattern("bb") == true);
    assert(s.repeatedSubstringPattern("bbb") == true);
    assert(s.repeatedSubstringPattern("bbbb") == true);
	assert(s.repeatedSubstringPattern("ababba") == false);
}
