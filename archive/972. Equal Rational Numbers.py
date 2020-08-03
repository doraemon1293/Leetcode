class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        from fractions import Fraction
        def solve(S):
            non_repeat_string = repeat_string = ""
            non_repeat_val = repeat_val = 0
            integer_val = int(S.split(".")[0])
            if "." in S:
                non_repeat_string = S.split(".")[1].split("(")[0]
                if non_repeat_string:
                    non_repeat_val = Fraction(int(non_repeat_string), 10 ** len(non_repeat_string))
            if "(" in S:
                repeat_string = S.split("(")[1][:-1]
                repeat_val = Fraction(int(repeat_string),
                                      (10 ** len(repeat_string) - 1) * (10 ** len(non_repeat_string)))
            return integer_val + non_repeat_val + repeat_val

        return solve(S) == solve(T)
