class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # check if left and right plots are empty
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
                
                # if both are empty, we can plan a flower here
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
        return True if n <= 0 else False