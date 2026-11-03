# Last updated: 11/3/2026, 10:21:35 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        ptr1, ptr2 = 0, 1

        while ptr2 <= len(s):
            window_length = len(s[ptr1 : ptr2])
            set_length = len(set(s[ptr1 : ptr2]))

            if window_length == set_length:
                longest = len(s[ptr1 : ptr2])
            else:
                ptr1 += 1
            ptr2 += 1
            
        return longest