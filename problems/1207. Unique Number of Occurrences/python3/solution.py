from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = dict()

        for num in arr:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

        uniq = dict()

        for k, v in seen.items():
            if v not in uniq:
                return False
            else:
                uniq[v] = [k]

        return True


if __name__ == "__main__":
    s = Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3])
    print(s)
    assert s == True

    s = Solution().uniqueOccurrences([1, 2])
    print(s)
    assert s == False
