class RandomizedSet:

    def __init__(self) -> None:
        import random
        self.rand = random
        self.data = []
        self.value2index = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val) -> bool:
        if val in self.value2index:
            return False
        self.data.append(val)
        self.value2index[val] = len(self.data) - 1

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val) -> bool:
        if val not in self.data:
            return False
        dead_val_index = self.value2index[val]
        self.data[dead_val_index] = self.data[-1]
        self.value2index[self.data[-1]] = dead_val_index
        self.value2index.pop(val)
        self.data.pop()

    """
    @return: Get a random element from the set
    """

    def getRandom(self) -> int:
        return self.data[self.rand.randint(0, len(self.data) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
