# Last updated: 11/3/2026, 10:18:51 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        longest = 0
4
5        ptr1, ptr2 = 0, 1
6
7        while ptr2 <= len(s):
8            window_length = len(s[ptr1 : ptr2])
9            set_length = len(set(s[ptr1 : ptr2]))
10
11            if window_length == set_length:
12                longest = len(s[ptr1 : ptr2])
13            else:
14                ptr1 += 1
15            ptr2 += 1
16            
17        return longest