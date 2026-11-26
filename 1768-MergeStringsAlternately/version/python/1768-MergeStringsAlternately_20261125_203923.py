# Last updated: 11/25/2026, 8:39:23 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3
4        newstr = ""
5        j = 0
6
7        for i in range(min(len(word1), len(word2))):
8            newstr += f"{word1[i]}{word2[i]}"
9            j += 1
10            
11        if len(word1) > len(word2):
12            chars_to_add = word1[j :]
13            newstr += f"{chars_to_add}"
14        
15        
16        if len(word1) < len(word2):
17            chars_to_add = word2[j :]
18            newstr += f"{chars_to_add}"
19        
20        return newstr