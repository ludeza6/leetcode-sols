# Last updated: 8/6/2026, 7:29:55 PM
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        
        for battery in batteryPercentages:
            if battery - tested > 0:
                tested += 1
        return tested