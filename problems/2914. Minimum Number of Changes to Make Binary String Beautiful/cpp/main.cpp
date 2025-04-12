#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int minChanges(string s) {

        int ops = 0;
        for (int i = 0; i < s.size(); i += 2) {
            if (s[i] != s[i + 1]) {
                ops++;
            }
        }

		return ops;
    }
};

int main() {
    auto s = Solution();
    assert(s.minChanges("1001") == 2);
	assert(s.minChanges("0000") == 0);
}
