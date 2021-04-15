# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.6
    d = {}
    ans=-1
    for i in range(len(S) - 1):
        diagram = S[i] + S[i + 1]
        if diagram not in d:
            d[diagram]=i
        else:
            ans=max(ans,i-d[diagram])
    return ans

print(solution("aakmaakmakda"))