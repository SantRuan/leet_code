

class Solution(object):
    def romanToInt(s: str):
        """
        :type s: str
        :rtype: int
        """

        roman_dic = {
            'I':  1,
            'IV': 4,
            'V':  5,
            'IX': 9,
            'X':  10,
            'XL': 40,
            'L':  50,
            'XC': 90,
            'C':  100,
            'CD': 400,
            'D':  500,
            'CM': 900,
            'M':  1000,
        }
        number = 0
        for roman, integer in roman_dic.items():
            while s.endswith(roman):
                s = s.removesuffix(roman)
                number += integer
        return number


Solution.romanToInt(s="MCMXCIV")
