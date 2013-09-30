
#All values and methods associated with the Original Ticket to Ride board game
import TTRBoard
import TTRCards
import TTRPlayer
import collections

class Game:
    def __init__(self, numPlayers):
        
        self.sizeDrawPile = 5
        self.numTicketsDealt = 3
        self.sizeStartingHand = 4
        self.endingTrainCount = 3 #when a player has less than this value of trains, trigger final round
        self.pointsForLongestRoute = 10
        self.startingNumOfTrains = 4 #45
        self.deck = TTRCards.Cards(self.sizeDrawPile)
        #self.deck.createDrawPile() is executed when deck is initialized
        
        self.board = TTRBoard.Board()
        self.numPlayers = numPlayers
        self.players = []
        for position in range(numPlayers):
            startingHand = self.deck.dealCards(self.sizeStartingHand)
            startingTickets = self.deck.dealTickets(self.numTicketsDealt)
            playerBoard = TTRBoard.PlayerBoard()
            player = TTRPlayer.Player(startingHand, startingTickets, playerBoard, position, self.startingNumOfTrains)
            self.players.append(player)
        self.posToMove = 0
        
        #point values for places tracks of different lengths
        self.routeValues = {1:1, 2:2, 3:4, 4:7, 5:10, 6:15}
        
    def getPlayer(self, playerNumber):
        return self.players[playerNumber]
    
    def getPlayerName(self, playerNumber):
        '''returns the player's name based on the player's number
        playerNumber: int
        '''
        return self.getPlayer(playerNumber).name
    
    def highestScore(self, players):
        #Not yet implimented
        pass
        
    def advanceOnePlayer(self):
        '''Updates self.posToMove'''
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
    
    def enterPlayerNames(self):
        selectedNames = []
        for player in self.players:
            count = 0
            name = raw_input("Player " + str(self.posToMove + 1) + " please enter your name: ")
            while (name in selectedNames or len(name) > 50) and count < 5:
                name = raw_input("Player " + str(self.posToMove + 1) + " please enter your name: (Must be unique) ")
                count += 1
            if len(name) > 50 or name == '' or name in selectedNames:
                name = str(self.posToMove + 1)
                player.setPlayerName(name)
                selectedNames.append(name)
            else:
                player.setPlayerName(name)
                selectedNames.append(name)
            self.advanceOnePlayer()

    def printIt(self, group):
        '''prints each item of group on its own line
        group: list or dict or set or iterable
        '''
        print ""
        kind = type(group)
        if kind == dict or kind == collections.Counter:
            for i in group:
                print i, "\t", group[i]
            print "__________________________________________"
        elif type(group) == list or type(group) == set:
            for i in group:
                print i
            print "__________________________________________" 
        else:
            print group
            print "__________________________________________"

    def scorePlayerTickets(self, player):
        '''returns None.  Scores player's destination tickets and adds/subtracts from player's points
        '''
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
                
    def scoreLongestRoute(self, players):
        '''determines which player has the longest route and adjust their score accordingly
        players: list of players
        adds self.pointsForLongestRoute to player with longest route
        '''
        
        return None

        #Waiting on this to be impimented in the Board class



    def playTurn(self, player):
        '''player chooses 'cards', 'trains', 'tickets'
        player: player object
        '''
        
        choice = raw_input("Please type: cards, trains or tickets: ")
    
        count = 0 # a way out of the loop if 5 invalid responses
        while choice not in ['cards', 'trains', 'tickets'] and count < 5:
            choice = raw_input("Invalid repsonse. Please select either cards, trains or tickets")
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
        self.printIt(player.getHand())
        
        print "Draw pile consists of: "
        self.printIt(self.deck.getDrawPile())
        
        choice1 = raw_input("Please type a card from the above list or type 'drawPile': ")
        while choice1 not in self.deck.getDrawPile() + ['drawPile'] and count < 5:
            choice1 = raw_input("Invalid repsonse. Please type either from " + \
            str(self.deck.getDrawPile()) + " or type 'drawPile' ")
            count += 1
        
        #add card to player's hand, remove it from drawPile or cards and add new card to drawPile
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
            self.printIt(player.getHand()) 
 
            return "Move complete"

        count = 0
        
        self.printIt(self.deck.getDrawPile())
         
        choice2 = raw_input("Please type another card from the above list or type 'drawPile': ")
        while choice2 == 'wild' or (choice2 not in self.deck.getDrawPile() + ['drawPile'] and count < 5):
            choice2 = raw_input("Invalid repsonse. Please type either from " + \
            str(self.deck.getDrawPile()) + " or type 'drawPile' NOTE: second choice cannot be 'wild' ")
            count += 1
            
        #add card to player's hand, remove it from drawPile or cards and add new card to drawPile
        if count >= 5:
            return "Move complete"
        elif choice2 == 'drawPile':
            chosenCard = self.deck.pickFaceDown()
            print "You selected: " + str(chosenCard)
            player.addCardToHand(chosenCard)
        else:
            player.addCardToHand(self.deck.pickFaceUpCard(choice2))
        
        print "Your hand now consists of: "
        self.printIt(player.getHand())  
        return "Move complete"
    
    def placeTrains(self, player):
        count = 0
        print "Available cities:"

        #only print routes that are legal given the players cards
        self.printIt([x for x in sorted(self.board.iterEdges()) if self.doesPlayerHaveCardsForEdge(player, x[0], x[1])]) #sort alphabetically
        
        print "Your hand consists of: "
        self.printIt(player.getHand())
        
        city1 = raw_input("Please type the start city of the route you would like to claim: ")
        while city1 not in self.board.getCities() and count < 5:
            city1 = raw_input("Invalid response.  Please type one of the following cities (without quotes): \n" + str(self.board.getCities()) + ": ")
            count += 1
        
        if count >= 5:
            return "Move complete"
            
        if len([x for x in self.board.G.neighbors(city1) if self.board.hasEdge(city1, x)]) == 0:
            print "You have a selected a city with no legal destination"
            return "Move complete"
        
        
        
        #start city2
        count = 0
        
        print "Available destination cities: " + str([x for x in self.board.G.neighbors(city1) if self.doesPlayerHaveCardsForEdge(player, city1, x)])
        city2 = raw_input("Please type the destination city to go to from " + str(city1) + " : ")
        
        while not self.board.hasEdge(city1, city2) and count < 5:
            city2 = raw_input("Invalid response.  Please type one of the following cities (without quotes): \n" + \
            str([x for x in self.board.G.neighbors(city1) if self.board.hasEdge(city1, x)]) + " : ")
            count += 1    
            
        if count >=5:
            return "Move complete"
    
        #start exchange cards and place trains
    
        routeDist = self.board.getEdgeWeight(city1, city2)
        spanColors = self.board.getEdgeColors(city1, city2)
        
        if len(spanColors) == 0:
            #a little harsh but will updated later to players start over
            print "You have a selected two cities with no legal route"
            return "Move complete"
        
        
        print "\n This route is of length: "
        self.printIt(routeDist)
        print "Your hand consists of: "
        self.printIt(player.getHand())
        
        if len(spanColors) == 1:
            color = spanColors[0]  #use first element since getEdgeColors returns a list
            print "This route is: " + str(color)
        else:
            color = raw_input("which color track would you like to claim? (" + str(spanColors) + " available) ")
            if color not in spanColors:
                print "Invalid Color"
                return "Move complete"
                
        #check to see if player has appropriate cards to play route (edge weight, color/wild)
        if not self.doesPlayerHaveCardsForEdge(player, city1, city2):
            print "You do not have sufficient cards to play this route"
            return "Move complete"
        if color == 'grey':
            availColor = max(x for x in player.hand.values())
        else:
            availColor = player.hand[color]

        availWild = player.hand['wild']
        if color == 'grey':
            
            color = raw_input("Which color would you like to play on this grey route? (pick a color, not 'wild') ")
            if color not in self.deck.possibleColors:
                print "Invalid Color"
                return "Move complete"
            availColor = player.hand[color]
            numColor = raw_input("How many " + str(color) + " cards would you like to play? (" + str(availColor) + " available) ")
        else:
            numColor = raw_input("How many " + str(color) + " cards would you like to play? (" + str(availColor) + " available) ")
        if numColor not in [str(x) for x in range(routeDist + 1)]:
            print "Invalid Entry"
            return "Move complete"
        numColor = int(numColor) # change raw string to int
        if numColor not in range(0, availColor +1):
            print "You do not have that many"
            return "Move complete"

        if numColor < routeDist: #span distance
            numWild = raw_input("How many wild cards would you like to play? (" + str(availWild) + " available) ")
            numWild = int(numWild)
            if numWild not in range(0, availWild +1):
                print "You do not have that many"
                return "Move complete"
        else:
            numWild = 0

        #verify that this is a legal move
        if numWild + numColor != routeDist:
            print "Selected cards do not properly span that route"
            return "Move complete"
        
        #claim route for player (see dedicated method within Game class)
        player.playerBoard.addEdge(city1, city2, routeDist, color)
        
        #remove route from main board
        self.board.removeEdge(city1, city2, color)
        
        #calculate points
        player.addPoints(self.routeValues[routeDist])
    
        #remove cards from player's hand
        player.removeCardsFromHand(color, numColor)
        player.removeCardsFromHand('wild', numWild)
        
        #add cards to discard pile
        self.deck.addToDiscard([color for x in range(numColor)] + ['wild' for x in range(numWild)])
        
        #remove trains from players numTrains
        player.playNumTrains(routeDist)
        
        print "Number of trains left to play: "
        self.printIt(player.getNumTrains())  
                    
        return "Move complete"
    
    def pickTickets(self, player):
        count = 0
        minNumToSelect = 1
        tickets = self.deck.dealTickets(self.numTicketsDealt)

        #assign a number to each ticket to make it easier to choose
        tickets = {x[0]:x[1] for x in zip(range(len(tickets)), tickets)}
        print "Please select at least " + str(minNumToSelect) + ": "
        
        self.printIt(tickets)
        
        choices = set()
        choice = raw_input("Select a number corresponding to the above tickets, type done when finished: ")
        while (choice != 'done' and count < 7) or len(choices) < minNumToSelect:
            try:
                choices.add(tickets[int(choice)])
                choice = raw_input("Select the number corresponding to the above tickets, type done when finished: ")
            except:
                choice = raw_input("Invalid Choice: Select the number corresponding to the above tickets, type done when finished: ")
                count += 1
        print "You selected: "
        for ticket in choices:
            player.addTicket(ticket)
            print ticket
        
        
        #add tickets that weren't chosen to the ticketDiscardPile
        notChosen = set(range(len(tickets))).difference(choices)
        for i in notChosen:
            self.deck.addToTicketDiscard(tickets[i])
        
        print "All of your tickets: "
        self.printIt(player.getTickets())
        
        return "Move complete"


