class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.values = []
        self.idxs = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.values.append(val)
        self.idxs[val].add(len(self.values) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.idxs[val]:
            out = self.idxs[val].pop()
            ins = self.values[-1]
            self.values[out] = ins
            self.idxs[ins].add(out)
            self.idxs[ins].discard(len(self.values) - 1)
            self.values.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        import random
        return self.values[random.randint(0, len(self.values)-1)]
