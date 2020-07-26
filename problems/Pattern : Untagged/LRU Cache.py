from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.mem=deque([])
        self.k_v_store={}

    def get(self, key: int) -> int:
        if key in self.k_v_store:
            self.mem.remove(key)
            self.mem.append(key)
            return self.k_v_store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.mem and len(self.mem)==self.capacity:
            lru_key=self.mem.popleft()
            del self.k_v_store[lru_key]
        if key in self.mem:
            self.mem.remove(key)
        self.mem.append(key)
        self.k_v_store[key]=value
        return
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)