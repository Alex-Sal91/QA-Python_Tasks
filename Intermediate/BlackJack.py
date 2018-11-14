#Given 2 integer values greater than 0,
# return whichever value is closest to 21 with- out going over 21.
# If they both go over 21 then return 0

def blackjack(card1, card2):
    if card1 == 0 or card2 == 0:
        return "Not a valid card"
    elif card1 < 21 and card1 > card2:
        return card1
    elif card1 < 21 and card2 > 21:
        return card1
    elif card1 < 21 and card2 > card1:
        return card2
    elif card1 > 21 and card2 < 21:
        return card2
    elif card1 == 21 or card2 == 21:
        return 21
    else:
        return 0


print(blackjack(0,22))