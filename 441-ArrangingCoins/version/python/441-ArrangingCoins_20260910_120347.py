# Last updated: 9/10/2026, 12:03:47 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        newarr = nums1 + nums2
4        newarr.sort()
5
6        if len(newarr) % 2 != 0:
7            return float(newarr[len(newarr) // 2])
8        else:
9            return (newarr[len(newarr) // 2 - 1] + newarr[len(newarr) // 2]) / 2.0