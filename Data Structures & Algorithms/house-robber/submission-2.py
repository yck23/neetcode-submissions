class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.extend([0,0])
        totnums = nums[:]
        totnums[2]=nums[2]+nums[0]
        for i in range(3, len(nums)):
            totnums[i]= nums[i]+max(totnums[i-2], totnums[i-3])
        return max(totnums)
        