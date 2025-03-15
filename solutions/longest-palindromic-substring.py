class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = s[::-1]  # Reverse the string
        n = len(s)
        
        # Create DP table
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        
        # Fill DP table
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        # Reconstruct the longest palindromic subsequence from the DP table
        i, j = 0, 0
        lps = []
        while i < n and j < n:
            if s[i] == t[j]:
                lps.append(s[i])
                i += 1
                j += 1
            elif dp[i+1][j] >= dp[i][j+1]:
                i += 1
            else:
                j += 1
        
        # Return the subsequence as a string
        return ''.join(lps)