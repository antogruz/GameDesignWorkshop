import cartes

def nbhits(d):
    return d / float(3)

class Enn:
    def __init__(self, a, d):
        self.a = a
        self.d = d

    def value(self):
        return self.d + self.a * nbhits(self.d)/float(4)

class Hero:
    def __init__(self, name, force=0, defense=0, terre=0, eau=0, feu=0):
        self.name = name
        self.force = force
        self.defense = defense
        self.terre = terre
        self.eau = eau
        self.feu = feu

def moyenne(list):
    somme = 0
    for l in list:
        somme += l
    return somme / len(list)
ennemis = [Enn(a, d) for d in range(2, 7) for a in range(0, 2*d + 1) if (a + d) < 10 ]

def evaluate(hero, card):
    values = [card.value(hero, enn) for enn in ennemis]
    return round(moyenne(values), 2)

def main():
    heroes = [Hero(name="fighter",force=1), Hero(name="tank",defense=1), Hero(name="druide", terre=1), Hero(name="aquaman", eau=1), Hero(name="pyro", feu=1)]
    cards = [cartes.Hammer(), cartes.Dagues(), cartes.Shurikens(3), cartes.ArcElfique(), cartes.Javelot(), cartes.Enchevetrement(), cartes.IceSword(mana=1), cartes.Flammes()]
    for carte in cards:
        print "--- {} ---".format(carte.__class__.__name__)
        for hero in heroes:
            print "{} : {}".format(hero.name, evaluate(hero, carte))

main()
