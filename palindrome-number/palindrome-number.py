class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        r = 0

        while x > 0:
            r *= 10
            r += x % 10
            x //= 10
        if self.x == r:
            return True
        else:
            return False