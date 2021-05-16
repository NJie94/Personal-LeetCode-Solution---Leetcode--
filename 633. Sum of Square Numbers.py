
'''

'''
import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(math.sqrt(c))+1):
            b = int(math.sqrt(c-a*a))
            if a*a + b*b == c:
                return True
        return False