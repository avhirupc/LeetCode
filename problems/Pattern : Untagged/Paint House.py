"""Wrong Answer"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs)==0:
            return 0
        colorcost=min(costs[0])
        prevcolor=costs[0].index(colorcost)
        for itr in range(1, len(costs)):
            currcost=min(costs[itr])
            currcolor=costs[itr].index(currcost)
            if currcolor!=prevcolor:
                colorcost+=currcost
                prevcolor=currcolor
                continue
            
            prevcost=costs[itr-1][prevcolor]
            colorcost-=prevcost
            prevcosts_min_prevcolor=min([(color,val) for color,val in enumerate(costs[itr-1]) if color!=prevcolor],key=lambda x:x[1])
            currcosts_min_currcolor=min([(color,val) for color,val in enumerate(costs[itr]) if color!=prevcolor],key=lambda x:x[1])
            if prevcost+currcosts_min_currcolor[1]<currcost+prevcosts_min_prevcolor[1]:
                colorcost+=(prevcost+currcosts_min_currcolor[1])
                prevcolor=currcosts_min_currcolor[0]
            else:
                colorcost+=(currcost+prevcosts_min_prevcolor[1])
                prevcolor=currcolor
            
        return colorcost
        