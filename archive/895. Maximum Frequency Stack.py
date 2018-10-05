import heapq
import collections
class FreqStack:

    def __init__(self):
        self.key_freq=collections.defaultdict(int)
        self.freq_keys=[]


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.key_freq[x]+=1
        freq=self.key_freq[x]
        if freq>len(self.freq_keys):
            self.freq_keys.append([])
        self.freq_keys[freq-1].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x=self.freq_keys[-1].pop()
        if len(self.freq_keys[-1])==0:
            self.freq_keys.pop()
        self.key_freq[x]-=1
        return x




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()