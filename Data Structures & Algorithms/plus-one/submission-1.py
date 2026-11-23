class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(len(digits)):
            number += digits[-1-i]*(10**i)
        return list(str(number+1))
        