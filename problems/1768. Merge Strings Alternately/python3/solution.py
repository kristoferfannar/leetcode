class Solution:
     def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        smaller = min(len(word1), len(word2))

        for idx in range(smaller):
            merged += word1[idx] + word2[idx]

        if len(word1) == smaller:
            merged += word2[smaller:]
        else:
            merged += word1[smaller:]

        return merged


    def mergeAlternately2(self, word1: str, word2: str) -> str:
        """Use a initialized list instead of creating strings on the fly"""
        merged = [""] * min(len(word1), len(word2)) * 2

        smaller = min(len(word1), len(word2))

        for idx in range(smaller):
            merged[2 * idx] = word1[idx]
            merged[2 * idx + 1] = word2[idx]

        if len(word1) == smaller:
            return "".join(merged) + word2[smaller:]
        else:
            return "".join(merged) + word1[smaller:]


if __name__ == "__main__":
    word1, word2 = "hello", "world"
    merged = Solution().mergeAlternately(word1, word2)

    assert merged == "hweolrllod"
