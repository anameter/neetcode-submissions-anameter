class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minstr = min(strs)
        slen = len(minstr)
        ans = ""

        for i in range(slen):
            for x in strs:
                if x[i] != minstr[i]:
                    return ans
                
            ans = ans + x[i]
        
        return ans
            
                    
            