# Last updated: 8/6/2026, 7:30:08 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split()
        whitespace = " "
        while whitespace in word_list:
            word_list.remove(whitespace)
        return len(word_list[len(word_list) - 1])
