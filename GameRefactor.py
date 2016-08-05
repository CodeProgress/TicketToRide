import TTRBoard
import TTRCards
import TTRPlayer


class Game(object):
    def __init__(self):

        self.sizeDrawPile = 5
        self.maxWildsToDrawFrom = 3
        self.numTicketsDealt = 3
        self.sizeStartingHand = 4

        self.endingTrainCount = 3  # ending condition to trigger final round

        self.pointsForLongestRoute = 10
        self.startingNumOfTrains = 45

        self.deck = TTRCards.Cards(self.sizeDrawPile, self.maxWildsToDrawFrom)
        self.board = TTRBoard.Board()
        self.numPlayers = 0  # to be determined
        self.players = []
        self.posToMove = 0

        # point values for tracks of different lengths
        self.routeValues = {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15}

        # add numPlayers

    def initialize(self):
        # get number of players
        # get player names
        # players pick initial destination tickets (at least two of three)
        pass

    def is_game_over(self):
        pass

    def score_routes(self):
        pass

    def score_tickets(self):
        pass

    def score_longest_path(self):
        pass

    def playTurn(self, player):
        # player can choose one of the following:
        #     acquire more color cards
        #     place trains along a route
        #     acquire more destination tickets
        pass

    def pickCards(self, player):
        pass

    def placeTrains(self, player):
        pass

    def pickTickets(self, player, minNumToSelect=1):
        pass

    def playTTR(self):
        # Get number of players

        # Initialize Game

        # While game not over, play turn, rotating through players

        # Score every player

        # Display scores/data
        pass


if __name__ == "__main__":
    g = Game()
    g.playTTR()
