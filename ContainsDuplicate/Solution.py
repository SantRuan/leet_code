from typing import List


class Solution:
    def containsDuplicate(nums: List[int]) -> bool:

        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False


Solution.containsDuplicate(nums=[1, 2, 3, 4])
