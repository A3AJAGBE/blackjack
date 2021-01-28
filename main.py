"""
This is a basic blackjack game application
"""

# Imports
import random

# Default displays
print('HOUSE RULES:\nUnlimited deck size.\nThere are no Jokers.\nThe Jack,Queen and King counts as 10\n'
      'Ace can count as either 1 or 11\nCards are not removed from the deck as they are drawn\n'
      'The computer is the dealer\n')

# User prompts
user_start = input('Ready to play a game of blackjack? Type "Yes" or "No"\n').title()

# Validate response
if user_start == "Yes":
    print('Let\'s Go\n')
    # Deck Cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Dealing cards
    user_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)

    #testing
    print(f'Dealer\'s card: {computer_cards}')

    user_score = 0
    for card in user_cards:
        user_score += card
    print(f'Your cards are: {user_cards} and the current score is {user_score}')
    computer_score = 0
    print(f'The dealer\'s first card is: {computer_cards[0]}')
elif user_start == "No":
    print('When ever you are ready, start the game.')
else:
    print('Invalid Response.')
