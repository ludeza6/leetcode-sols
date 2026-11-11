# Last updated: 11/11/2026, 9:48:39 AM
1class Solution:
2    def prefixCount(self, words: list[str], pref: str) -> int:
3
4        count = 0
5
6        for word in words:
7            if pref == word[0 : len(pref)]:
8                count += 1
9        return count