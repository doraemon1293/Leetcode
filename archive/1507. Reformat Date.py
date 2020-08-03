class Solution:
    def reformatDate(self, date: str) -> str:
        a=["1st", "2nd", "3rd", "4th", ..., "30th", "31st"]
        b=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return "{}-{}-{}".format(date.split(" ")[2],str(b.index(date.split(" ")[1])+1).zfill(2),"".join([ch for ch in date.split(" ")[0] if ch.isdigit()]).zfill(2))


