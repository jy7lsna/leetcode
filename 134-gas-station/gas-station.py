class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        
        return start if total_tank >= 0 else -1