# Last updated: 9/2/2026, 2:44:18 PM
1class Solution:
2    def fib(self, n: int) -> int:
3        if n == 0:
4            return 0
5        if n == 1:
6            return 1
7        return self.fib(n - 1) + self.fib(n - 2)