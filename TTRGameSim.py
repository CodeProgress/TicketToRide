
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

    def scorePlayerTickets(self, player):
        """returns None.  
        Scores player's destination tickets and 
        adds/subtracts from player's points
        """
        for ticket in player.tickets:
            city1 = ticket[0]
            city2 = ticket[1]
            value = ticket[2]
            posNodes = player.playerBoard.getNodes()
            if city1 not in posNodes or city2 not in posNodes:
                player.subtractPoints(value)
                continue
            if player.playerBoard.hasPath(city1, city2):
                player.addPoints(value)
                
    def scoreLongestPath(self):
        """determines which player has the longest route and 
        adjusts their score accordingly
        players: list of players
        adds self.pointsForLongestRoute to player with longest route
        """

        scores = { x:(0, ()) for x in self.players }
        longestPath = 0
        for player in scores:

            for city in player.playerBoard.getCities():
                pathInfo = player.playerBoard.longestPath(city)
                if pathInfo[0] > scores[player][0]:
                    scores[player] = pathInfo
        
            if scores[player][0] > longestPath:
                longestPath = scores[player][0]
        
        print scores
        
        for player in scores:
            if scores[player][0] == longestPath:
                player.addPoints(self.pointsForLongestRoute)
        
        #does not return anthing

    def printAllPlayerData(self):
        """prints out all of the non method attributes values for all players
        """
        for player in self.players:
            print player.name
            print "------------------------------"
            for x in player.__dict__:
                print x, player.__dict__[x]
                    
            print "=============================="

    def playTurn(self, player):
        """player chooses 'cards', 'trains', 'tickets'
        player: player object
        """
        
        choice = raw_input("Please type: cards, trains or tickets: ")
    
        count = 0 # a way out of the loop if 5 invalid responses
        while choice not in ['cards', 'trains', 'tickets'] and count < 5:
            choice = raw_input("Invalid repsonse. Please select either cards, "
                               + "trains or tickets: ")
            count += 1

        #displayMap = raw_input("Display map? y/n: ")
        #if displayMap == 'y':
        #    pauseTime = raw_input("For how many seconds? (between 1 and 30): ")
        #    if int(pauseTime) not in range(1, 31):
        #        pass
        #    else:
        #        self.board.showBoard(self.board.G, int(pauseTime))
        #        #Depricated?

        if count >= 5:
            return "Move complete"
            
        if choice == 'cards':
            self.pickCards(player)
            return "Move complete"
        
        elif choice == 'trains':
            self.placeTrains(player)
            return "Move complete"
        else:
            self.pickTickets(player)
            return "Move complete"
    
    def pickCards(self, player):
        count = 0 # a way out of the loop if 5 invalid responses
        print "Your hand consists of: "
        self.printSepLine(player.getHand())
        
        print "Draw pile consists of: "
        self.printSepLine(self.deck.getDrawPile())
        
        choice1 = raw_input("Please type a card from the above list or "
                            + "type 'drawPile': ")
        while choice1 not in self.deck.getDrawPile() + ['drawPile'] \
               and count < 5:

            choice1 = raw_input("Invalid repsonse. Please type either from " 
                                + str(self.deck.getDrawPile()) 
                                + " or type 'drawPile' "
                                )
            count += 1
        
        #add card to player's hand
        #remove it from drawPile or cards and 
        #add new card to drawPile
        if count >= 5:
            pass
        elif choice1 == 'drawPile':
            chosenCard = self.deck.pickFaceDown()
            print "You selected: " + str(chosenCard)
            player.addCardToHand(chosenCard)
        else:
            player.addCardToHand(self.deck.pickFaceUpCard(choice1))
        
        #start second card selection
        if choice1 == 'wild':
            print "Your hand now consists of: "
            self.printSepLine(player.getHand()) 
 
            return "Move complete"

        count = 0
        
        self.printSepLine(self.deck.getDrawPile())
         
        choice2 = raw_input("Please type another card from the above list or "
                            + "type 'drawPile': ")
        while choice2 == 'wild'  \
               or (choice2 not in self.deck.getDrawPile() + ['drawPile'] \
               and count < 5):
            
            choice2 = raw_input("Invalid repsonse. Please type either from " 
                                + str(self.deck.getDrawPile()) 
                                + " or type 'drawPile' \
                                NOTE: second choice cannot be 'wild' "
                                )
            count += 1
            
        #add card to player's hand
        #remove it from drawPile or cards and 
        #add new card to drawPile
        if count >= 5:
            return "Move complete"
        elif choice2 == 'drawPile':
            chosenCard = self.deck.pickFaceDown()
            print "You selected: " + str(chosenCard)
            player.addCardToHand(chosenCard)
        else:
            player.addCardToHand(self.deck.pickFaceUpCard(choice2))
        
        print "Your hand now consists of: "
        self.printSepLine(player.getHand())  
        return "Move complete"
    
    def placeTrains(self, player):
        count = 0
        print "Available cities:"

        #only print routes that are legal given the players cards
        #sort alphabetically
        self.printSepLine([x for x in sorted(self.board.iterEdges()) 
                        if self.doesPlayerHaveCardsForEdge(player, x[0], x[1])])
        
        print "Your hand consists of: "
        self.printSepLine(player.getHand())
        
        city1 = raw_input("Please type the start city of desired route: ")
        
        while city1 not in self.board.getCities() and count < 5:
            city1 = raw_input("Invalid response.  "
                              + "Please select from the above city list: "
                             )
            count += 1
        
        if count >= 5:
            return "Move complete"
            
        if len([x for x in self.board.G.neighbors(city1) 
                if self.board.hasEdge(city1, x)]) == 0:

            print "You have a selected a city with no legal destination"
            return "Move complete"
        
        #start city2
        count = 0
        
        print "Available destination cities: " \
        + str([x for x in self.board.G.neighbors(city1) 
              if self.doesPlayerHaveCardsForEdge(player, city1, x)])
        
        city2 = raw_input("Please type the destination city to go to from " 
                          + str(city1) 
                          + " : "
                          )
        
        while not self.board.hasEdge(city1, city2) and count < 5:
            city2 = raw_input("Invalid response.  "
                              + "Please type one of the following cities "
                              + "(without quotes): \n" 
                              + str([x for x in self.board.G.neighbors(city1) 
                                    if self.board.hasEdge(city1, x)]) 
                              + " : "
                              )
            count += 1    
            
        if count >=5:
            return "Move complete"
    
        #start exchange cards and place trains
    
       
