class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        alpha=[]
        digit=[]
        for log in logs:
            identifier=log[:log.index(" ")]
            rest=log[log.index(" ")+1:]
            if rest[0].isdigit():
                digit.append(log)
            else:
                alpha.append((rest,identifier))
        alpha.sort()
        alpha=[x[1]+" "+x[0] for x in alpha]
        return alpha+digit



