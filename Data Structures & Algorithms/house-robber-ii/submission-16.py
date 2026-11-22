class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<4:
            return max(nums)
        totnums = nums[:]
        totnums[2]=nums[0]+nums[2]
        totnums[1]=0
        for i in range(3, len(totnums)-1):
            totnums[i]=nums[i]+max(totnums[i-2], totnums[i-3])
        bestnum = max(totnums[-3], totnums[-2])
        print(nums, totnums)
        nums.append(nums[0])
        nums.pop(0)
        totnums = nums[:]
        totnums[2]=nums[0]+nums[2]
        totnums[1]=0
        for i in range(3, len(totnums)-1):
            totnums[i]=nums[i]+max(totnums[i-2], totnums[i-3])
        bestnum = max(bestnum,totnums[-3], totnums[-2])
        print(nums, totnums)
        nums.append(nums[0])
        nums.pop(0)
        totnums = nums[:]
        totnums[2]=nums[0]+nums[2]
        totnums[1]=0
        for i in range(3, len(totnums)-1):
            totnums[i]=nums[i]+max(totnums[i-2], totnums[i-3])
        bestnum = max(bestnum,totnums[-2], totnums[-3])
        print(nums, totnums)
        return bestnum