class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        for x1 in range(1,len(S)//2+1):
            for x2 in range(x1+1,len(S)-1):
                if S[0]=="0" and len(S[:x1])>1 and int(S[:x1])<=2**31-1:
                    break
                else:
                    n1 = int(S[:x1])
                if S[x1]=="0" and len(S[x1:x2])>1 and int(S[x1:x2])<=2**31-1:
                    break
                else:
                    n2=int(S[x1:x2])
                ans=[n1,n2]
                tempS=S[x2:]
                while tempS:
                    n3=n1+n2
                    l=len(str(n3))
                    if n3<=2**31-1 and int(tempS[:l])==n3:
                        if tempS[0]=="0" and len(tempS[:l]) > 1:
                            break
                        else:
                            tempS=tempS[l:]
                            n1=n2
                            n2=n3
                            ans.append(n3)
                    else:
                        break
                if tempS=="":
                    return ans
        return []

S="11235813"
S="1101111"
S="0123"
S="539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
print(Solution().splitIntoFibonacci(S))