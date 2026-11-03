# Last updated: 11/3/2026, 10:20:19 AM
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        
        for battery in batteryPercentages:
            if battery - tested > 0:
                tested += 1
        return tested