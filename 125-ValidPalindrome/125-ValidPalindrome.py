# Last updated: 8/6/2026, 7:29:51 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        return filtered_chars == filtered_chars[::-1]