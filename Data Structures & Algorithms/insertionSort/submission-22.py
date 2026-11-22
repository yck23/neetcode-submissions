# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for j in range(0, len(pairs)):
            i=0
            while i<j:
                if pairs[j].key>=pairs[i].key:
                    i+=1
                else:
                    break
            pairs.insert(i, pairs[j])
            pairs.pop(j+1)
            res.append(pairs.copy())
        return res

