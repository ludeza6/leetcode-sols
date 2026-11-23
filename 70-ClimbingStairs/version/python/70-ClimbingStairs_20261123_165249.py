# Last updated: 11/23/2026, 4:52:49 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        
4        if n <= 2:
5            return n
6        
7        prev2, prev1 = 1, 2
8
9        for _ in range(3, n + 1):
10            curr = prev1 + prev2
11            prev2, prev1 = prev1, curr
12        return prev1