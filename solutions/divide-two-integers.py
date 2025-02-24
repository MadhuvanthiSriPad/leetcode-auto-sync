class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q=0
        while( dividend - divisor >=0):
            q+=1
            dividend-=divisor
        return q
        