'''
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        len1 = len(str1)
        len2 = len(str2)

        def check(i):
            if len1 % i or len1 % i:
                return False
            r1, r2 = len1//i, len2//i
            return (str1[:i] * r1 == str1 and str1[:i] * r2 == str2)

        for i in range(min(len1, len2), 0, -1):
            if check(i):
                return str1[:i]
        return ""

'''
we find length of both the given strings. then, out of the two see which is min. iterating from the min value, to 0.(decrementing each time) i.e., using the
greedy approach.
if str1 is ABABAB AND str2 is ABAB, first from str2, we take ABAB, then ABA, then AB, and each time i is given to check function which
will check if the length of both the strings is divisible by the length of the sub string.

if any of the case, i.e., either str1 or str2 gives remainder on dividing with the length of substring, then we do not consider that sub string.
this is because, the remainder should be zero in both cases, then only we can say like if we multiply AB 3 times we will get str1 and 2 times to get str2.
then only we can say we can get both the original string as a multiple of substring. 

when we multiply the substring a certain number of times, we should get both the original strings, then only remainder will be zero.

'''