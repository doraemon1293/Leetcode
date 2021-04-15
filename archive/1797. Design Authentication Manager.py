class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens={}
        self.timeToLive=timeToLive
        self.renewed_time=[]

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId]+self.timeToLive>currentTime:
            self.tokens[tokenId]=currentTime


    def countUnexpiredTokens(self, currentTime: int) -> int:
        return len([token for token in self.tokens if self.tokens[token]+self.timeToLive>currentTime])


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)