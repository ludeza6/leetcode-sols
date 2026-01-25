# Last updated: 1/25/2026, 10:50:52 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        nums1[m:] = nums2
7        nums1.sort()