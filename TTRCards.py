import random

class Cards:
    def __init__(self):
        self.cards = ["wild" for x in range(14)] + \
                    [x for x in ["red", "orange", "yellow", "green", "blue", \
                     "purple", "white", "black"] for j in range(12)]
                     
        self.shuffle(self.cards)
        
        #city1, city2, pointValue
        self.tickets = [ \
        ('Los Angeles', 'New York City', 21), \
        ('Duluth', 'Houston', 8), \
        ('Sault St Marie', 'Nashville', 8), \
        ('New York', 'Atlanta', 6), \
        ('Portland', 'Nashville', 17), \
        ('Vancouver', 'Montreal', 20), \
        ('Duluth', 'El Paso', 10), \
        ('Toronto', 'Miami', 10), \
        ('Portland', 'Phoenix', 11), \
        ('Dallas', 'New York City', 11), \
        ('Calgary', 'Salt Lake City', 7), \
        ('Calgary', 'Phoenix', 13), \
        ('Los Angeles', 'Miami', 20), \
        ('Winnipeg', 'Little Rock', 11), \
        ('San Francisco', 'Atlanta', 17), \
        ('Kansas City', 'Houston', 5), \
        ('Los Angeles', 'Chicago', 16), \
        ('Denver', 'Pittsburgh', 11), \
        ('Chicago', 'Santa Fe', 9), \
        ('Vancouver', 'Santa Fe', 13), \
        ('Boston', 'Miami', 12), \
        ('Chicago', 'New Orleans', 7), \
        ('Montreal', 'Atlanta', 9), \
        ('Seattle', 'New York', 22), \
        ('Denver', 'El Paso', 4), \
        ('Helena', 'Los Angeles', 8), \
        ('Winnipeg', 'Houston', 12), \
        ('Montreal', 'New Orleans', 13), \
        ('Sault St Marie', 'Oklahoma City', 9), \
        ('Seattle', 'Los Angeles', 9)]
        
        self.shuffle(self.tickets)
        
        self.drawPile = []
        self.createDrawPile()
        
        self.discardPile = []
        self.ticketDiscardPile = []
                
    def shuffle(self, cards):
        '''shuffles cards in-place, nothing returned
        cards: list
        '''
        random.shuffle(cards)
        
    def dealCard(self):
        '''returns a single card'''
        if len(self.cards) == 0:
            self.restockCards()
        if len(self.cards) == 0:
            return "There are no more cards in the deck!"
        return self.cards.pop()
    
    def dealTicket(self):
        '''returns a single destination ticket'''
        return self.tickets.pop()
    
    def dealCards(self, numCards):
        '''returns a list of (numCards) cards
        numCards: int
        '''
        return [self.dealCard() for x in range(numCards)]
    
    def dealTickets(self, numTickets):
        '''returns a list of (numTickets) tickets
        numTickets: int
        '''
        return [self.dealTicket() for x in range(numTickets)]
    
    def pickFaceUpCard(self, card):
        '''returns one card from draw pile
        card: string
        '''
        assert card in self.drawPile
        self.drawPile.remove(card)
        self.addToDrawPile()
        return card
        
    def pickFaceDown(self):
        '''returns the next card in cards'''
        return self.dealCard()
    
    def createDrawPile(self, sizeDrawPile = 5):
        '''adds (sizeDrawPile) more cards to draw pile'''
        assert len(self.drawPile) == 0
        for card in range(sizeDrawPile):
            self.drawPile.append(self.dealCard())
    
    def addToDrawPile(self):
        '''adds one more card to draw pile'''
        self.drawPile.append(self.dealCard())
    
    def getDrawPile(self):
        return self.drawPile
    
    def addToDiscard(self, cards):
        '''adds one or more cards to the discard pile
        does not remove cards from source they came from
        '''
        for card in cards:
            self.ticketDiscardPile.append(card)
    
    def addToTicketDiscard(self, tickets):
        '''adds one or more cards to the discard pile
        does not remove cards from source they came from
        tickets: list of length > 0
        '''
        for card in tickets:
            self.discardPile.append(card)
    
    def getTicketPointValue(self, ticket):
        '''returns the point value associated with the destination ticket
        ticket: tuple(city1, city2, value)
        '''
        return ticket[2]
    
    def cardsLeft(self):
        '''returns the number of cards left in the cards pile'''
        return len(self.cards)
    
    def ticketsLeft(self):
        '''returns the number of tickets left in the tickets pile'''
        return len(self.tickets)
    
    def restockCards(self):
        '''used when cards is empty, restocks cards with discard pile and shuffles'''
        assert len(self.cards) == 0
        self.cards = self.discardPile
        self.shuffle(self.cards)
        self.discardPile = []
    
    def restockTickets(self):
        '''used when tickets is empty, restocks tickets with ticket discard pile and shuffles'''
        assert len(self.tickets) == 0
        self.tickets = self.ticketDiscardPile
        self.shuffle(self.tickets)
        self.ticketDiscardPile = []
        
    
    def printDrawPile(self):
        '''prints the draw pile, nothing is returned'''
        print self.drawPile