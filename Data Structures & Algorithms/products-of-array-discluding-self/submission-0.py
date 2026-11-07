class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        

        l = len(nums)
        output = l * [1]

        left_prod=1
        right_prod=1
        for i in range(l):
            output[i] = left_prod
            left_prod = left_prod * nums[i]

        for i in range(l-1,-1,-1):
            output[i] = output[i] * right_prod
            right_prod = right_prod * nums[i]

        return output

            

        