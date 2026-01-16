# Last updated: 1/15/2026, 10:55:33 PM
1class Solution(object):
2    def plusOne(self, digits):
3        """
4        :type digits: List[int]
5        :rtype: List[int]
6        """
7        num = int(''.join(map(str, digits))) + 1
8        return [int(d) for d in str(num)]