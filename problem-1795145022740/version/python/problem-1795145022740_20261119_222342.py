# Last updated: 11/19/2026, 10:23:42 PM
1class Solution:
2    def buildArray(self, target: list[int], n: int) -> list[str]:
3        if not target:
4            return []
5        
6        ops = []
7        seen = []
8
9        for i in range(1, n + 1):
10            if seen == target:
11                break
12            if i in target:
13                ops.append("Push")
14                seen.append(i)
15            if i not in target:
16                if i not in seen:
17                    seen.append(i)
18                    ops.append("Push")
19                    ops.append("Pop")
20                    seen.remove(i)
21        return ops