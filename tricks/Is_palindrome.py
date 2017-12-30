
def isPalindrome(self, x):
        """
        判断是否为回文数
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return str(x)[::-1] == str(x)
