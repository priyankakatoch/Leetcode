class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range (0,n):
            if nums[i] == target:
                return True
        return False
        