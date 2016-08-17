def contactValue(degats, defense, ennemi):
    if degats > ennemi.d:
        return ennemi.value() - (ennemi.a - defense)/float(2)
    else:
        return (degats / float(ennemi.d)) * ennemi.value() - (ennemi.a - defense)/float(2)

def distanceValue(degats, ennemi):
    if degats > ennemi.d:
        return ennemi.value()
    else:
        return (degats / float(ennemi.d)) * ennemi.value()


class Hammer:
    @staticmethod
    def value(hero, enn):
        return contactValue(4 + hero.force, hero.defense, enn)

class Dagues:
    @staticmethod
    def value(hero, enn):
        return 2 * contactValue(2 + hero.force, hero.defense, enn)

class Shurikens:
    def __init__(self):
        self.nombre = 3
    def value(self, hero, enn):
        return self.nombre * distanceValue(1, enn)

class ArcElfique:
    @staticmethod
    def value(hero, enn):
        return distanceValue(2, enn) + 0.5

class Javelot:
    @staticmethod
    def value(hero, enn):
        return distanceValue(2 + hero.force, enn)

class Enchevetrement:
    def __init__(self):
        self.mana = 1
    def value(self, hero, enn):
        return 2*distanceValue(hero.terre, enn) + distanceValue(3, enn) - 0.5*self.mana

class IceSword:
    def __init__(self):
        self.mana = 1
    def value(self, hero, enn):
        return contactValue(4 + hero.force + hero.eau, hero.defense + hero.eau, enn) - 0.5 * self.mana

class Flammes:
    def __init__(self):
        self.mana = 2
        self.deg = 4
    def value(self, hero, enn):
        return distanceValue(self.deg + hero.feu, enn) - 0.5 * self.mana

class Etincelles:
    def __init__(self):
        self.mana = 3
    def value(self, hero, enn):
        return distanceValue(2 + hero.feu, enn) + distanceValue(1 + hero.feu, enn) - 0.5 * self.mana

class Ping:
    def __init__(self):
        self.nombre = 8
        self.mana = 1
    def value(self, hero, enn):
        return distanceValue(hero.feu, enn) + self.nombre * (distanceValue(1, enn) - 0.5 *self.mana)

