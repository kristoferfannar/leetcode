#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int mySqrt(int x) {

    long long lo = 1, hi = x;
    while (lo <= hi) {
      long long mid = (lo + hi) / 2;
      if (mid * mid == x)
        return (int)mid;
      else if (mid * mid > x)
        hi = mid - 1;
      else
        lo = mid + 1;
    }

    return (int)hi;
  }
};

int main() {
  auto s = Solution();
  assert(s.mySqrt(4) == 2);
  assert(s.mySqrt(100) == 10);
  assert(s.mySqrt(8) == 2);
  assert(s.mySqrt(2147395599) == 46'339);
}
