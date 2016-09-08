import TTRBoard
import TTRCards
import TTRPlayer


class Game(object):
    def __init__(self):

        self.sizeDrawPile = 5
        self.maxWildsToDrawFrom = 3
        self.numTicketsDealt = 3
        self.minTicketsToKeepAtStart = 2
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

    def get_num_of_players(self):
        while True:
            try:
                self.numPlayers = int(raw_input("Enter number of players: "))
                assert 1 <= self.numPlayers <= 6
            except (ValueError, AssertionError):
                print "Invalid response. Please enter '1', '2', '3', '4', '5' or '6'"
                continue
            break

    def create_all_players(self):
        for position in range(self.numPlayers):
            startingHand = self.deck.dealCards(self.sizeStartingHand)
            startingTickets = []
            playerBoard = TTRBoard.PlayerBoard()

            player = TTRPlayer.Player(startingHand, startingTickets, playerBoard, position, self.startingNumOfTrains)

            self.players.append(player)

    def print_cards(self, cards):
        for i, card in enumerate(cards):
            print "{}: {}".format(i, card)

    def narrow_down_starting_tickets(self, player):
        possible_tickets_to_choose_from = self.deck.dealTickets(self.numTicketsDealt)
        while True:
            choices = []
            self.print_cards(possible_tickets_to_choose_from)
            try:
                chosen_cards = raw_input("Enter numbers corresponding to the cards you'd like to keep: (Ex: 0 1 (or) 0 1 2) ")
                chosen_cards = chosen_cards.split(' ')
                assert len(chosen_cards) >= self.minTicketsToKeepAtStart
                for i in chosen_cards:
                    choice = int(i)
                    assert 0 <= choice < len(possible_tickets_to_choose_from)
                    choices.append(choice)

                # Once all choices have been verified add to players hand
                for i, ticket in enumerate(possible_tickets_to_choose_from):
                    if i in choices:
                        player.addTicket(ticket)
                    else:
                        self.deck.addToTicketDiscard(ticket)
            except (ValueError, AssertionError):
                print "\nInvalid response.  Numbers must be separated by one space and you must choose at least {} cards.".format(self.minTicketsToKeepAtStart)
                continue
            break
        print player.tickets

    def narrow_down_starting_tickets_for_all_players(self):
        for player in self.players:
            print "\nPlayer {}, it's your turn to select destination tickets! \n".format(player.playerPosition)
            self.narrow_down_starting_tickets(player)

    def initialize_game(self):
        self.get_num_of_players()
        self.create_all_players()
        self.narrow_down_starting_tickets_for_all_players()

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
        self.initialize_game()

        # While game not over, play turn, rotating through players

        # Score every player

        # Display scores/data
        pass


if __name__ == "__main__":
    g = Game()
    g.playTTR()
