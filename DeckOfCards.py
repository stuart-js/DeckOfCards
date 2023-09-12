# Creating a deck of cards to practice classes and object oriented programming
# Practice using doubly linked lists - THIS might be the wrong choice of data structure to use
# Algorithm for this will be more diffcult than using indices and arrays. Especially when alternating for 
# a riffle shuffle.

class CardDeck():

    def __init__(self) -> None:
        #self.cards = # list of cards in deck
        #self.topCard = #TODO - complete top and bottom cards
        #self.bottomCard = 
        self.deck = []

    def build_deck(self):
        # Iterate through each suit
        # Link each card with and previous
        define_ace_value = input("Ace High or Low? H or L?").strip()
    
        suits = ["C", "H", "D", "S"]
        facecards = ["J","Q","K"]

        for suit in suits:
            if define_ace_value == "L":
                self.deck.append(Card("A", suit, False))
            for num in range(2,11):
                self.deck.append(Card(num, suit, False))
            for facecard in facecards:
                self.deck.append(Card(facecard, suit, True))
            if define_ace_value == "H":
                self.deck.append(Card("A", suit, False))



        
        
        #self.topCard = Card("Ace", "Clubs", False)
        #self.bottomCard = Card("King", "Spades", True)

    def split_deck(self):
        # Split the deck in half
        pass
    
    def riffle_shuffle(self):
        # Deck is split in half, each card is fanned into the other side.
        # This might be very difficult to implement using linked lists. 
        # Array and indices may be a better data structure
        # Could place each object into a list of objects rather than using a linked list!

        pass


class Card():
    # should each card be an object?
    # Should also function as a linked list?
    isCard = True

    def __init__(self, value: int, suit: str, face: bool) -> None:
        self.value = value
        self.suit = suit
        self.face = face
        #self.prevCard = 
        #self.nextCard =

    def __str__(self):
        
        string = ( str(self.value) + self.suit +
                "\tFaceCard: " + str(self.face)
                )


        return string
    



# When deck is instatiated in creates a new deck of cards
""" A new deck of cards contains:
    Ace:        2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A  
    Clubs:      2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    Hearts:     2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    Diamonds:   2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A 
"""

# Builder function creates all the cards in a fresh deck
# It uses the Card Class for each card and iterates over the numbers
# and the face cards.

def main():
    
    eight_hearts = Card(8, "Hearts", False)
    
    #print(eight_hearts) # This just prints object, need actual values
                        # Need to use __str__ method to return what you want to print of class

    # How will I create a whole deck of 52 cards?
    # Need to create each card and put them in the deck
    # Each card can be a node of a linked list.

    #print(str(eight_hearts.isCard))

    deck = CardDeck()
    deck.build_deck()
    
    for i in range(0,52):
        print(deck.deck[i])

    """
    #TESTS
    # Test topCard
    if str(deck.topCard) == "Ace of Clubs\nFaceCard: False":
        print("Passed")
    else:
        print("Failed")

    # Test bottomCard
    if str(deck.bottomCard) == "King of Spades\nFaceCard: True":
        print("Passed")
    else:
        print("Failed")
    """

if __name__ == "__main__":
    main()