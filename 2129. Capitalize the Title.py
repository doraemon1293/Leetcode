class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([w.lower() if len(w)<=2 else w[0].upper()+w[1:].lower() for w in title.split()])