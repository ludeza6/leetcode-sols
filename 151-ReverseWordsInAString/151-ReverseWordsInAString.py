# Last updated: 8/24/2026, 9:51:47 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() # now a list of the words
        reversed_words = words[::-1]
        return " ".join(reversed_words)

