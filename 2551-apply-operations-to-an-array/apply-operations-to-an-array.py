class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                nums[i],nums[i+1] = nums[i]*2,nums[i]*0
        for nums in nums:
            if nums != 0:
                result.append(nums)
        while len(result)<n:
            result.append(0)
        return result

        