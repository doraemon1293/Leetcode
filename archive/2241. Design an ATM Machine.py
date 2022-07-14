class ATM:

    def __init__(self):
        self.denom = [20, 50, 100, 200, 500]
        self.notes = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, c in enumerate(banknotesCount):
            self.notes[i] += c
        return None

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(4, -1, -1):
            if amount >= self.denom[i] and self.notes[i] > 0:
                x = min(amount // self.denom[i], self.notes[i])
                amount -= x * self.denom[i]
                self.notes[i] -= x
                res[i] = x
        if amount == 0:
            return res
        else:
            for i in range(5):
                self.notes[i] += res[i]
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
