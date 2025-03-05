class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            x_list = ['-'] + [int(digit) for digit in str(abs(x))]
        else:
            x_list = [int(digit) for digit in str(x)]

        if(x_list[:] == x_list[::-1]):
            return True
        return False