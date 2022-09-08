class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        energy0,exp0=initialEnergy,initialExperience
        energy1=exp1=0
        for energy,exp in zip(energy,experience):
            if energy0<=energy:
                energy1=max(energy1,energy-energy0+1)
            if exp0<=exp:
                exp1=max(exp1,exp-exp0+1)
            exp0+=exp
            energy0 -= energy
        return exp1+energy1



