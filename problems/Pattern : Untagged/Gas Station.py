class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumCost,sumGas,total=0,0,0
        start=0
        for itr in range(0,len(gas)):
            sumCost += cost[itr]
            sumGas += gas[itr]
            total += (gas[itr]- cost[itr])
            if total<0:
                total =0
                start = itr +1
        
        if sumGas - sumCost <0:
            return -1
        return start