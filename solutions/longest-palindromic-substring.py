class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for j in s:
            resStr,res,cnt='',0,0
            for i in range(n-1):
                if(i!=0 and i!=n-1 and s[i-1]==s[i+1]):
                    resStr+=(s[i-1])+s[i]+s[i+1]
                    cnt+=len(resStr)
            res = max(res , cnt)
        return resStr

        