# Last updated: 9/2/2026, 2:30:49 PM
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        row x has x slots.
        - n == 1: 1 
        - n == 2: 1
        - n == 3: 2
        - n == 4: 2
        - n == 5: 2
        - n == 6: 3
        - n == 7: 3
        - n == 8: 3
        - n == 9: 3
        - n == 10: 4
        - 
        - 
        - 
        - 
        """
        return int((-1 + math.sqrt(1 + 8 * n)) // 2)
        