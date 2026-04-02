class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        e = dict()
        for x in s:
            if x not in d:
                d[x] = 0
            d[x] = d[x] +1
        
        for x in t:
            if x not in e:
                e[x] = 0
            e[x] = e[x] +1

        if (d!=e):
            return False
        return True

