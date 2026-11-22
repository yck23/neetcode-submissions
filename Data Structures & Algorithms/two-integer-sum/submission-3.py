class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for idx in range(len(nums)):
            num = nums[idx]
            if (target-num) in numdict:
                output = sorted([idx, numdict[target-num]])
                return output
            if num not in numdict:
                numdict[num] = idx