class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        merged_intervals=[]
        if len(intervals)in [0,1]:
            return intervals
        prev_st,prev_en=intervals[0]
        
        for itr in range(1,len(intervals)):
            curr_st,curr_en=intervals[itr]
            if curr_st>prev_en and prev_en<=curr_en:
                merged_intervals.append([prev_st,prev_en])
                prev_st,prev_en=intervals[itr]
            else:
                prev_en=max(curr_en,prev_en)
                
        merged_intervals.append([prev_st,prev_en])
        
        return merged_intervals
                
            
        