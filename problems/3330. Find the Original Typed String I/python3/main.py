class Solution:
    def possibleStringCount(self, word: str) -> int:

        last = word[0]
        count = 0
        total = 1
        for c in word[1:]:
            if c == last:
                count += 1
            else:
                total += count
                count = 0
            last = c

        total += count

        return total
