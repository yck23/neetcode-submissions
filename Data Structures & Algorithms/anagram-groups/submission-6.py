class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in mydict:
                mydict[key]=[s]
            else:
                mydict[key].append(s)
        return list(mydict.values())

        