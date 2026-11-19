# Last updated: 11/19/2026, 12:40:22 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        
4        stack = []
5
6        pairs = {
7            ")": "(",
8            "}": "{",
9            "]": "["
10        }
11
12        for char in s:
13
14            if char == "(" or char == "{" or char == "[":
15                stack.append(char)
16
17            else:
18                if not stack or pairs[char] != stack[-1]:
19                    return False
20                
21                stack.pop()
22
23        if not stack:
24            return True
25        else:
26            return False