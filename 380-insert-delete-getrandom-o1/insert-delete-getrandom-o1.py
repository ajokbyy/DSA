import random

class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.pos = {}   # val -> index

    def insert(self, val):
        if val in self.pos:
            return False
        
        self.arr.append(val)
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        if val not in self.pos:
            return False
        
        idx = self.pos[val]
        last_val = self.arr[-1]

        # swap with last element
        self.arr[idx] = last_val
        self.pos[last_val] = idx

        # remove last
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()