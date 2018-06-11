class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = ["0"] + list(dominoes) + ["0"]
        p1 = 0
        while p1 < len(dominoes) - 1:
            p2 = p1 + 1
            while dominoes[p2] == ".":
                p2 += 1
            l = p2 - p1 - 1
            #print(p1,p2,l,dominoes[p1],dominoes[p2],dominoes)
            if dominoes[p1] == "L" and dominoes[p2] == "R":
                pass
            elif dominoes[p1] == dominoes[p2] == "L":
                dominoes[p1 + 1:p2] = ["L"] *l
            elif dominoes[p1] == "L" and dominoes[p2] == "0":
                pass
            elif dominoes[p1] == "R" and dominoes[p2] == "L":
                if l % 2 == 0:
                    dominoes[p1 + 1:p2] = ["R"] * (l // 2) + ["L"] * (l // 2)
                else:
                    dominoes[p1 + 1:p2] = ["R"] * (l // 2) + ["."] + ["L"] * (l // 2)
            elif dominoes[p1] == "R" and dominoes[p2] == "R":
                dominoes[p1 + 1:p2]=["R"]*l
            elif dominoes[p1]=="R" and dominoes[p2]=="0":
                print("**")
                dominoes[p1+1:p2]=["R"]*l
            elif dominoes[p1]=="0" and dominoes[p2]=="L":
                dominoes[p1+1:p2]=["L"]*l
            elif dominoes[p1]==dominoes[p2]=="0":
                pass
            #print(p1,p2,l,dominoes)
            #input()
            p1 = p2
        return "".join(dominoes[1:-1])

dominoes=".L.R...LR..L.."
#dominoes=".L.R"

print(Solution().pushDominoes(dominoes))