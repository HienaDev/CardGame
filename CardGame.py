import random

DeckPlayer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DeckNPC = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def showDeck(Deck):
    
    print(str(Deck))

def shuffleDeck (Deck):

    random.shuffle(Deck)

def goFish(Deck):
    
    print("He gets " + str(Deck[12]) + " and " + str(Deck[13]))

#ola github, teste 1 2


showDeck(DeckPlayer)
print("\n")
shuffleDeck(DeckNPC)
print("NPC's Shuffled Deck: ")
showDeck(DeckNPC)
print("\nPlayer goes fish: ")
goFish(DeckPlayer)
print("\nNPC goes fish: ")
goFish(DeckNPC)