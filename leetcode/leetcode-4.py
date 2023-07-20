'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if
n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(0,len(flowerbed)):
            if i == 0 and i == len(flowerbed) - 1:
                if flowerbed[i] == 0:
                    count += 1
                    break
                else:
                    break
            if i == 0:
                if flowerbed[i] == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
                else:
                    continue
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        count += 1
                else:
                    break
            else:
                if flowerbed[i] == 0:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                    else:
                        continue
                else:
                    continue
        if count < n:
            return False
        else:
            return True
        
#OPTIMIZED CODE

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
        if count >= n:
            return True
        else:
            return False




        
            