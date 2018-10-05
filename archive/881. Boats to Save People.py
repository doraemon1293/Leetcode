class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        heaviest = len(people) - 1
        lightest = 0
        boats = 0
        while lightest < heaviest:
            if limit - people[heaviest] >= people[lightest]:
                heaviest -= 1
                lightest += 1
            else:
                heaviest -= 1
            boats += 1
        if lightest==heaviest:
            boats+=1
        return boats