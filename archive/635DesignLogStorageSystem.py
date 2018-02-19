import bisect
import datetime


class LogSystem(object):

    def __init__(self):
        self.logs = []
        self.ids = {}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        year, month, day, hour, minute, second = [int(x) for x in timestamp.split(":")]
        temp = datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute, second = second)
        bisect.insort(self.logs, temp)
        self.ids[temp] = id

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        year1, month1, day1, hour1, minute1, second1 = [int(x) for x in s.split(":")]
        year2, month2, day2, hour2, minute2, second2 = [int(x) for x in e.split(":")]
        if gra == "Year":
            s = datetime.datetime(year = year1, month = 1, day = 1)
            e = datetime.datetime(year = year2 + 1, month = 1, day = 1) - datetime.timedelta(seconds = 1)

        if gra == "Month":
            s = datetime.datetime(year = year1, month = month1, day = 1)
            if month2 == 12:
                e = datetime.datetime(year = year2 + 1, month = 1, day = 1) - datetime.timedelta(seconds = 1)
            else:
                e = datetime.datetime(year = year2, month = month2 + 1, day = 1) - datetime.timedelta(seconds = 1)

        if gra == "Day":
            s = datetime.datetime(year = year1, month = month1, day = day1)
            e = datetime.datetime(year = year2, month = month2, day = day2) + datetime.timedelta(days = 1) - datetime.timedelta(seconds = 1)

        if gra == "Hour":
            s = datetime.datetime(year = year1, month = month1, day = day1, hour = hour1)
            e = datetime.datetime(year = year2, month = month2, day = day2, hour = hour2) + datetime.timedelta(hours = 1) - datetime.timedelta(seconds = 1)
        if gra == "Minute":
            s = datetime.datetime(year = year1, month = month1, day = day1, hour = hour1, minute = minute1)
            e = datetime.datetime(year = year2, month = month2, day = day2, hour = hour2, minute = minute2) + datetime.timedelta(minutes = 1) - datetime.timedelta(seconds = 1)

        if gra == "Second":
            s = datetime.datetime(year = year1, month = month1, day = day1, hour = hour1, minute = minute1, second = second1)
            e = datetime.datetime(year = year2, month = month2, day = day2, hour = hour2, minute = minute2, second = second2)
        print s, e
        st = bisect.bisect_left(self.logs, s)
        en = bisect.bisect_right(self.logs, e)
        return [self.ids[x] for x in self.logs[st:en]]


["LogSystem", "put", "put", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:02:23:59:59"], ["2017:01:01:23:59:59", "2017:01:02:23:59:59", "Second"]]

obj = LogSystem()
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:02:23:59:59")
print obj.retrieve("2017:01:01:23:59:59", "2017:01:02:23:59:59", "Second")

# param_2 = obj.retrieve(s,e,gra)
