class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = sorted(nums1 + nums2)
        n = len(array)

        if n % 2 == 0:
            mid1 = array[n // 2 - 1]
            mid2 = array[n // 2]
            return (mid1 + mid2) / 2.0
        else:
            return array[n // 2]