class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.filled=set([])
        self.total=n_rows*n_cols
        self.q=n_cols

    def flip(self) -> List[int]:
        num=random.randint(0,self.total-1)
        while(num in self.filled):
            num=random.randint(0,self.total-1)
        self.filled.add(num)
        q=num//self.q
        r=num%self.q
        return [q,r]

    def reset(self) -> None:
        self.filled=set([])


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()