from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        print(f"nums: {nums}")

        smallest = float("inf")
        second_smallest = float("inf")

        for num in nums:
            # smallest number we've seen so far
            if num <= smallest:
                smallest = num
            # second smallest number we've seen so far
            elif num <= second_smallest:
                second_smallest = num

            else:  # third smallest number we've seen so far

                print(f"num: {num}")
                return True

        return False


if __name__ == "__main__":
    s = Solution().increasingTriplet([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(s)
    assert s == True

    s = Solution().increasingTriplet([5, 4, 3, 2, 1])
    print(s)
    assert s == False

    s = Solution().increasingTriplet([2, 1, 5, 0, 4, 6])
    print(s)
    assert s == True

    # not only checks that i < min(j, k), but also checks that j < k
    s = Solution().increasingTriplet([0, 4, 2, 1, 0, -1, -3])
    print(s)
    assert s == False

    s = Solution().increasingTriplet([1, 5, 0, 4, 1, 3])
    print(s)
    assert s == True
