from threading import Semaphore


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sema = Semaphore(1)
        self.even_sema = Semaphore(0)
        self.odd_sema = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_sema.acquire()
            printNumber(0)
            if i % 2:
                self.odd_sema.release()
            else:
                self.even_sema.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2==0:
                self.even_sema.acquire()
                printNumber(i)
                self.zero_sema.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2:
                self.odd_sema.acquire()
                printNumber(i)
                self.zero_sema.release()
