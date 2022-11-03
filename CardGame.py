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
    return (Deck[12], Deck[13])

def isNumber(phrase):

    try:
        val = int(phrase)
    except:
        return (0)
    else:
        return (int(phrase))

def lastCardSum(cards):

    sumFinal = isNumber(cards[0])
    sumFinal = sumFinal + isNumber(cards[1])
    
    for i in range(len(Test)):
        if((cards[0], cards[1])  == Test[i]):
            sumFinal = sumFinal + 11 + i

    return(sumFinal)

def whoWins(player, npc):
    if (player > npc):
        return (1)
    elif (player < npc):
        return (-1)
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
playerSum = goFish(DeckPlayer)
print("\nNPC goes fishing: ")
NPCSum = goFish(DeckNPC)
#print("---------------\nWho wins: " + str(lastCardSum(DeckPlayer, DeckNPC)))
print("---------------\nWho wins: " + str(whoWins(playerSum, NPCSum)))