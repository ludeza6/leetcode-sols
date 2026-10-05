# Last updated: 10/5/2026, 10:47:42 AM
1class Solution:
2    def longestCommonPrefix(self, strs: list[str]) -> str:
3        if len(strs) == 1:
4            return strs[0]
5        
6        if not strs:
7            return ""
8
9        strs.sort()
10        first, last = strs[0], strs[-1]
11        result = []
12
13        for i in range(min(len(first), len(last))):
14            if first[i] != last[i]:
15                break
16            result.append(first[i])
17        return "".join(result)