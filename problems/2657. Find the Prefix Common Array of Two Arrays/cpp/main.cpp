#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> findThePrefixCommonArray(vector<int> &A, vector<int> &B) {
    set<int> a, b, total;
    int n = (int)A.size();
    vector<int> out(n);

    out[0] = A[0] == B[0];
    a.insert(A[0]);
    b.insert(B[0]);

    for (int i = 1; i < n; i++) {
      out[i] = out[i - 1];

      if (A[i] == B[i] && b.find(B[i]) == b.end() && a.find(A[i]) == a.end())
        out[i]++;

      if (a.find(A[i]) == a.end() && b.find(A[i]) != b.end())
        out[i]++;

      if (b.find(B[i]) == b.end() && a.find(B[i]) != a.end())
        out[i]++;

      a.insert(A[i]);
      b.insert(B[i]);
    }
    return out;
  }
};

int main() {
  auto s = Solution();
  vector<int> A, B, exp;

  A = {1, 3, 2, 4}, B = {3, 1, 2, 4};
  exp = {0, 2, 3, 4};
  assert(s.findThePrefixCommonArray(A, B) == exp);

  A = {2, 3, 1}, B = {3, 1, 2};
  exp = {0, 1, 3};
  assert(s.findThePrefixCommonArray(A, B) == exp);
}
