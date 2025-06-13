class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        dis = {}
        for i in range (0,n):
            dis[nums[i]] = 0 
        j = 0
        for k in  dis:
            nums[j] = k 
            j+=1
        return j        