from typing import List
# 733. Flood Fill
# Array, DFS, BFS, Matrix

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.
# -----------------------------------------------

class Solution:    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # check color at current coords
        prevCol = image[sr][sc]
        if prevCol == color:
            return image
        image[sr][sc] = color

        # update colours in four directions
        if sr > 0 and image[sr - 1][sc] == prevCol:
            image = self.floodFill(image, sr - 1, sc, color)
        if sr + 1 < len(image) and image[sr + 1][sc] == prevCol:
            image = self.floodFill(image, sr + 1, sc, color)
        if sc > 0 and image[sr][sc - 1] == prevCol:
            image = self.floodFill(image, sr, sc - 1, color)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == prevCol:
            image = self.floodFill(image, sr, sc + 1, color)
        # once all directions are checked
        return image
        
# -----------------------------------------------
# Testcases

my_sol = Solution()

images = [[[1,1,1],[1,1,0],[1,0,1]], [[0,0,0],[0,0,0]]]
sr = [1, 0]
sc = [1, 0]
colours = [2, 0]

for i in range (2):
    print(my_sol.floodFill(images[i], sr[i], sc[i], colours[i]))