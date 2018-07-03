class Solution(object):
    def rectangleArea(self, rectangles):
        # Populate events
        from bisect import insort_left,bisect_left
        events=[]
        for x1,y1,x2,y2 in rectangles:
            events.append((y1,"add",x1,x2))
            events.append((y2,"remove",x1,x2))
        events.sort()
        print(events)

        def cur_length(active):
            ret=0
            cur_x1=cur_x2=-1
            for x1,x2 in active:
                if x1<=cur_x2:
                    cur_x2=max(cur_x2,x2)
                else:
                    ret+=cur_x2-cur_x1
                    cur_x1,cur_x2=x1,x2
            ret+=cur_x2-cur_x1
            return ret

        active=[]
        cur_y=events[0][0]
        ans=0
        for y,typ,x1,x2 in events:
            ans+=(y-cur_y)*cur_length(active)
            if typ=="add":
                insort_left(active,(x1,x2))
            else:
                active.remove((x1,x2))
            cur_y=y

        return ans % (10**9 + 7)