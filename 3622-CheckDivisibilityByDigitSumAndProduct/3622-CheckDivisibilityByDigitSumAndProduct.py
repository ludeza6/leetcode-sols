# Last updated: 11/3/2026, 10:20:22 AM
import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(str(n))
        int_digits = [int(x) for x in digits]
        digitSUM = sum(int_digits)
        digitsPROD = math.prod(int_digits)

        return (n % (digitSUM + digitsPROD) == 0)