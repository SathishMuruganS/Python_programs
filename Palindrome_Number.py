'''

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = x
            result = 0
            while y > 0:
                result *= 10
                result += y%10
                y //= 10
            return result == x
