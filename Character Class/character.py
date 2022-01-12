class Character(object):
    def __init__(self, name, catch_phrase, taunt):
        self.name = name
        self.level = 0
        self.catch_phrase = catch_phrase
        self.taunt = taunt

    def speak(self, speech):
        if speech == 1:
            print(self.catch_phrase) 
        elif speech == 2:
            print(self.taunt)

    def setLevel(self, level):
        self.level == level
        print(level)
   
Kung_Fu_Panda = Character("Master Ping Xiao Po The", "Skadoosh", "You have been blinded by pure awesomeness!")
Spider_Man = Character("Peter Parker", "My Spider-Sense is tingling", "Your friendly neighbourhood spiderman.")

Kung_Fu_Panda.speak(2)
Kung_Fu_Panda.setLevel(2)
Spider_Man.speak(1)
