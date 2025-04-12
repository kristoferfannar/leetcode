#include <bits/stdc++.h>
#include <queue>
using namespace std;

class Solution {
  public:
    int minimumCost(int m, int n, vector<int> &horizontalCut,
                    vector<int> &verticalCut) {

        priority_queue<int> ph, pv;
        int hsum = 0, vsum = 0;

        for (auto i : horizontalCut) {
            ph.push(i);
            hsum += i;
        }
        for (auto i : verticalCut) {
            pv.push(i);
            vsum += i;
        }

        int out = 0;
        while (!ph.empty() && !pv.empty()) {
            if (ph.top() > pv.top()) {
                out += ph.top() + vsum;
                hsum -= ph.top();
                ph.pop();
            } else {
                out += pv.top() + hsum;
                vsum -= pv.top();
                pv.pop();
            }
        }

        return out + vsum + hsum;
    }
};

int main() {
    auto s = Solution();
    vector<int> hCut, vCut;

    hCut = {1, 3}, vCut = {5};
    assert(s.minimumCost(3, 2, hCut, vCut) == 13);

    hCut = {7}, vCut = {4};
    assert(s.minimumCost(2, 2, hCut, vCut) == 15);

    hCut = {2, 3, 2, 3, 1}, vCut = {1, 2};
    assert(s.minimumCost(6, 3, hCut, vCut) == 28);
}
