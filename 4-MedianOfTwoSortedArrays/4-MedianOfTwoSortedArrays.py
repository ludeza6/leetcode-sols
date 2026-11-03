# Last updated: 11/3/2026, 10:21:32 AM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarr = nums1 + nums2
        newarr.sort()

        if len(newarr) % 2 != 0:
            return float(newarr[len(newarr) // 2])
        else:
            return (newarr[len(newarr) // 2 - 1] + newarr[len(newarr) // 2]) / 2.0