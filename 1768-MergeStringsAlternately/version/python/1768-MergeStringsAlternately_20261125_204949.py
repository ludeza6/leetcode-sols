# Last updated: 11/25/2026, 8:49:49 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        merged = []
4        n = min(len(word1), len(word2))
5
6        for i in range(n):
7            merged.append(word1[i])
8            merged.append(word2[i])
9
10        if len(word1) > n:
11            merged.append(word1[n:])
12        elif len(word2) > n:
13            merged.append(word2[n:])
14
15        return "".join(merged)