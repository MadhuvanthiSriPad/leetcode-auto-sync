class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s) - 2):  # Sliding window of size 3
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:  # All distinct
                count += 1
        
        return count