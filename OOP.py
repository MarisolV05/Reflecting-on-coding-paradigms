#First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
def __init__(self, max_speed, conditions, price):
    self.max_speed = max_speed
    self.conditions = conditions
    self.price = price

#Define a repair() method that will update the condition of the podracer to "repaired".
def repair(self):
    self.condition = "repaired"

#Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
    

#Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".