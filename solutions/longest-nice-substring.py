class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""
        
        charSet = set(s)

        for i , ch in enumerate(s):
            if(ch.swapcase() not in charSet):
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                return max(left,right,key=len)
        return s