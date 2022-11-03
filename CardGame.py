import random

DeckPlayer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DeckNPC = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
Test = ("J", "Q", "K", "A")

def showDeck(Deck):
    
    print(str(Deck))

def shuffleDeck (Deck):

    random.shuffle(Deck)

def goFish(Deck):
    
    print("He gets " + str(Deck[12]) + " and " + str(Deck[13]))

def isNumber(phrase):

    try:
        val = int(phrase)
    except:
        return (0)
    else:
        return (1)

def lastCardSum(PlayerDeck, NPCDeck):
    PlayerSum = 0
    NPCSum = 0

    if (isNumber(PlayerDeck[12]) == 1):
        PlayerSum = PlayerSum + int(PlayerDeck[12])
    if (isNumber(PlayerDeck[13]) == 1):
        PlayerSum = PlayerSum + int(PlayerDeck[13])
    if (isNumber(NPCDeck[12]) == 1):
        NPCSum = NPCSum + int(NPCDeck[12])
    if (isNumber(NPCDeck[13]) == 1):
        NPCSum = NPCSum + int(NPCDeck[13])

    for i in range(len(Test)):
        if(PlayerDeck[12] == Test[i] or PlayerDeck[13] == Test[i]):
            PlayerSum = PlayerSum + 11 + i
        if(NPCDeck[12] == Test[i] or NPCDeck[13] == Test[i]):
            NPCSum = NPCSum + 11 + i

    if (PlayerSum < NPCSum):
        return (-1)
    elif (PlayerSum > NPCSum):
        return (1)
    else:
        return(0)

    





shuffleDeck(DeckPlayer)
print("Player's Shuffled Deck: ")
showDeck(DeckPlayer)
print("\n")
shuffleDeck(DeckNPC)
print("NPC's Shuffled Deck: ")
showDeck(DeckNPC)
print("\nPlayer goes fishing: ")
goFish(DeckPlayer)
print("\nNPC goes fishing: ")
goFish(DeckNPC)
print("---------------\nWho wins: " + str(lastCardSum(DeckPlayer, DeckNPC)))