class Solution:
    def largestVariance(self, s: str) -> int:
        d = {}
        for i, ch in enumerate(s):
            d.setdefault(ch, [])
            d[ch].append(i)

        def foo(arr1, arr2):
            arr = []
            p1 = p2 = 0
            while p1 < len(arr1) or p2 < len(arr2):
                a1 = arr1[p1] if p1 < len(arr1) else float("inf")
                a2 = arr2[p2] if p2 < len(arr2) else float("inf")
                if a1 < a2:
                    arr.append(1)
                    p1 += 1
                else:
                    arr.append(-1)
                    p2 += 1
            print(arr1, arr2, arr)
            diff1 = diff2 = None
            max_diff = 0
            min_diff = 0
            seen1 = seen2 = False
            for x in arr:
                if x == 1:
                    seen1 = True
                else:
                    seen2 = True
                if diff1 == None:
                    diff1 = x
                else:
                    diff1 = max(diff1 + x, x)
                if diff2 == None:
                    diff2 = x
                else:
                    diff2 = min(diff2 + x, x)
                if seen1 and seen2:
                    max_diff = max(max_diff, diff1)
                    min_diff = min(min_diff, diff2)
            # print()
            return max(abs(max_diff), abs(min_diff))

        ans = 0
        for ch1 in d:
            for ch2 in d:
                if ch1 != ch2:
                    ans = max(ans, foo(d[ch1], d[ch2]))
        return ans


print(Solution().largestVariance("abced"))
