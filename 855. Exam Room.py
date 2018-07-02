import bisect
class ExamRoom:


    def __init__(self, N):
        """
        :type N: int
        """
        self.N=N
        self.seats=[]

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seats)==0:
            self.seats.append(0)
            return 0
        else:
            dis=0
            ret=float("inf")
            if self.seats[0]!=0:
                if self.seats[0]>=dis:
                    dis=self.seats[0]
                    ret=0

            for i in range(len(self.seats)-1):
                temp_dis=(self.seats[i+1]-self.seats[i])//2
                if temp_dis>dis:
                    dis=temp_dis
                    ret=self.seats[i]+dis

            if self.seats[-1] != self.N - 1:
                if self.N - 1 - self.seats[-1] > dis:
                    dis = self.N - 1 - self.seats[-1]
                    ret = self.N - 1

            bisect.insort_left(self.seats,ret)
            return ret

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        ind=bisect.bisect_left(self.seats,p)
        del self.seats[ind]