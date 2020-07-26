"""Wrong Solution"""
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs=[abs(ord(x)-ord(y)) for x,y in zip(s,t)]
        itr,curr_cost,candidates,st,en=0,0,[],-1,-1
        #loop till costs[itr]<maxCosts:
        #st = itr
        flg=0
        while(itr<len(s) and costs[itr]>maxCost):
            itr+=1
        st=itr
        print(costs)
        while(itr<len(s)):
            flg=1
            if curr_cost+costs[itr]<=maxCost:
                curr_cost+=costs[itr]
            else:
                en=itr-1
                candidates.append((st,en))
                curr_cost=0
                while(itr<len(s)-1 and costs[itr]>maxCost):
                    itr+=1
                st=itr
                curr_cost+=costs[itr]
            itr+=1
        en=itr-1
        candidates.append((st,en))
        if flg==0:
            return 0
        print(candidates)
        return max([en-st+1for st,en in candidates])
        
        
                
                
                
"""
whenever rationing, or need to find max subarray kind of , slinding window works great
Sliding window
o(n),o(n)
1208. Get Equal Substrings Within Budget
3. Longest Substring Without Repeating Characters
159. Longest Substring with At Most Two Distinct Characters
340. Longest Substring with At Most K Distinct Characters
992. Subarrays with K Different Integers
424. Longest Repeating Character Replacement
209. Minimum Size Subarray Sum
713. Subarray Product Less Than K
76. Minimum Window Substring
"""
from collections import deque
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(x)-ord(y)) for x,y in zip(s,t)]
        wsum,swindow,mws = 0,deque([]),0
        itr=0
        while(itr<len(s)):
            if wsum+costs[itr]<=maxCost:
                wsum+=costs[itr]
                swindow.append(costs[itr])
            else:
                mws=max(mws,len(swindow))
                while(swindow):
                    fe = swindow.popleft()
                    wsum-=fe
                    if costs[itr]+wsum<=maxCost:
                        break
                if not swindow:
                    wsum=0
                while(itr< len(s) and wsum+costs[itr]>maxCost):
                    itr+=1
                if itr>=len(s):
                    break
                wsum+=costs[itr]
                swindow.append(costs[itr])
            itr+=1
        mws=max(mws,len(swindow))
        
        return mws


def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    n = len(s)
    cost = 0
    left = 0
    max_len = 0
    for right in range(n):
        cost += abs(ord(s[right]) - ord(t[right]))
        while cost > maxCost:
            cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
                    
                    
            
        
        
        
        