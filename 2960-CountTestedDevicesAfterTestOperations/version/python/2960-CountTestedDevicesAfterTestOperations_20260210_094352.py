# Last updated: 2/10/2026, 9:43:52 AM
1class Solution:
2    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
3        tested = 0
4        
5        for battery in batteryPercentages:
6            if battery - tested > 0:
7                tested += 1
8        return tested