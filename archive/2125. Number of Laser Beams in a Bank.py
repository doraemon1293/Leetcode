class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last=0
        ans=0
        for row in bank:
            lazers=len(row.count("1"))
            if lazers:
                ans+=last*lazers
                last=lazers
        return ans


