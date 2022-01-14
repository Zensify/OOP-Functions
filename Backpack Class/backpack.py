
class Backpack(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    def openBag(self):
        if self.open == False:
            self.open = True

    def closeBag(self):
        if self.open == True:
            self.open = False

    def putIn(self, item):
        if self.open == True:
            self.items.append(item)

    def takeOut(self, item):
        if self.open == True:
            self.items.remove(item)


# task 2
blue = Backpack("blue", "small")
red = Backpack("red", "medium")
green = Backpack("green", "large")

blue.openBag()  # Open Bag
blue.putIn("lunch")  # Put in Lunch
blue.putIn("jacket")  # Put in Jacket
blue.closeBag()  # close
blue.openBag()  # open
blue.takeOut("jacket")  # take out jacket
blue.closeBag()  # close
