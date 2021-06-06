import bisect
import collections
import heapq
class FileSharing:

    def __init__(self, m: int):
        self.chunk_users=collections.defaultdict(set)
        for i in range(1,m+1):
            self.chunk_users[i]=set()
        self.user_chunk=collections.defaultdict(set)
        self.m=m
        self.avai_userid=[]
        self.max_userid=0

    def get_new_userid(self):
        if self.avai_userid:
            return heapq.heappop(self.avai_userid)
        else:
            self.max_userid+=1
            return self.max_userid

    def join(self, ownedChunks: List[int]) -> int:
        userid=self.get_new_userid()

        for x in ownedChunks:
            self.chunk_users[x].add(userid)
        self.user_chunk[userid]=set(ownedChunks)
        return userid

    def leave(self, userID: int) -> None:
        for x in self.user_chunk[userID]:
            self.chunk_users[x].remove(userID)
        del self.user_chunk[userID]
        heapq.heappush(self.avai_userid,userID)


    def request(self, userID: int, chunkID: int) -> List[int]:
        res=sorted(self.chunk_users[chunkID])
        if res:
            self.chunk_users[chunkID].add(userID)
            self.user_chunk[userID].add(chunkID)
        return res