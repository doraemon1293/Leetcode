


import collections
class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.kv=dict([(k,v) for k,v in zip(keys,values)])
        self.dictionary=set(dictionary)
        self.decrypt_counter=collections.Counter([self.encrypt(s) for s in dictionary])

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        return "".join([self.kv[c] for c in word1])



    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        return self.decrypt_counter[word2]



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)