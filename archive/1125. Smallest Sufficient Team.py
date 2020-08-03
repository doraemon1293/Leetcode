class Solution:
    def smallestSufficientTeam(self, req_skills: list, people: list) -> list:
        d = {}
        for i, skill in enumerate(req_skills):
            d[skill] = 1 << i
        dp = {}
        dp[0] = (0, [])
        for i, person in enumerate(people):
            if person:
                temp = sum([d[skill] for skill in person])
                new_dp = dict((k, v) for k, v in dp.items())
                for k in sorted(dp.keys()):
                    new_k = k | temp
                    if new_k not in new_dp or dp[k][0] + 1 < new_dp[new_k][0]:
                        new_dp[new_k] = (dp[k][0] + 1, dp[k][1] + [i])
                dp = new_dp
        return dp[2 ** len(req_skills) - 1][1]


# req_skills=["a","b","c","d","e","f","g","h"]
# people=[["b"],["a","c","e","f"],["g"],["h"],["c","d"]]
req_skills = ["gvp", "jgpzzicdvgxlfix", "kqcrfwerywbwi", "jzukdzrfgvdbrunw", "k"]
people = [["jgpzzicdvgxlfix"], ["jgpzzicdvgxlfix", "k"], ["jgpzzicdvgxlfix", "kqcrfwerywbwi"], ["gvp"], ["jzukdzrfgvdbrunw"], ["gvp", "kqcrfwerywbwi"]]
print(Solution().smallestSufficientTeam(req_skills, people))
