# Last updated: 1/20/2026, 2:09:07 PM
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        word_list = s.split()
8
9        while " " in word_list:
10            word_list.remove(" ")
11        return len(word_list[len(word_list) - 1])
12