# Last updated: 11/3/2026, 10:20:39 AM
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        if not target:
            return []
        
        ops = []
        seen = []

        for i in range(1, n + 1):
            if seen == target:
                break
            if i in target:
                ops.append("Push")
                seen.append(i)
            if i not in target:
                if i not in seen:
                    seen.append(i)
                    ops.append("Push")
                    ops.append("Pop")
                    seen.remove(i)
        return ops