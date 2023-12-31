from typing import List


class Solution:

    def __init__(self) -> None:
        pass

    def daily_temperature(self, temperature: List[str]) -> List[str]:
        res = [0] * len(temperature)
        stack = []
        for i, t in enumerate(temperature):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res
