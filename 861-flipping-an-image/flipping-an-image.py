class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        i = len(image)
        for row in range(i):
            left = 0
            right = i-1
            while left <= right:
                temp = image[row][left] ^ 1
                image[row][left] = image[row][right] ^ 1
                image[row][right] = temp
                left +=1 
                right -=1
        return image
        #time O(n*2)
        # space O(1)