class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cumcosts = [0]*(len(cost)+1)
        cumcosts[0] = cost[0]
        cumcosts[1] = cost[1]
        cost.extend([0])

        for i in range(2, len(cost)):
            cumcosts[i] = min(cumcosts[i-1], cumcosts[i-2])+cost[i]
            print(cumcosts)
        return cumcosts[-1]
        