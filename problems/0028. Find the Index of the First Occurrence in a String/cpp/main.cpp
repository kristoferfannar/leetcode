#include <bits/stdc++.h>
using namespace std;

#define sz(a) (int)a.size()

class Solution {
  private:
    vector<int> buildp(string needle) {
        vector<int> p(needle.size(), 0);
        int k = 0;

        for (int i = 1; i < sz(needle); i++) {
            while (k && needle[k] != needle[i])
                k = p[k - 1];

			if(needle[k] == needle[i])
				++k;
			p[i] = k;
        }

        return p;
    }

    /* KMP: blazing fast o(n+m) sol using */
    int kmp(string haystack, string needle) {
        if (needle.size() > haystack.size())
            return -1;

        auto p = buildp(needle);

        int hi = 0, ni = 0;

        while (hi < sz(haystack) && ni < sz(needle)) {
            if (haystack[hi] == needle[ni]) {
                hi++;
                ni++;
            } else if (ni == 0) {
                hi++;
            } else {
                ni = p[ni - 1];
            }
        }

        if (ni == sz(needle))
            return hi - sz(needle);

        return -1;
    }

    /* naive o(n*m) sol */
    int naive(string haystack, string needle) {
        if (needle.size() > haystack.size())
            return -1;
        for (int i = 0; i <= (int)(haystack.size() - needle.size()); i++) {
            if (needle == haystack.substr(i, needle.size())) {
                return i;
            }
        }

        return -1;
    }

  public:
    int strStr(string haystack, string needle) {
        return kmp(haystack, needle);
        // return naive(haystack, needle);
    }
};

int main() {
    auto s = Solution();
    assert(s.strStr("sadbutsad", "sad") == 0);
    assert(s.strStr("leetcode", "leeto") == -1);
    assert(s.strStr("mississippi", "issip") == 4);
    assert(s.strStr("ababcaababcaabc", "ababcaabc") == 6);
}
