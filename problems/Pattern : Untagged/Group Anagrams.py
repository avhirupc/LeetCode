from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping=defaultdict(list)
        memory=set([])
        for str in strs:
            sstr="".join(sorted(str))
            if sstr in memory:
                mapping[sstr].append(str)
            else:
                memory.add(sstr)
                mapping[sstr].append(str)
        return list(mapping.values())
        class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr=sorted(arr)
        count=0
        itr=0
        while(itr<len(arr)):
            no=arr[itr]
            j=itr+1
            while(j <len(arr) and arr[j]==no):
                j+=1
            while(j <len(arr) and arr[j]==no+1):
                count+=1
                break
            itr+=1
        return count