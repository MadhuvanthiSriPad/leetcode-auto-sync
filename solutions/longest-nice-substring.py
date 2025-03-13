class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""

        char_set = set(s)
        
        for i, ch in enumerate(s):
            if ch.swapcase() not in char_set:  # If ch's counterpart is missing
                left = self.longestNiceSubstring(s[:i])  # Left part
                right = self.longestNiceSubstring(s[i+1:])  # Right part
                return max(left, right, key=len)

        return s 