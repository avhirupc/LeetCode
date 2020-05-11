class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor=image[sr][sc]
        length,width=len(image),len(image[0])
        is_traversed=[[False for col in range(width)]for row in range(length)]
        self.floodFillUtil(image, sr, sc, newColor,oldColor,is_traversed)
        return image
        
    def floodFillUtil(self,image, sr, sc, newColor,oldColor,is_traversed):
        length,width=len(image),len(image[0])
        if not(0<=sr<length):
            return 
        if not(0<=sc<width):
            return 
        if image[sr][sc]!=oldColor or is_traversed[sr][sc]:
            return 
        image[sr][sc]=newColor
        is_traversed[sr][sc]=True
        self.floodFillUtil(image, sr-1, sc, newColor,oldColor,is_traversed)# row above
        self.floodFillUtil(image, sr+1, sc, newColor,oldColor,is_traversed)# row below
        self.floodFillUtil(image, sr, sc-1, newColor,oldColor,is_traversed)# right
        self.floodFillUtil(image, sr, sc+1, newColor,oldColor,is_traversed)# left
        
        