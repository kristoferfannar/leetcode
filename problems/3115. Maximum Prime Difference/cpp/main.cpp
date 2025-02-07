#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int maximumPrimeDifference(vector<int> &nums) {
    // sacrifice all sanity for speed
    vector<int> primes = {2,  3,  5,  7,  11, 13, 17, 19, 23, 29, 31, 37, 41,
                          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
    vector<bool> isPrime(100);
    for (auto prime : primes) {
      isPrime[prime] = true;
    }

    int first, last;
    // faster to split into two for loops
    for (int i = 0; i < (int)nums.size(); i++) {
      if (isPrime[nums[i]]) {
        first = i;
        break;
      }
    }

    for (int i = (int)nums.size() - 1; i >= 0; i--) {
      if (isPrime[nums[i]]) {
        last = i;
        break;
      }
    }

    return last - first;
  }
};

int main() {

  auto s = Solution();
  vector<int> nums;

  nums = {4, 2, 9, 5, 3};
  assert(s.maximumPrimeDifference(nums) == 3);
}
