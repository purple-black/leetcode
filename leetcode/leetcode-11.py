'''

Letter combinations of a phone number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

'''
#Python3 Code

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        a = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []

        def get_combinations(combin, giv_d):
            if not giv_d:
                ans.append(combin)
                return

            for i in a[giv_d[0]]:
                get_combinations(combin + i, giv_d[1:])


        get_combinations("", digits)
        return ans


