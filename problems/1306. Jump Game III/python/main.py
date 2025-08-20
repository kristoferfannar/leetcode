from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        idxs = [start]
        visited = [False] * len(arr)
        visited[start] = True

        while idxs:
            idx = idxs.pop(0)
            val = arr[idx]
            if val == 0:
                return True

            l = idx - val
            r = idx + val

            if l >= 0 and not visited[l]:
                visited[l] = True
                idxs.append(l)
            if r < len(arr) and not visited[r]:
                visited[r] = True
                idxs.append(r)

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.canReach([4, 2, 3, 0, 3, 1, 2], 5) == True
    assert s.canReach([4, 2, 3, 0, 3, 1, 2], 0) == True
