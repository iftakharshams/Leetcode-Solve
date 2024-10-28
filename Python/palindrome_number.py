class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Numbers that end in 0 (but are not 0) are not palindromes
        if x != 0 and x % 10 == 0:
            return False

        # Reversing half of the integer
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # x equals reversed_half for even-length numbers
        # x equals reversed_half // 10 for odd-length numbers
        return x == reversed_half or x == reversed_half // 10
