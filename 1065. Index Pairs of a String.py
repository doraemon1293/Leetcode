class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans=[]
        for word in words:
            for i in range(len(text)):
                if text[i:i+len(word)]==word:
                    ans.append([i,i+len(word)-1])
        ans.sort()
        return ans