#include <bits/stdc++.h>
using namespace std;

#define sz(s) (int)s.size()

class Solution {
  public:
    int myAtoi(string s) {
        int out = 0;
        bool isNeg = false, found = false;

        for (int i = 0; i < sz(s); i++) {
            if (!found && (s[i] == ' ' || s[i] == '\t' || s[i] == '\n')) {
                continue;
            }
            if (s[i] == '-' || s[i] == '+') {
                if (found) {
                    break;
                }
                found = true;
                isNeg = s[i] == '-';
                continue;
            }

            if (s[i] >= '0' && s[i] <= '9') {
                found = true;

                if (out > INT_MAX / 10 ||
                    (out == INT_MAX / 10 && (s[i] - '0') > 7)) {
                    return isNeg ? INT_MIN : INT_MAX;
                    break;
                }
                out *= 10;
                out += s[i] - '0';
            } else {
                break;
            }
        }

        if (found == false)
            return 0;

        return (isNeg * -2 + 1) * out;
    }
};

int main() {
    auto s = Solution();
    assert(s.myAtoi("42") == 42);
    assert(s.myAtoi("1337c0d3") == 1337);
    assert(s.myAtoi(" -042") == -42);
    assert(s.myAtoi("0-1") == 0);
    assert(s.myAtoi("words and 987") == 0);
    assert(s.myAtoi("-91283472332") == INT_MIN);
    assert(s.myAtoi("+1") == 1);
    assert(s.myAtoi("+-12") == 0);
    assert(s.myAtoi("-2147483647") == -2147483647);
}
