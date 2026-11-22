class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sdict = {}

        for slet in s:
            if slet in sdict:
                sdict[slet]+=1
            else:
                sdict[slet]=1
        for tlet in t:
            if tlet in sdict:
                sdict[tlet]-=1
                if sdict[tlet]==0:                    
                    sdict.pop(tlet)
            else:
                return False
        if sdict:
            return False
        else:
            return True