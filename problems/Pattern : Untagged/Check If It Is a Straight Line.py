class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) in [0,1]:
            return True
        p1,p2=coordinates[0],coordinates[1]
        try:
            slope=(p2[1]-p1[1])/(p2[0]-p1[0])
        except:
            slope=float("inf")
        i=2
        while(i < len(coordinates)):
            pt=coordinates[i]
            try: 
                slope_to_test=(pt[1]-p1[1])/(pt[0]-p1[0])
            except:
                slope_to_test=float("inf")
            if slope!=slope_to_test:
                return False
            i+=1
        return True
            
        