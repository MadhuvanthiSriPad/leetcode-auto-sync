class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        sum = [0] * (n + 1)  
        sum[0], sum[1], sum[2] = 0, 1, 1

        for i in range(3, n + 1):
            sum[i] = sum[i - 1] + sum[i - 2] + sum[i - 3]

        return sum[n]