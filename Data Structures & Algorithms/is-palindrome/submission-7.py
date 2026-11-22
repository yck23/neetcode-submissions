class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()

        l = len(s)
        i = 0
        j= l-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True