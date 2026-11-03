# Last updated: 11/3/2026, 10:21:30 AM
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]
        result = []

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result.append(first[i])
        return "".join(result)