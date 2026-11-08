# Last updated: 11/8/2026, 11:58:40 AM
1class Solution:
2    def smallestEvenMultiple(self, n: int) -> int:
3        if n % 2 == 0:
4            return n
5        return n*2