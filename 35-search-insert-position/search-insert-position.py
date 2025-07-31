class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        x=n
        while left<=right:
            m = (left+right)//2
            if nums[m] >= target:
                x = m
                right = m-1
            else:
                left = m+1
        return x

        