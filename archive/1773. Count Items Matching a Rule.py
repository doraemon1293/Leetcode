from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=="type":
            key_ind=0
        elif ruleKey=="color":
            key_ind=1
        elif ruleKey=="name":
            key_ind=2
        ans=[item for item in items if item[key_ind]==ruleValue]
        return len(ans)

