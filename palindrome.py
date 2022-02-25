class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            x = str(x)
            y = x[::-1]
            return True if x == y else False
        else:
            return False