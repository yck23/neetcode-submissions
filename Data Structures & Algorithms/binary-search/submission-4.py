class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        if len(nums)<3:
            i=0
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
            return -1
        while left<right-1:
            mid = (left+right)//2
            num = nums[mid]
            if num ==target:
                return mid
            elif num<target:
                left = mid
            else:
                right = mid
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        return -1