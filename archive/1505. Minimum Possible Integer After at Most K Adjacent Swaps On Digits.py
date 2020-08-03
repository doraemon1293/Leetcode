
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        def sum1ton(n):
            return (1+n)*n//2

        def brutforce(num,k: int):
            N = len(num)
            i = 0
            while i < N - 1 and k > 0:
                min_ind = i
                j = i + 1
                while j - i <= k and j < N:
                    if num[j] < num[min_ind]:
                        min_ind = j
                    j += 1
                num[i:min_ind + 1] = [num[min_ind]] + num[i:min_ind]
                k -= min_ind - i
                i += 1
            return num

        def solve(num,k,digit):
            if digit==10:
                return num
            if k==0:
                return num

            positons = []
            summ = 0
            for i, x in enumerate(num):
                if x ==digit:
                    positons.append(i)
                    summ += i

            if len(positons)==0:
                return solve(num,k,digit+1)
            temp=summ-sum1ton(len(positons)-1)
            if k>=temp:# if can move all digit to left
                new_num=[x for x in num if x!=digit]
                res=[digit]*len(positons)+solve(new_num,k-temp,digit+1)
                return res
            else:#otherwise try to move as many digit to left as possible
                ind=0
                while k>=positons[ind]-ind:
                    k-=positons[ind]-ind
                    ind+=1
                pre=[digit]*ind
                temp=[x for x in num[:positons[ind]] if x!=digit]+num[positons[ind]:]
                return pre+brutforce(temp,k)

        num=[int(ch) for ch in num]
        ans=solve(num,k,0)
        return "".join([str(x) for x in ans])
