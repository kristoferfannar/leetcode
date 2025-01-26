#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int busyStudent(vector<int> &startTime, vector<int> &endTime, int queryTime) {
    int count = 0;

    for (int i = 0; i < (int)startTime.size(); i++)
      if (startTime[i] <= queryTime && endTime[i] >= queryTime)
        count++;

    return count;
  }
};

int main() {
  auto s = Solution();

  vector<int> start{1, 2, 3}, end{3, 2, 7};
  assert(s.busyStudent(start, end, 4) == 1);
}
