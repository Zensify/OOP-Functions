class character(object):
    def __init__(self, name, catch_phrase, taunt):
        self.name = name
        self.level = 1
        self.catch_phrase = catch_phrase
        self.taunt = taunt


Kung_Fu_Panda = character("Master Ping Xiao Po The",
                          "Skadoosh", "You have been blinded by pure awesomeness!")
Spider_Man = character("Peter Parker", "My Spider-Sense is tingling",
                       "Your friendly neighbourhood spiderman.")


# Catch-phrase
print(Spider_Man.catch_phrase)

# Change character level
if Kung_Fu_Panda.level == 1:
    Kung_Fu_Panda.level = 2
    print(f"Character is level {Kung_Fu_Panda.level}")

# taunt
print(Kung_Fu_Panda.taunt)
