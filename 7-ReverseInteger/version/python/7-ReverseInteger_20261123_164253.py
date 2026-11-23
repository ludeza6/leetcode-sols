# Last updated: 11/23/2026, 4:42:53 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        
4        if str(x)[0] == "-":
5            val = int("-" + str(x)[::-1][:-1])
6        
7        else:
8            val =  int(str(x)[::-1])
9
10        if val < (-1 * 2 ** 31) or val > (2 ** 31 - 1):
11            return 0
12        else:
13            return val