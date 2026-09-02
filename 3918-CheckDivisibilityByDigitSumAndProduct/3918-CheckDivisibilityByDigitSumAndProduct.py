# Last updated: 9/2/2026, 2:30:44 PM
import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(str(n))
        int_digits = [int(x) for x in digits]
        digitSUM = sum(int_digits)
        digitsPROD = math.prod(int_digits)

        return (n % (digitSUM + digitsPROD) == 0)