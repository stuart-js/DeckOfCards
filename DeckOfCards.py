# Creating a deck of cards to practice classes and object oriented programming

class CardDeck():

    def __init__(self) -> None:
        #self.cards = # list of cards in deck
        pass


class Card():
    # should each card be an object?
    # Should also function as a linked list?
    isCard = True

    def __init__(self, face: bool, value: int, suit: str) -> None:
        self.face = face
        self.value = value
        self.suit = suit
        #self.prevCard = 
        #self.nextCard =

    def __str__(self):
        
        string = ( str(self.value) + " of " + self.suit +
                "\nFaceCard: " + str(self.face)
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
    
    eight_hearts = Card(False, 8, "Hearts")
    
    print(eight_hearts) # This just prints object, need actual values
                        # Need to use __str__ method to return what you want to print of class

    # How will I create a whole deck of 52 cards?
    # Need to create each card and put them in the deck
    # Each card can be a node of a linked list.

    #print(str(eight_hearts.isCard))
    

if __name__ == "__main__":
    main()