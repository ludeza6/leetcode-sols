# Last updated: 11/22/2026, 7:46:46 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        
4        best = ""
5        
6        def expand(left, right):
7
8            while left >= 0 and right < len(s) and s[left] == s[right]:
9                left -= 1
10                right += 1
11
12            return s[left + 1: right]
13
14        for i in range(len(s)):
15            odd = expand(i, i)
16            even = expand(i, i + 1)
17
18            if len(odd) > len(best):
19                best = odd
20            if len(even) > len(best):
21                best = even
22
23        return best
24        
25        return s