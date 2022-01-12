backpackItem = []


class Backpack(object):
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

    def putIn(self, item):
        if self.open == True:
            backpackItem.append(item)

    def takeOut(self, item):
        if self.open == True:
            backpackItem.remove(item)


# task 2
blue = Backpack("blue", "small", "x")
red = Backpack("red", "medium", "x")
green = Backpack("green", "large", "x")

blue.openBag()  # Open Bag
blue.putIn("lunch")  # Put in Lunch
blue.putIn("jacket")  # Put in Jacket
blue.closeBag()  # close
blue.openBag()  # open
blue.takeOut("jacket")  # take out jacket
blue.closeBag()  # close

print(backpackItem)
