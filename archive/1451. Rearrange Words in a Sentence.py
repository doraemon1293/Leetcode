class Solution:
    def arrangeWords(self, text: str) -> str:
        def bigger(x1,x2):
            s1,i=x1
            s2,j=x2
            if len(s1) > len(s2):
                return True
            if len(s1) < len(s2):
                return False
            if len(s1) == len(s2):
                return i>j

        def sort(arr, left, right):
            if left < right:
                x = arr[left]
                lo, hi = left, right
                while lo < hi:
                    while lo < hi and bigger(arr[hi], x):
                        hi -= 1
                    arr[lo] = arr[hi]
                    while lo < hi and not bigger(arr[hi], x):
                        lo += 1
                    arr[hi] = arr[lo]
                arr[hi] = x
                sort(arr, left, lo - 1)a
                sort(arr, lo + 1, right)

        text = [(s,i) for s,i in enumerate(text.split(" "))]
        sort(text, 0, len(text) - 1)
        text=[x[0] for x in text]
        text[0]=text[0][0].upper()+text[0][1:]
        return " ".join([s for s in text])
