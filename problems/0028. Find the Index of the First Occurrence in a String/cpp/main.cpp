#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() > haystack.size())
            return -1;
        for (int i = 0; i <= (int)(haystack.size() - needle.size()); i++) {
            if (needle == haystack.substr(i, needle.size())) {
                return i;
            }
        }

        return -1;
    }
};
