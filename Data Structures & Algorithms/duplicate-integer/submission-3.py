class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        thisset = set()
        for num in nums:
            if num in thisset:
                return True
            else:
                thisset.add(num)
        return False