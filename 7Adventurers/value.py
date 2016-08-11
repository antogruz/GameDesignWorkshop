def nbhits(d):
    return d / float(3)

class Enn:
    def __init__(self, a, d):
        self.a = a
        self.d = d

    def value(self):
        return self.d + self.a * nbhits(self.d)/float(4)

def hammerValue(force, ennemi):
    if force > ennemi.d:
        return ennemi.value() - ennemi.a/float(2)
    else:
        return (force / float(ennemi.d)) * ennemi.value() - ennemi.a/float(2)

ennemis = [Enn(a, d) for a in range(0, 7) for d in range(2, 7) if (a + d) < 10 ]

for enn in ennemis:
    print str(enn.a) + "-" + str(enn.d) + " " + str(hammerValue(4, enn))
