class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for a in nums:
            if a in x:
                return True
            x.add(a)
            
        return False
        