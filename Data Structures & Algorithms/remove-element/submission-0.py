class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        l = 0

        for x in nums:
            if x == val:
                k=k-1
                l=l+1

        for i in range(l):
            nums.remove(val)


        return k