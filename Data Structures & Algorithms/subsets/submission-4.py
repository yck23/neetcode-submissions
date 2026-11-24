class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arrlist = []
        lennum = len(nums)
        for i in range(2**lennum):
            arr = []
            for j in range(lennum):
                if i & 2**j:
                    arr.append(nums[j])
            arrlist.append(arr)
        return arrlist

        