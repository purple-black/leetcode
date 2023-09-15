'''

Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 2

'''

#Python3 Code

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        st =''
        if x > 0:
            while x > 0:
                r = x%10
                x = x//10
                st = st + str(r)
            if int(st) >= INT_MIN and int(st) <= INT_MAX:
                return (int(st))
            else:
                return 0

        elif x < 0:
            x = -1 * x
            while x > 0:
                r = x%10
                x = x//10
                st = st + str(r)
            if int(st) >= INT_MIN and int(st) <= INT_MAX:
                return (-1*int(st))
            else:
                return 0
            

        else:
            return (0)
