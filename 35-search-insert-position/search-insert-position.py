class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lef = 0
        rig = n-1
        ub = n
        for i in range(0,n):
            while lef <=rig :
                mid  = (lef+rig)//2
                if nums[mid] >= target:
                    ub =  mid
                    rig = mid-1
                else:
                    lef = mid+1
            return ub
 

                