backpackItem = []

class backpack(object):
    def __init__(self, color, size, item):
        self.color = color 
        self.size = size 
        self.item = item 
        self.open = False

    def openBag(self):
        if self.open == False:
            self.open = True
    
    def closeBag(self):
        if self.open == True:
            self.open = False

    def putIn(self):
        if self.open == True:
            backpackItem.append("lunch") 
            backpackItem.append("jacket")
    
    def takeOut(self):
        if self.open == True:
            backpackItem.pop(1)


#task 2
blue = backpack("blue", "small", "x")
red = backpack("red", "medium", "x")
green = backpack("green", "large", "x")

#blue.openBag() #Open Bag
blue.putIn() #Put in lunch and jacket
blue.closeBag() #close 
#blue.openBag() #open
blue.takeOut() #take out jacket
blue.closeBag() #close

print(backpackItem)