class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        p = nums[0]
        for i in range (1,n-1):
            if nums[i] == nums[i+1]:
                continue
            if (p>nums[i]<nums[i+1]) or (p<nums[i]>nums[i+1]):
                count+=1 
            p=nums[i]
        return count
