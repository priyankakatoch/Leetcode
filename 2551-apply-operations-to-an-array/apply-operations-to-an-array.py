class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                nums[i],nums[i+1] = nums[i]*2,nums[i]*0
        r0=[]
        for i in nums:
            if i!=0:
                result.append(i)
            else:
                r0.append(i)
        print(result,r0)
        return result+r0

        