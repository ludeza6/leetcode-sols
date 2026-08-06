# Last updated: 8/6/2026, 7:30:20 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        
        if str(x) == (str(x))[::-1]:
            return True
        return False
        