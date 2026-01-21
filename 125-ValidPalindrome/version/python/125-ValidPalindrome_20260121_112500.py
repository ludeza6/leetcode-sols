# Last updated: 1/21/2026, 11:25:00 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        filtered_chars = [char.lower() for char in s if char.isalnum()]
4        return filtered_chars == filtered_chars[::-1]