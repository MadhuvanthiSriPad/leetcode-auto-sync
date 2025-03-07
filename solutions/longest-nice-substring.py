class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest=""
        
        for i in range(len(s)):
            flag = False
            for j in range(i+1,len(s)):
                substr = set(s[i:j+1])

                if all(c.lower() in substr and c.upper() in substr for c in substr):
                    if(len(s[i:j+1])>len(longest)):
                        longest = s[i:j+1]
        return longest
