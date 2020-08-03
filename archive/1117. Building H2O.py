from collections import deque

class H2O:
    def __init__(self):
        self.hq=deque()
        self.oq=deque()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.hq.append(releaseHydrogen)
        self.merge()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.oq.append(releaseOxygen)
        self.merge()

    def merge(self):
        if len(self.hq)>=2 and len(self.oq)>=1:
            self.hq.pop()()
            self.hq.pop()()
            self.oq.pop()()
