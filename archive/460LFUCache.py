from collections import OrderedDict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key_value = {}  # store key->value
        self.key_freq = {}  # store key->used times
        self.freq_list = {}  # store used->time ->ordered set
        self.min_freq = 0  # minimum used time
        self.capacity = capacity
        self.number = 0

    def freq_plus_1(self, key):
        freq = self.key_freq[key]
        self.key_freq[key] += 1
        del self.freq_list[freq][key]
        self.freq_list.setdefault(freq + 1, OrderedDict())
        self.freq_list[freq + 1][key] = None
        if self.min_freq == freq and self.freq_list[freq].keys() == []:
            self.min_freq += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity == 0: return -1
        if key in self.key_value:
            value = self.key_value[key]
            self.freq_plus_1(key)
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0: return
        if key in self.key_value:
            self.freq_plus_1(key)
            self.key_value[key] = value
        if key not in self.key_value:
            if self.number == self.capacity:
                remove_key = self.freq_list[self.min_freq].keys()[0]
                self.delete(remove_key)
            self.key_freq[key] = 0
            self.freq_list.setdefault(0, OrderedDict())
            self.freq_list[0][key] = None
            self.key_value[key] = value
            self.min_freq = 0
            self.number += 1

    def delete(self, key):
        del self.key_value[key]
        freq = self.key_freq.pop(key)
        del self.freq_list[freq][key]
        self.number -= 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
