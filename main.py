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
elif user_start == "No":
    print('When ever you are ready, start the game.')
else:
    print('Invalid Response.')
