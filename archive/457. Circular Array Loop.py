class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def set_zero(i):
            cur_pos = i
            while 1:
                next_pos = (cur_pos + nums[cur_pos]) % N
                if nums[next_pos] * nums[i] > 0:
                    nums[i] = 0
                    cur_pos = new_pos
                else:
                    break

        N = len(nums)
        for i in range(N):
            if nums[i] != 0:
                cnt, cur_pos = 0, i
                while cnt < N:
                    new_pos = (cur_pos + nums[cur_pos]) % N
                    new_num = nums[new_pos]
                    if new_pos == cur_pos or new_num * nums[i] < 0:
                        set_zero(i)
                        break
                    else:
                        cur_pos = new_pos
                        cnt += 1
                if cnt == N:
                    return True
        return False