def playTTR():

    #before first turn, select 1, 2 or 3 destination tickets
    
    print "\n Welcome to Ticket to Ride! \n"
    
    
    
    numPlayers = raw_input("How many players will be playing today? 1,2,3,4,5 or 6? ")

    count = 0
    while int(numPlayers) not in range(1,7) and count < 5:
        if numPlayers == 'exit': return "Thanks for playing!"
        numPlayers = raw_input("Please enter either 1,2,3,4,5 or 6: ")
        count += 1
    if count >= 5:
        print "Default player count has been set to 2"
        numPlayers = 2
        
    game = Game(int(numPlayers))    
    
    game.enterPlayerNames()
    
    player = game.players[game.posToMove]

    #main game loop
    while True:
        print "\n_________________NEW PLAYER'S TURN_________________ \n"
        print "It's your turn " + str(player.getName()) + "! "
        game.playTurn(player)
        
        #condition to break out of loop
        if game.checkEndingCondition(player):
            game.advanceOnePlayer()
            player = game.getCurrentPlayer()
            break
        game.advanceOnePlayer()
        player = game.getCurrentPlayer()
    
    print "\n This is the last round!  Everyone has one more turn! \n"
    
    for i in range(len(game.players)):
        print "\n_________________NEW PLAYER'S TURN_________________ \n"
        print "This is your LAST TURN " + str(player.getName()) + "! "
        game.playTurn(player)
        game.advanceOnePlayer()
        player = game.getCurrentPlayer()
    
    
    for player in game.players:
        game.scorePlayerTickets(player)
    
    game.scoreLongestRoute(game.players)
    

    scores = []
    for player in game.players:
        print str(player.getName()) + " had " + str(player.getPoints()) + " points!"
        score = player.getPoints()
        scores.append(score)
        
    
    winners = [x.getName() for x in game.players if x.getPoints() == max(scores)]
    if len(winners) == 1:
        print "The winner is " + str(winners[0])
    else:
        print "The winners are " + ' and '.join(winners)
    
    
    print "\n =========== fin =========== \n"

if __name__ == "__main__":

    playTTR()

