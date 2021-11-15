import itertools

class Card:
    newidC = itertools.count()
    def __init__(self, name):
        self.cardID = next(Card.newidC)
        self.name = name
        # True = Up tight
        # False = Up side down
        self.orientation = True
    
    def get_id(self):
        return self.cardID
    
    def get_name(self):
        return self.name

    def get_orientation(self):
        # True = Up tight
        # False = Up side down
        return self.orientation

    def set_orientation(self, ori):
        # True = Up tight
        # False = Up side down
        self.orientation = ori

class MajorAcanas(Card):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def get_type(self):
        return self.type

class MinorAcanas(Card):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def get_type(self):
        return self.type

class Numbers(Card):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def get_type(self):
        return self.type

class Suits(Card):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def get_type(self):
        return self.type