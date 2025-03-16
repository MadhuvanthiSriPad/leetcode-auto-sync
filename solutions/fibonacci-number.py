class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 1
        one,two = 0,1
        for i in range(2,n+1):
            one,two = two , one+two
        return two 