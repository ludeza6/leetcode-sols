# Last updated: 8/6/2026, 7:49:37 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        nums1[m:] = nums2
7        nums1.sort()