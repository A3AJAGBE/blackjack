"""
This is a basic blackjack game application
"""

# Imports
import random
from logo import cards

# Default displays
print('HOUSE RULES:\nUnlimited deck size.\nThere are no Jokers.\nThe Jack,Queen and King counts as 10\n'
      'Ace can count as either 1 or 11\nCards are not removed from the deck as they are drawn\n'
      'The computer is the dealer\n')


# Dealing cards
def deal():
    card_deal = random.choice(cards)
    return card_deal


# Calculate scores
def score(player_cards):
    # Detect Ace in player cards
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
    else:
        return sum(player_cards)


# User prompts
user_start = input('Ready to play a game of blackjack? Type "Yes" or "No"\n').title()

# Validate response
if user_start == "Yes":
    print('Let\'s Go\n')

    user_cards = []
    dealer_cards = []

    for i in range(2):
        user_cards.append(deal())
        dealer_cards.append(deal())

    # testing
    print(f'Dealer\'s card: {dealer_cards}')

    game_over = False
    while not game_over:
        # Outputs
        user_score = score(user_cards)
        dealer_score = score(dealer_cards)
        print(f'Your cards are: {user_cards} and the current score is {user_score}')
        print(f'The dealer\'s first card is: {dealer_cards[0]}')

elif user_start == "No":
    print('When ever you are ready, start the game.')
else:
    print('Invalid Response.')
