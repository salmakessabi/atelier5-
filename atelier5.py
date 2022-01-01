#exercice1:
class Vecteur2D(): "definir la classe "


def __init__(self, x=0, y=0):
    self.x = x
    self.y = y


# l'instanciation de deux vecteur 
vecteur1 = Vecteur2D()
vecteur2 = Vecteur2D(5, 77)

# la methode d'affichage 
print(" les cordonnees du  vecteur 2 est : ", "(", vecteur2.x, ",", vecteur2.y, ")")
print(" les cordonnees  du vecteur 1 est : ", "(", vecteur1.x, ",", 
vecteur1.y, ")")
"la methode d'affichage"
def  affichage(self):
    print('les cordonner des ces vecteurs sont : ({0},{1})'.format(self.x,self.y))

def __add__(self, other):
    result = Vecteur2D(self.x + other.x, self.y + other.y)
    return result




"la methode d'addition "
def __add__(self, other):
    result = Vecteur2D(self.x + other.x, self.y + other.y)

    return
class Rectangle:

    langeur = 0
    hauteur = 0
    nom = ""

    def _init_(self, langeur=0, hauteur=0, nom='rectangle'):
        self.langeur = langeur
        self.hauteur = hauteur
        self.nom = nom

    def display(self): 'methode d effichage'
        print("(", self.nom, ": (", self.langeur, ", ", self.hauteur, ")")

    def surface(self):   'methode clacul de surface du rectangle'
        return self.langeur*self.hauteur


class Carre(Rectangle): 

     def _init_(self, langeur=0, hauteur=0, nom='Carre'):
        super()._init_(langeur, hauteur)
        self.nom = nom


c = Carre(3, 3, 'carre1')
r = Rectangle(1, 2, 'rectangle1')

#------------------------------------------------------------------------
#exercice2:
class Etudiant:

    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne


la_liste = [Etudiant("kessabi", "salma", 12, "N134175745", 19),
            Etudiant("lazrak", "hind", 11, "P111111111", 17),
            ]


# triage des etudiants
def triage(etudiant):
    return etudiant.age


la_liste.sort(key=triage)
print('affichage des etudiant trie par note\n')
for etudiant in la_liste:
    print("______________")
    print(etudiant.nom)
    print(etudiant.prenom)
    print(etudiant.age)
    print("______________")


# triage selon la moyenne
def triage2(etudiant):
    return etudiant.moyenne


print('affichage des etudiant trie par moyenne\n')
la_liste.sort(key=triage2)

for etudiant in la_liste:
    print("______________")
    print(etudiant.nom)
    print(etudiant.prenom)
    print(etudiant.moyenne)
    print("______________")
