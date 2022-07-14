class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = [heights[-1]]
        ans = [0]
        for h in heights[::-1][1:]:
            people = 0
            while stack and stack[-1] < h:
                stack.pop()
                people += 1
            if stack:
                people += 1
            stack.append(h)
            ans.append(people)
        return ans[::-1]

