#include <bits/stdc++.h>
using namespace std;

#define sz(s) (int)s.size()

class Solution {
  private:
    bool list(vector<vector<int>> &trips, int capacity) {
        vector<int> delta(1001, 0);

        for (int i = 0; i < sz(trips); i++) {
            auto amt = trips[i][0], start = trips[i][1], end = trips[i][2];
            delta[start] += amt;
            delta[end] -= amt;
        }

        int curr = 0;
        for (auto d : delta) {
            curr += d;

            if (curr > capacity)
                return false;
        }

        return true;
    }
    bool queue(vector<vector<int>> &trips, int capacity) {
        auto cmp = [&](vector<int> a, vector<int> b) { return a[1] < b[1]; };
        sort(trips.begin(), trips.end(), cmp);

        auto pq_cmp = [&](pair<int, int> a, pair<int, int> b) {
            return a.first > b.first;
        };

        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(pq_cmp)>
            out(pq_cmp);

        int ps = 0;

        for (int i = 0; i < sz(trips); i++) {
            auto amt = trips[i][0], start = trips[i][1], end = trips[i][2];

            while (out.size() && out.top().first <= start) {
                ps -= out.top().second;
                out.pop();
            }

            ps += amt;
            out.push(pair(end, amt));

            if (ps > capacity)
                return false;
        }

        return true;
    }

  public:
    bool carPooling(vector<vector<int>> &trips, int capacity) {
        // return queue(trips, capacity);
        return list(trips, capacity);
    }
};

int main() {
    auto s = Solution();
    vector<vector<int>> trips;

    trips = {{2, 1, 5}, {3, 3, 7}};
    assert(s.carPooling(trips, 4) == false);

    trips = {{2, 1, 5}, {3, 3, 7}};
    assert(s.carPooling(trips, 5) == true);

    trips = {{3, 2, 7}, {3, 7, 9}, {8, 3, 9}};
    assert(s.carPooling(trips, 11) == true);
}
