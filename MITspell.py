class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
    def getDescription(self):
        return 'No Descrition'
    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def getDescription(Spell):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(Spell):
    print(Spell)
