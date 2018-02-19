# coding=utf-8
'''
Created on 2017å¹?7æœ?16æ—?

@author: Administrator
'''


def cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.sentences_ind = {}
        self.sentences = sorted([[sentences[i], times[i]] for i in xrange(len(sentences))], cmp = cmp)
        for i, sentences in enumerate(self.sentences):
            self.sentences_ind[sentences[0]] = i
        self.inputting = ""
        self.currentMatchSentences = [x[0] for x in self.sentences]

    def search(self, inputting):
        self.currentMatchSentences = [s[1:] for s in self.currentMatchSentences if s and s[0] == inputting]
        return [self.inputting + s for s in self.currentMatchSentences[:3]]

    def addSentence(self, sentence):
        if sentence in self.sentences_ind:
            ind = self.sentences_ind[sentence]
            self.sentences[ind][1] += 1
        else:
            ind = len(self.sentences)
            self.sentences.append([sentence, 1])
        while ind > 0 and cmp(self.sentences[ind], self.sentences[ind - 1]) == -1:
            self.sentences_ind[self.sentences[ind - 1][0]] += 1
            self.sentences[ind - 1], self.sentences[ind] = self.sentences[ind], self.sentences[ind - 1]
            ind -= 1
        self.sentences_ind[self.sentences[ind][0]] = ind

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != "#":
            self.inputting += c
            return self.search(c)
        else:
            self.addSentence(self.inputting)
            self.inputting = ""
            self.currentMatchSentences = [x[0] for x in self.sentences]
            return []

# [[["abc", "abbc", "a"], [3, 3, 3]], ["b"], ["c"], ["#"], ["b"], ["c"], ["#"], ["a"], ["b"], ["c"], ["#"], ["a"], ["b"], ["c"], ["#"]]
# # Your AutocompleteSystem object will be instantiated and called as such:
# sentences = ["abc", "abbc", "a"]
# times = [3, 3, 3]
# obj = AutocompleteSystem(sentences, times)
# print obj.input("b")
# print obj.input("c")
# print obj.input("#")
# # print obj.sentences
# # print obj.sentences_ind
# print obj.input("b")
# print obj.input("c")
# print obj.input("#")
# # print obj.sentences
# # print obj.sentences_ind
# print obj.input("a")
# print obj.input("b")
# print obj.input("c")
# print obj.input("#")
# # print obj.sentences
# # print obj.sentences_ind
# print obj.input("a")
# print obj.input("b")
# print obj.input("c")
# print obj.input("#")


["AutocompleteSystem", "input", "input", "input", "input", "input", "input", "input", "input", "input", "input", "input", "input"]
sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]
obj = AutocompleteSystem(sentences, times)
for c in [["i"], [" "], ["a"], ["#"], ["i"], [" "], ["a"], ["#"], ["i"], [" "], ["a"], ["#"]]:
    print obj.input(c[0])
    if c[0] == "#":
        print obj.sentences
