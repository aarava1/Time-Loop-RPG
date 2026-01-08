class TimeLoopMemory:
    def __init__(self):
        self.flags = set()

    def remember(self, key):
        self.flags.add(key)

    def knows(self, key):
        return key in self.flags
