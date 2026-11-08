# Last updated: 11/8/2026, 12:08:22 PM
1class Solution:
2    def reverseDegree(self, s: str) -> int:
3        letters = {
4            'a': 26,
5            'b':25,
6            'c':24,
7            'd':23,
8            'e':22,
9            'f':21,
10            'g':20,
11            'h':19,
12            'i':18,
13            'j':17,
14            'k':16,
15            'l':15,
16            'm':14,
17            'n':13,
18            'o':12,
19            'p':11,
20            'q':10,
21            'r':9,
22            's':8,
23            't':7,
24            'u':6,
25            'v':5,
26            'w':4,
27            'x':3,
28            'y':2,
29            'z':1
30        }
31
32        newlist = list(s)
33        sum = 0
34
35        for i in range(len(newlist)):
36            sum += letters[newlist[i]] * (i + 1)
37        
38        return sum