class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        length=0
        i=0
        while length<K:
            ch=S[i]
            if ch.isdigit():
                length*=int(ch)
            else:
                length+=1
            i+=1
        while:
            ch=S[i]
            if ch.isdigit():
                size//=int(ch)
                k%=size
            else:
                if K==N or K==0:
                    return ch
                size-=1

