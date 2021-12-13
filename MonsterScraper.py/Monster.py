# BWG 121221, This was mostly because I thought I could write the monster object to JSON for some reason? Idk I guess
# I'm starting to get too used to models or something and just decided to map it in main.

class Monster:
    def __init__(self, habitats, hitzones, elementalWeakness, ailmentWeakness):
        self.habitats = habitats
        self.hitzones = hitzones
        self.elementalWeakness = elementalWeakness
        self.ailmentWeakness = ailmentWeakness

    def getName(self):
        return self.name

    def setHabitats(self):
        return self.habitats

    def getHabitats(self):
        return self.habitats

    def getMonsterHitzones(self):
        return self.hitzones

    def getElementalWeakness(self):
        return self.elementalWeakness

    def getAilmentWeakness(self):
        return self.ailmentWeakness
