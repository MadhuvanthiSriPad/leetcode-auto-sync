class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring=[]
        longestSubstr , res = 0 , ''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if(len(s[i:j+1])>len(res)):
                        longestSubstr = max(longestSubstr,len(s[i:j+1]))
                        res=s[i:j+1]
        return res
    