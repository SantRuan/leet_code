from typing import List


class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:

        if len(strs) == 0:
            return ""
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                # A ordem da condicional afeta
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base


Solution.longestCommonPrefix(strs=["acabei", "acabou", "acabamos"])
