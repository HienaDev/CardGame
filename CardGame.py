import random
import string

DeckPlayer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DeckNPC = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
Test = ("J", "Q", "K", "A")

def showDeck(Deck):
    
    print(str(Deck))

def shuffleDeck (Deck):

    random.shuffle(Deck)

def goFish(Deck):
    
    return (Deck[len(Deck) - 2], Deck[len(Deck) - 1])

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
        if(Test[i] in (cards[0], cards[1])):
            sumFinal = sumFinal + 11 + i

    return(sumFinal)

def whoWins(player, npc):

    print("Player sum: " + str(player) + " \nNPC sum: " + str(npc))
    print("------------------------------------------")
    if (player > npc):
        print("Player Wins!")
        return (1)
    elif (player < npc):
        print("NPC Wins!")
        return (-1)
    else:
        print("It's a tie!")
        return(0)


def discardCard(hand):

    while (True):
        discard = input("How many cards would you like to discard? Your hand is " + hand[0] + " and " + hand[1] + "\n").translate({ord(c): None for c in string.whitespace})
        if (discard == "0"):
            break
        elif (discard == "1"):
            whatDiscard = input("\nWhat card do you want to discard? 1) " + hand[0] + " 2) " + hand[1] + "\n").translate({ord(c): None for c in string.whitespace})
            if (whatDiscard == "1"):
                hand = (goFish(DeckPlayer[:12])[1], hand[1])
                print("You get " + goFish(DeckPlayer[:12])[1] + "!")
            elif (whatDiscard == "2"):
                hand = (hand[0], goFish(DeckPlayer[:12])[1])
                print("You get " + goFish(DeckPlayer[:12])[1] + "!")
            else:
                print("Invalid Choice")
                continue
            break
        elif (discard == "2"):
            hand = goFish(DeckPlayer[:12])
            print("You get " + str(hand))
            break
        else:
            print("Invalid Choice")
    
    return (hand)

shuffleDeck(DeckPlayer)
print("Player's Shuffled Deck: ")
showDeck(DeckPlayer)
print("\n")
shuffleDeck(DeckNPC)
print("NPC's Shuffled Deck: ")
showDeck(DeckNPC)
print("\nPlayer goes fishing: ")
playerHand = goFish(DeckPlayer)
print(str(playerHand))
print("\nNPC goes fishing: ")
NPCHand = goFish(DeckNPC)
print(str(NPCHand))
playerHand = discardCard(playerHand)
whoWins(lastCardSum(playerHand), lastCardSum(NPCHand))