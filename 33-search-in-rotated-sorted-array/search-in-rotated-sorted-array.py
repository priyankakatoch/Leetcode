class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(0,n):
            if nums[i] == target:
                return i
        return -1
        