class Solution:
    def addNegabinary(self, arr1: list, arr2: list) -> list:
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        if len(arr1) > len(arr2):
            arr2 += [0] * (len(arr1) - len(arr2))
            length = len(arr1)
        else:
            arr1 += [0] * (len(arr2) - len(arr1))
            length = len(arr2)
        arr1 += [0] * 2
        arr2 += [0] * 2
        length += 2
        carry = [0] * length
        ans = [0] * length
        print(arr1)
        print(arr2)
        print(carry)
        print(ans)
        for i in range(length):
            temp = arr1[i] + arr2[i] + carry[i]
            print(i,temp)

            if temp == -1:
                ans[i] = 1
                carry[i + 1] = 1
            elif temp < 2:
                ans[i] = temp
            elif temp >= 2:
                ans[i] = temp - 2
                carry[i + 1] = -1
        while len(ans)>1 and ans[-1]==0:
            ans.pop()
        return ans[::-1]


arr1 = [1, 1, 1, 1, 1]
arr2 = [1, 0, 1]
print(Solution().addNegabinary(arr1, arr2))

