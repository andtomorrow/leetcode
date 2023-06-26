class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            x_rev_str = x_str[::-1]
            if x_str == x_rev_str:
                return True

        
