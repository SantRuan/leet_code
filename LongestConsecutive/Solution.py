from typing import List


class Solution():
    def __init__(self):
        pass

    def longest_consecutive(self, nums: List[int]):
        number_set = set(nums)
        longest = 0

        for number in nums:
            if (number - 1) not in number_set:
                length = 0
                while number + length in number_set:
                    length += 1
                longest = max(length, longest)
        return longest


Solution().longest_consecutive([1, 2, 3, 4, 7, 6, 200, 201])
