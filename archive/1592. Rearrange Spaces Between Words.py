import re


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        words = [w for w in re.split(r" +", text) if w]
        if len(words)==1:
            return words[0]+" "*spaces
        # print(words)
        return (" " * (spaces // (len(words) - 1))).join(words) + " " * (spaces % (len(words) - 1))

