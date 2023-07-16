''' PROBLEM STATEMENT

    1768. Merge Strings Alternately
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
    If a string is longer than the other, append the additional letters onto the end of the merged string.

example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r
example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b 
    word2:    p   q   r   s
    merged: a p b q   r   s
example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q 
    merged: a p b q c   d
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        same = False
        word1_size = len(word1)
        word2_size = len(word2)
        if word1_size > word2_size:
            for i in range(word2_size):
                merged += word1[i]
                merged += word2[i]
            for i in range(i+1,word1_size):
                merged += word1[i]

        elif word2_size > word1_size:
            for i in range(word1_size):
                merged += word1[i]
                merged += word2[i]
            for i in range(i+1,word2_size):
                merged += word2[i]
        else:
            same = True
            for i in range(0,word1_size):
                merged += word1[i]
                merged += word2[i]
        return merged
