class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        nums.sort()
        for i in range(0,n):
            if a in nums:
                a=a+1
                continue
        return a


        