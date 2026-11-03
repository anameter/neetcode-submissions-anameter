class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffSet = dict()
        for i, x in enumerate(nums):
            if (target-x) in diffSet:
                return [diffSet[target-x],i]
            diffSet[x] = i

            
        
