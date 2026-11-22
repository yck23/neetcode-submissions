# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        
        res.append(pairs.copy())
        if not pairs:
            return []
        for j in range(1, len(pairs)):
            i=j
            while i>0:
                if pairs[i].key<pairs[i-1].key:
                    pairs[i], pairs[i-1] = pairs[i-1], pairs[i]
                    i-=1
                else:
                    break
            res.append(pairs.copy())
        return res

