from typing import List


class Solution():
    def __init__(self):
        pass

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        for number, c in count.items():
            freq[c].append(number)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result


if __name__ == "__main__":
    Solution().topKFrequent(nums=[1, 1, 1, 3, 3, 2], k=2)
