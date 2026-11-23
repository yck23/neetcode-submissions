class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=1
        uniqlen = 1
        myset = set()
        # s = list(s)
        # print(s)
        if len(s)==0:
            return 0
        myset.add(s[0])
        while r<len(s):
            if s[r] in myset:
                myset.remove(s[l])
                # print(myset)
                l+=1
            else:
                myset.add(s[r])
                uniqlen = max(uniqlen, r-l+1)
                r+=1
        return uniqlen

        