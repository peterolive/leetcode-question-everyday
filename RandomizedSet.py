class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomized_set = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.randomized_set:
            return False
        self.randomized_set[val] = val
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.randomized_set:
            self.randomized_set.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return self.randomized_set[random.choice(list(self.randomized_set.keys()))]
