class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while True:
            added = numbers[i]+numbers[j]
            if added == target:
                return [i+1, j+1]
            if added > target:
                j-=1
            else:
                i+=1
        