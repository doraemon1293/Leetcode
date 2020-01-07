from threading import Semaphore

class Foo:
    def __init__(self):
        self.first_sema=Semaphore(1)
        self.second_sema = Semaphore(0)
        self.third_sema=Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        self.first_sema.acquire()
        printFirst()
        self.second_sema.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.second_sema.acquire()
        printSecond()
        self.third_sema.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.third_sema.acquire()
        printThird()
        self.first_sema.acquire()
