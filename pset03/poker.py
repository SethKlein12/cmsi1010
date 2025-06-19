# ----------------------------------------------------------------------
# This is the file poker.py
#
# In this file, you will write a function that classifies poker hands,
# embedding it in a small application that deals hands and announces
# the type of hand for each player.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# This program will make use of the card.py module we created in Lab 11.
#
# In this file, your main program will first ask a user for a numbers
# of players, which should be between 2 and 10. Then it will deal that
# many hands of 5 cards each, using the deal() function from card.py.
# Then, for each hand, it will call a function called classify_hand()
# that you will write, which will classify the hand and return a string
# describing the hand. The classification should be one of the following:
#
#   - "High Card"
#   - "One Pair"
#   - "Two Pair"
#   - "Three of a Kind"
#   - "Straight"
#   - "Flush"
#   - "Full House"
#   - "Four of a Kind"
#   - "Straight Flush"
#   - "Royal Flush"
#
# The classification should be done according to the rules of poker, and
# you can find the rules online or in a book about poker. You should
# use the card.py module to help you with this.
# ----------------------------------------------------------------------
import sys
from cards import Card, standard_deck, shuffled_deck, deal_one_five_card_hand

def deal_hands(num_players):
    if not (2 <= num_players <= 10):
        raise ValueError("Number of players must be between 2 and 10.")
    hands = []
    for _ in range(num_players):
        hand = deal_one_five_card_hand()
        hands.append(hand)
    return hands

def classify_hand(hand):
    ranks = sorted(card.rank for card in hand)
    suits = {card.suit for card in hand}
    if len(suits) == 1:
        if ranks == [1, 10, 11, 12, 13]:
            return "Royal Flush"
        elif ranks == list(range(ranks[0], ranks[0] + 5)) or ranks == [10, 11, 12, 13, 1]:
            return "Straight Flush"
        else:
            return "Flush"
    if len(set(ranks)) == 2:
        return "Four of a Kind" if ranks.count(ranks[0]) in (1, 4) else "Full House"
    if len(set(ranks)) == 3:
        counts = [ranks.count(rank) for rank in set(ranks)]
        return "Three of a Kind" if 3 in counts else "Two Pair"

    if len(set(ranks)) == 4:
        return "One Pair"
    if ranks == list(range(ranks[0], ranks[0] + 5)):
        return "Straight"
    return "High Card"

while True:
    print("Welcome to Poker!")
    num_players = int(input("Enter the number of players (2-10): "))
    hands = deal_hands(num_players)
    for i in range(num_players):
        print(f"Player {i + 1}: {classify_hand(hands[i])}")
        print("  Hand:", ' '.join(str(card) for card in hands[i]))
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break