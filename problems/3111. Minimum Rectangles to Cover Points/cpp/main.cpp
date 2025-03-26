#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minRectanglesToCoverPoints(vector<vector<int>>& points, int w) {
		vector<int> x;
		for (auto p : points) {
			x.push_back(p[0]);
		}

		sort(x.begin(), x.end());

		int rect = 0;
		int last = INT_MIN;

		for (int i = 0; i < x.size(); i++) {
			if (x[i] > last + w) {
				rect++;
				last = x[i]; 
			}
		}

		return rect;
    }
};

int main() { 

	auto s = Solution();
	vector<vector<int>> points;

	points = {{2,1},{1,0},{1,4},{1,8},{3,5},{4,6}};
	assert(s.minRectanglesToCoverPoints(points, 1) == 2);

	points = {{0,0},{1,1},{2,2},{3,3},{4,4},{5,5},{6,6}};
	assert(s.minRectanglesToCoverPoints(points, 2) == 3);

	points = {{2, 1}, {1, 3}};
	assert(s.minRectanglesToCoverPoints(points, 1) == 1);
}
