class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diff = dict()
        for i in range(0,n):
            diff[target - nums[i]] = i
        
        for i in range(0,n):
            if nums[i] in diff:
                if i!= diff[nums[i]]:
                    return [i, diff[nums[i]]]
                