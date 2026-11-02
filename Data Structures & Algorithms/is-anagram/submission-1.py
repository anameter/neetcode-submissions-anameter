class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_s = {}
        freq_t = {}
        for x in s:
            freq_s[x] = freq_s.get(x,0) + 1
        for x in t:
            freq_t[x] = freq_t.get(x,0) + 1

        print(freq_s)
        print(freq_t)

        if freq_s != freq_t:
            return False
        return True