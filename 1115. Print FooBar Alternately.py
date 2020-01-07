from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sema=Semaphore(1)
        self.bar_sema=Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foo_sema.acquire()
            printFoo()
            self.foo_sema.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.bar_sema.acquire()
            printBar()
            self.bar_sema.release()
