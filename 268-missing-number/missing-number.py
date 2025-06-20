class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =  len(nums)
        dic = {}
        for i in range (0,n+1):
            dic[i]= 0
        for num in nums:
            dic[num] = 1
        for k,v in dic.items():
            if v == 0:
                return k 

        