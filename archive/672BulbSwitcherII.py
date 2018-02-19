class Solution(object):

    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        status_set = set()
        status_set.add(tuple())
        for _ in xrange(m):
            new_status_set = set()
            for status in status_set:
                for x in xrange(1, 5):
                    status_copy = list(status)
                    if x in status_copy:
                        status_copy.remove(x)
                    else:
                        status_copy.append(x)
                    new_status_set.add(tuple(status_copy))
            status_set = new_status_set

        ans = set()
        for status in status_set:
            init = [True] * n
            for x in status:
                if x == 1:
                    init = [not init[i] for i in xrange(n)]
                if x == 2:
                    init = [not init[i] if i % 2 == 1 else init[i] for i in xrange(n)]
                if x == 3:
                    init = [not init[i] if i % 2 == 0 else init[i] for i in xrange(n)]
                if x == 4:
                    init = [not init[i] if i % 3 == 0 else init[i] for i in xrange(n)]
            ans.add(tuple(init))
#         print status_set
#         print len(status_set)
#         print ans
        return len(ans)


n = 1000
m = 1000
print Solution().flipLights(n, m)

