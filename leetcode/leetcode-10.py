'''

longest palindromic substring

Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''
#Python3 code

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def check_string(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        ans_s = ''

        for i in range(n):
            pal_even = check_string(i,i)
            if len(pal_even) > len(ans_s):
                ans_s = pal_even

            pal_odd = check_string(i,i+1)
            if len(pal_odd) > len(ans_s):
                ans_s = pal_odd

        return ans_s