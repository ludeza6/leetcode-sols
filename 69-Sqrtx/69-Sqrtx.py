# Last updated: 8/6/2026, 7:30:04 PM
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 1
        while result * result <= x:
            result += 1
        return result - 1