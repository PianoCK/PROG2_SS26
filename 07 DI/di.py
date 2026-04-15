# Dependency Inversion!!!
class Item:
    def use(self):
        pass # Ich kenne das Verhalten von meinem Item noch gar nicht

class MagicPotion(Item):
    def use(self):
        print("Puff!!!")

class Schwert(Item):
    def use(self):  # Verhalten der Klasse Schwert
        print("Zing!!!")

class SuperSchwert(Schwert):
    def use(self):
        print("Zing!!! Zing!!! Zing!!!")

# Dependency Injection!! --> Das ist cool, damit kann das Schwert ohne den Ritter weiter verwendet werden
class Player:
    def __init__(self, name: str):
        self.name = name
        self.item = None # Ritter hat gar nichts (has a)

    def nehmeItemAuf(self, item: Item):
        self.item = item # Ritter bekommt ein Item injeziert

    def useItem(self):
        self.item.use() # Ein Item kann benutzt werden laut Vertrag / Interface (use())

class SuperRitter(Player):  # SuperRitter ist ein Ritter (is a)
    def fliegen(self):
        print("Hui!!!")

schwert = Schwert()
superschwert = SuperSchwert()
valerie = Player("Valerie") # Die Referenzvariable valerie zeigt auf ein neu erstelltes Objekt der Klasse Ritter
valerie.nehmeItemAuf(superschwert) # Ritter findet ein Schwert und nimmt es auf
valerie.useItem()
valerie.fliegen()

