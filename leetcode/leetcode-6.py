'''

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"
 


'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        left = 0
        right = len(word) - 1
        vowels = 'AEIOUaeiou'
        while left < right:
            if word[left] in vowels and word[right] in vowels:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            elif word[left] not in vowels:
                left += 1
            elif word[right] not in vowels:
                right -= 1
        return ''.join(word)
        
'''
the given word is made into a list called word. two variables left and right is taken. the vowels both upper case and lower case
is given together as one string variable. in the while loop till left is not >= right, 
we check if the letter at the given index is a vowel or not by checking if it is present in the string vowels.
if both are present, we swap them. 
if left is not present we increment left. if right letter is not present the string vowels, we decrement right.
at last after the loop, the word will be of the form, 
for example =>

word = ["h", "o", "l", "l", "e"]

to omit the " sign and join the word to get the final string, we use join function.
where '' is the string seperator. 

'''