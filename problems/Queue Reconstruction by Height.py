from functools import cmp_to_key
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def compare(person1,person2):
            if person1[0]==person2[0]:
                return person1[1]- person2[1]
            return person2[0] - person1[0]
        people=sorted(people, key=cmp_to_key(compare))
        res=[]
        for person in people:
            res.insert(person[1],person)
        return res
        