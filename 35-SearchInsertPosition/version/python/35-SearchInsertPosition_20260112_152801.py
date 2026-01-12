# Last updated: 1/12/2026, 3:28:01 PM
1class Solution(object):
2    def mySqrt(self, x):
3        """
4        :type x: int
5        :rtype: int
6        """
7        result = 1
8        while result * result <= x:
9            result += 1
10        return result - 1