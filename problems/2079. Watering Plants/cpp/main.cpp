#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
		int steps = 0, cap = capacity;

		for (int i = 0; i < plants.size(); i++) {

			if (cap< plants[i]) {
				steps += (i ) * 2;
				cap= capacity;
			}
			cap -= plants[i];
			steps++;
		}

		return steps;
    }
};

int main() {
	auto s = Solution();
	vector<int> plants;

	plants = {2, 2, 3, 3};
	assert(s.wateringPlants(plants,5) == 14);

	plants = {1,1,1,4,2,3};
	assert(s.wateringPlants(plants,4) == 30);

	plants = {7,7,7,7,7,7,7};
	assert(s.wateringPlants(plants, 8) == 49);
}
