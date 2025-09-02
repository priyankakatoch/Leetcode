class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        for nums in count:
            if count[nums]==1:
                return nums 
            