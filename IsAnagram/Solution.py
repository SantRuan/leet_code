def isAnagram(s: str, t: str) -> bool:

    s_freq = {}
    t_freq = {}

    for letter in s:
        s_freq[letter] = s_freq.get(letter, 0) + 1

    for letter in t:
        t_freq[letter] = t_freq.get(letter, 0) + 1
    return s_freq == t_freq


isAnagram(s="aacc", t="ccac")
