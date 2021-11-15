class Game:
    def __init__(self, playerNum, cardNum):
        self.playerNum = playerNum
        self.cardNum = cardNum
    
    def get_playerNum(self):
        return self.playerNum; 

    def pick_card(self, cardNum, playerID):
        if cardNum == 1:
            return Pick_one_card(playerID)
        elif cardNum == 2: 
            return Pick_two_card(playerID)
        elif cardNum == 3: 
            return Pick_three_card(playerID)
        elif cardNum == 0: 
            return Pick_creative_card(playerID)
    
    def add_Player(self):
        pass

    def choose_Player(self):
        pass

    def Play_Game(self):
        pass

    def get_history(self):
        # get history by id 
        pass


    def Pick_one_card(self, playerID):
        pass

    def Pick_two_card(self, playerID):
        pass

    def Pick_three_card(self, playerID):
        pass

    def Pick_creative_card(self, playerID):
        pass

    def readDatabase(self, playerID):
        pass

    def writeDatabase(self, playerID):
        pass
