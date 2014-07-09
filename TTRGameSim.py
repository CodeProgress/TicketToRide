
#this version no longer takes input from user. 
#Designed for computer OR human player (mainly comp v comp sim)

#All values and methods associated with the Original Ticket to Ride board game
import TTRBoard
import TTRCards
import TTRPlayer
import collections
import pprint

class Game(object):
    def __init__(self, numPlayers):
        
        self.sizeDrawPile          = 5
        self.numTicketsDealt       = 3
        self.sizeStartingHand      = 4
        self.maxWilds              = 3

        self.endingTrainCount      = 3 # ending condition to trigger final round

        self.pointsForLongestRoute = 10
        self.startingNumOfTrains   = 15 #45
        self.deck                  = TTRCards.Cards(self.sizeDrawPile, self.maxWilds)
        
        self.board                 = TTRBoard.Board()
        self.numPlayers            = numPlayers
        self.players               = []
        
        self.posToMove             = 0
        
        #point values for tracks of different lengths
        self.routeValues           = {1:1, 2:2, 3:4, 4:7, 5:10, 6:15}

        for position in range(numPlayers):
            startingHand     = self.deck.dealCards(self.sizeStartingHand)
            startingTickets  = [] #self.deck.dealTickets(self.numTicketsDealt)
                                  #this is now done in initialize method below
                                  #occurs before first player's first move
            playerBoard      = TTRBoard.PlayerBoard()

            player           = TTRPlayer.Player(startingHand, 
                                                startingTickets, 
                                                playerBoard, 
                                                position, 
                                                self.startingNumOfTrains
                                                )                          
            self.players.append(player)
    
    
    def printSepLine(self, toPrint):
        print toPrint
            
    def advanceOnePlayer(self):
        """Updates self.posToMove"""
        self.posToMove += 1
        self.posToMove %= self.numPlayers
    
    def getCurrentPlayer(self):
        return self.players[self.posToMove]
    
    def doesPlayerHaveCardsForEdge(self, player, city1, city2):
        if player.playerBoard.hasEdge(city1, city2):
            return False
        routeDist = self.board.getEdgeWeight(city1, city2)
        routeColors = self.board.getEdgeColors(city1, city2)
        for col in routeColors:
            if col == 'grey':
                if max([x for x in player.hand.values() if x != 'wild']) \
                + player.hand['wild'] >= routeDist:
                    return True
            else:
                routeDist = self.board.getEdgeWeight(city1, city2)
                if player.hand[col] + player.hand['wild'] >= routeDist:
                    return True
        return False      
    
    def checkEndingCondition(self, player):
        return player.getNumTrains() < self.endingTrainCount
    
    def initialize(self):
        """Before game turns starts, enter names and pick destination tickets
        """
        
        for player in self.players:
                
            #pick desination tickets
            
            self.pickTickets(player, 2)
            
            self.advanceOnePlayer()

    