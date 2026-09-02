# Last updated: 9/2/2026, 2:08:29 PM
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        
4        answer = []
5
6        for i in range(1, n + 1):
7
8            if i % 3 == 0 and i % 5 == 0:
9                answer += ["FizzBuzz"]
10            elif i % 3 == 0:
11                answer += ["Fizz"]
12            elif i % 5 == 0:
13                answer += ["Buzz"]
14            else:
15                answer += [f"{i}"]
16
17        return answer