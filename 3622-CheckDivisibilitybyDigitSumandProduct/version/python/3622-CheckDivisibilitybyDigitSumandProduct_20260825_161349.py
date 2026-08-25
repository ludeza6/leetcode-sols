# Last updated: 8/25/2026, 4:13:49 PM
1import math
2
3class Solution:
4    def checkDivisibility(self, n: int) -> bool:
5        digits = list(str(n))
6        int_digits = [int(x) for x in digits]
7        digitSUM = sum(int_digits)
8        digitsPROD = math.prod(int_digits)
9
10        return (n % (digitSUM + digitsPROD) == 0)