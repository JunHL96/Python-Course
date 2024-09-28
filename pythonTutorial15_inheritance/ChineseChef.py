from Chef import Chef

class ChineseChef(Chef):


    def makeFriedRice(self):
        print("The chef makes fried rice")

    # overrides Chef's makeSpecialDish
    def makeSpecialDish(self):
        print("The chef makes orange chicken")