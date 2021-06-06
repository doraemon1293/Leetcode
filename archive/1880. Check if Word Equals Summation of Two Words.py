class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def foo(s):
            number = []
            for ch in s:
                number.append(str(ord(ch) - ord("a")))
            return int("".join(number))

        return foo(firstWord) + foo(secondWord) == foo(targetWord)
