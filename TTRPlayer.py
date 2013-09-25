import collections

class Player:
    
    def __init__(self, startingHand, startingTickets):
        '''orderNumber: int
        startingHand: list
        startingTickets: list
        '''
        self.name = '' #ask for them to enter it on first turn
        
        #implimented as a collection to avoid O(n) hand.remove(x)
        self.hand = collections.Counter(startingHand)
        self.tickets = {x:False for x in startingTickets}
        self.trains = []
        self.points = 0
                    
    def removeCardsFromHand(self, cards):
        '''removes one ore more cards from hand
        assumes all cards are in hand, error if not
        cards: list
        '''
        cardCounts = collections.Counter(cards)
        assert all(self.hand[x] - cardCounts[x] >= 0 for x in cardCounts)
        for card in cards:
            self.hand[card] -= 1
        
    #add card to hand
    def addCardToHand(self, card):
        '''adds a single card to hand
        assumes card is a valid choice
        card: String
        '''
        self.hand[card] += 1
    
    #add ticket to hand
    def addTicket(self, ticket):
        '''adds a single ticket to tickets
        ticket: tuple(city1, city2, value)
        '''
        self.tickets[ticket] = False
    
    def completeTicket(self, ticket):
        '''updates the value in the tickets dict to True for key: ticket
        ticket: tuple(city1, city2, value)
        '''
        assert ticket in self.tickets
        self.tickets = True