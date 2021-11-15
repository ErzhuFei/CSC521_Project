from csv import reader
from pprint import pprint
import Card
import Player
import Game
import sqlite3


def main():
    # get connected with the database
    card_conn = sqlite3.connect("GameHistory.db")

    # initialize all the cards 
    cards = []
    # read csv file as a list of lists
    with open('TarotCard.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_data = list(csv_reader)
    
    for data in list_of_data:
        if data[2] == 'Major':
            cards.append(Card.MajorAcanas(data[1], data[2]))
        elif data[2] == 'Minor':
            cards.append(Card.MinorAcanas(data[1], data[2]))
    
    # start the game instance
    current_Game = Game.Game(0, 78)

    # options for player
    while (True): 
        print('Welcome to the Tarot Game,')
        print('Currently we have {0} players.'.format(current_Game.get_playerNum()))
        print("Shall we begin?")
        print('1. Add Players')
        print('2. Choose Players')
        print('3. Play a Game')
        print('4. Load History')
        print('5. Quit the Game')
        
        choice = int(input())
        if choice == 1: 
            current_Game.add_Player()
        elif choice == 2: 
            current_Game.choose_Player()
        elif choice == 3:
            current_Game.Play_Game()
        elif choice == 4:
            current_Game.get_history()
        elif choice == 5: 
            print('Thanks for playing, see you next time.')
            exit()
        else: 
            print('Unexpected input, lets try again :)')

if __name__ == "__main__":
    main()