# Last updated: 9/2/2026, 2:30:25 PM
1import math
2
3class Solution:
4    def arrangeCoins(self, n: int) -> int:
5        """
6        row x has x slots.
7        - n == 1: 1 
8        - n == 2: 1
9        - n == 3: 2
10        - n == 4: 2
11        - n == 5: 2
12        - n == 6: 3
13        - n == 7: 3
14        - n == 8: 3
15        - n == 9: 3
16        - n == 10: 4
17        - 
18        - 
19        - 
20        - 
21        """
22        return int((-1 + math.sqrt(1 + 8 * n)) // 2)
23        