# coding=utf-8
'''
Created on 2017�?10�?8�?

@author: Administrator
'''

import collections


class Solution(object):

    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
#         from collections import Counter, defaultdict
#         import math
#         temp = set(target)
#         ch_count = defaultdict(list)
#         arr = []
#         for sticker in stickers:  # 不加小集�?
#             new_count = Counter([ch for ch in sticker if ch in temp])
#             flag = True if len(new_count) != 0 else False
#             for count in arr:
#                 if count & new_count == new_count:
#                     flag = False
#                     break
#                 elif count & new_count == count:
#                     arr.remove(count)
#             if flag:
#                 arr.append(new_count)
#         for count in arr:
#             for ch in count:
#                 ch_count[ch].append(count)
#         for ch in target:
#             if len(ch_count[ch]) == 0:
#                 return -1
#         target = Counter(target)
#
#         def unique(ch_count):
#             for ch in ch_count:
#                 if len(ch_count[ch]) == 1:
#                     return ch
#             return ""
#
#
#
#         def dfs(target):
#             if len(target) == 0:
#                 return 0
#             unique_ch = unique(ch_count)
#             times = 0
#             while unique_ch:
#                 count = ch_count[unique_ch][0]
#                 temp = int(math.ceil(float(target[unique_ch]) / count[unique_ch]))
#                 times += temp
#                 for ch in count:
#                     if ch in target:
#                         target[ch] -= temp * count[ch]
#                         if target[ch] <= 0:
#                             del target[ch]
#                             del ch_count[ch]
#                 unique_ch = unique(ch_count)
#             if len(target) == 0:
#                 return times
#             ch = target.keys()[0]
#             res = min([dfs(target - count) + 1 for count in ch_count[ch]] + [float("inf")])
#             return res + times
#         res = dfs(target)
#         return res if res != float("inf") else -1

        # 利用位运�? TLE
#         N = 1 << len(target)
#         dp = [float("inf")] * N
#         dp[0] = 0
#         def bfs(target):
#         for status in xrange(N):
#             if dp[status] != -1:
#                 for s in stickers:
#                     now = status
#                     for ch in s:
#                         for j in range(len(target)):
#                             if target[j] == ch and (not now >> j & 1):
#                                 now |= 1 << j
#                                 break
#                     dp[now] = min(dp[now], dp[status] + 1)
#         return dp[N - 1] if dp[N-1]!=float("inf") else -1
        temp = [0] * 26
        for ch in target:
            temp[ord(ch) - ord("a")] += 1
        # chars 记录字符在target转化为tuple后的位置
        chars = dict([(char, ind) for ind, char in enumerate(sorted(set(target)))])
        # 把target转化成tuple
        char_set = set(target)
        target = tuple(filter(lambda x:x != 0, temp))

        temps = set()
        for sticker in stickers:
            deleting_sticker = []
            temp = [0] * len(target)
            flag1 = False
            flag2 = True
            for ch in sticker:  # 如果sticker中不含target中的字符
                if ch in chars:
                    flag1 = True
                    temp[chars[ch]] += 1
                    char_set.discard(ch)
            if flag1:
                temp = tuple(temp)
                for x in temps:
                    if all([x[i] >= temp[i] for i in range(len(target))]):  # 如果sticker是temps中某�?个元素的子集 则不加入
                        flag2 = False
                        break
                    if all([x[i] <= temp[i] for i in range(len(target))]):  # 如果stickers中某�?个元素是temp的子�? 则删�?
                        deleting_sticker.append(tuple(x))
            if flag1 and flag2:
                temps.add(tuple(temp))

            for x in deleting_sticker:
                temps.remove(x)
        if len(char_set) > 0: return -1
        stickers = temps
        ind_sticker = {}
        for sticker in stickers:
            for i in range(len(sticker)):
                if sticker[i] > 0:
                    ind_sticker.setdefault(i, [])
                    ind_sticker[i].append(sticker)
        # print target
        # print ind_sticker
        q = collections.deque()
        q.append((target, 0, 0))
        while q:
            t0, st, times = q.popleft()
            # print "t0", t0, st
            for sticker in ind_sticker[st]:
                new_st = st
                new_t0 = [0] * st + [max(0, t0[i] - sticker[i]) for i in range(st, len(target))]
                while new_st < len(target) and new_t0[new_st] == 0:
                    new_st += 1
                # print "new", new_t0, sticker, new_st
                if new_st == len(target):
                    return times + 1
                q.append((new_t0, new_st, times + 1))


stickers = ["with", "example", "science"]
target = "thehat"
stickers = ["fly", "me", "charge", "mind", "bottom"]
target = "centorder"

stickers = ["these", "guess", "about", "garden", "him"]
target = "aehmort"
stickers = ["this", "island", "keep", "spring", "problem", "subject"]
target = "aegopprrs"
print Solution().minStickers(stickers, target)
