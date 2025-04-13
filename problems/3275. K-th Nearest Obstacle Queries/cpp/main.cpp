#include <bits/stdc++.h>
using namespace std;

#define sz(s) (int)s.size()

class Solution {
  public:
    vector<int> resultsArray(vector<vector<int>> &queries, int k) {
        priority_queue<int> heap;
        vector<int> out;

        for (int i = 0; i < sz(queries); i++) {
            auto f = queries[i][0], s = queries[i][1];
            heap.push(abs(f) + abs(s));
            if ((int)heap.size() < k) {
                out.push_back(-1);
				continue;
            }

            if ((int)heap.size() > k) 
                heap.pop();

            out.push_back(heap.top());
        }

        return out;
    }
};

int main() {
    auto s = Solution();
    vector<vector<int>> queries;
    vector<int> out;

    queries = {{1, 2}, {3, 4}, {2, 3}, {-3, 0}};
    out = {-1, 7, 5, 3};
    assert(s.resultsArray(queries, 2) == out);
}
