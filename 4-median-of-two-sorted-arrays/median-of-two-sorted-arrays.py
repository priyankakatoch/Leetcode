class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1[:] = nums1+nums2
        nums1.sort()
        print (nums1)
        n= len(nums1)
        if n%2==0:
            med1 =nums1[n//2]
            med2 =nums1[n//2-1]
            med = (med1+med2)/2
            return med
        else:
            med = nums1[n//2]
            return med

        