class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1=sentence1.split(" ")
        sentence2=sentence2.split(" ")
        if len(sentence1)<len(sentence2):
            sentence1,sentence2=sentence2,sentence1
        p1=p2=0
        insert=0

        while p1<len(sentence1):
            if p2<len(sentence2) and sentence1[p1]==sentence2[p2]:
                if insert==1:
                    insert=2
                p1+=1
                p2+=1
            else:
                if insert==0:
                    insert=1
                elif insert==2:
                    return False
                p1+=1

        return p1==len(sentence1) and p2==len(sentence2)

print(Solution().areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))