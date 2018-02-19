# coding=utf-8
'''
Created on 2017å¹?11æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """

        def nextPoint(px, py):
            if len(source[px]) <= py + 1:
                return px + 1, 0
            else:
                return px, py + 1

        def jump(px, py):  # source[px][py]=="*" and source[px][py]=="/
            newPx, newPy = nextPoint(px, py)
            newPx, newPy = nextPoint(newPx, newPy)
            while not (newPy != 0 and source[newPx][newPy] == "/" and source[newPx][newPy - 1] == "*"):
                newPx, newPy = nextPoint(newPx, newPy)
            return nextPoint(newPx, newPy)

        ans = []
        curLine = []
        px, py = 0, 0
        while px < len(source):
            if source[px][py] == "*" and curLine and curLine[-1] == "/":
                curLine.pop()
                px, py = jump(px, py)
                if py == 0 and curLine:
                    ans.append("".join(curLine))
                    curLine = []
                # jump to end block
            elif source[px][py] == "/" and curLine and curLine[-1] == "/":
                curLine.pop()
                if curLine: ans.append("".join(curLine))
                curLine = []
                px, py = px + 1, 0
            else:
                curLine.append(source[px][py])
                newPx, newPy = nextPoint(px, py)
                if newPx > px:
                    if curLine: ans.append("".join(curLine))
                    curLine = []
                px, py = newPx, newPy
        return ans


source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
# source = ["a/*comment", "line", "more_comment*/b"]
source = ["/*Test program */",
          "int main()",
          "{ ",
          "  // variable declaration ",
          "int a, b, c;",
          "/* This is a test",
          "   multiline  ",
          "   comment for ",
          "   testing */",
          "a = b + c;",
          "}"]
source = ["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]
print Solution().removeComments(source)
