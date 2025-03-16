class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0]*(n+1)
        if n==0:
            return 0
        if(n==1):
            return 1

        
        dp[1],dp[2]=1,2
        print(dp)

        for i in range(3,n+1):
            dp[i]= dp[i-1]+dp[i-2]
        return dp[n]