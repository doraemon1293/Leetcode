# coding=utf-8
'''
Created on 2017å¹?4æœ?27æ—?

@author: Administrator
'''


class Codec(object):
    ch_to_int = [(x, str(x)) for x in range(10)] + [(x,)]

    def __init__(self):
        self.current_code = ["0"]
        self.code_to_url = {}

    def current_code_plus_1(self):
        plus = 1
        i = 0
        while plus:
            if "0" <= self.current_code[i] < "9" or "A" <= self.current_code[i] < "Z" or "a" <= self.current_code[i] < "z":
                self.current_code[i] = chr(ord(self.current_code[i]) + 1)
                plus = 0
            elif self.current_code[i] == "9":
                self.current_code[i] = "A"
                plus = 0
            elif self.current_code[i] == "Z":
                self.current_code[i] = "a"
                plus = 0
            elif self.current_code[i] == "z":
                self.current_code[i] = "-"
                plus = 0
            elif self.current_code[i] == "-":
                self.current_code[i] = "="
                plus = 0
            elif self.current_code[i] == "=":
                self.current_code[i] = "0"
                i += 1
                if i == len(self.current_code):
                    self.current_code.append("1")
                    plus = 0
        # 0-9:0-9 "A-Z":10-35 "a-z":36-61 "-":62 "=":63

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        code = "".join(self.current_code)
        self.code_to_url[code] = longUrl
        self.current_code_plus_1()
        return code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code_to_url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
