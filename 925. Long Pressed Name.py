class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        def solve(s):
            arr = []
            p1 = 0
            cur_char = None
            cur_len = 1
            while p1 < len(s):
                if s[p1] != cur_char:
                    if cur_char is not None:
                        arr.append((cur_char, cur_len))
                    cur_char = s[p1]
                    cur_len = 1
                else:
                    cur_len += 1
                p1 += 1
            return arr

        arr_name = solve(name)
        arr_typed = solve(typed)
        # print(arr_name)
        # print(arr_typed)
        if len(arr_name) != len(arr_typed):
            return False
        else:
            for i in range(len(arr_name)):
                if arr_name[i][0] != arr_typed[i][0] or arr_name[i][1] > arr_typed[i][1]:
                    return False
        return True



