# coding=utf-8
'''
Created on 2017å¹?6æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        ind = 0

        def getTagName(ind):
            tagName = []
            while ind < len(code) and code[ind] != ">":
                if "A" <= code[ind] <= "Z" and len(tagName) < 9:
                    tagName.append(code[ind])
                    ind += 1
                else:
                    return False

            if ind == len(code):
                return False
            else:
                tagName = "".join(tagName)
                if len(tagName) > 0:
                    return ind, tagName
                else:
                    return False

        def getCDATA(ind):
            ind += 1
            if code[ind:ind + 7] == "[CDATA[":
                ind += 7
                while ind < len(code) and not (code[ind - 2] == "]" and code[ind - 1] == "]" and code[ind] == ">"):
                    ind += 1
                if ind == len(code):
                    return False
                else:
                    return ind
            else:
                return False

            pass

        tagStack = []
        # getFirstTag
        if ind >= len(code) or code[ind] != "<":
            return False
        else:
            ind += 1
            temp = getTagName(ind)
            if temp:
                ind, tagName = temp
                print tagName
                tagStack.append(tagName)
                ind += 1
            else:
                return False

        while ind < len(code):
            if code[ind] == "<":
                ind += 1
                if ind >= len(code):
                    return False
                # closed tag
                elif code[ind] == "/":
                    ind += 1
                    temp = getTagName(ind)
                    if temp != False:
                        ind, tagName = temp
                    else:
                        return False
                    if tagStack and tagStack[-1] == tagName:
                        tagStack.pop()
                        if tagStack == [] and ind + 1 < len(code):
                            return False
                    else:
                        return False
                # CDATA
                elif code[ind] == "!":
                    ind = getCDATA(ind)
                    if ind == False:
                        return False
                # open Tag
                else:
                    temp = getTagName(ind)
                    if temp != False:
                        ind, tagName = temp
                    else:
                        return False
                    tagStack.append(tagName)
            ind += 1
        if tagStack:
            return False
        else:
            return True


code = "<DIV>Th<IS></IS> the first line <![CDATA[<div>]]></DIV>"
code = "<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"
code = "<A<></A<>"
print Solution().isValid(code)
