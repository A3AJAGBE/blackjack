"""
This is a basic blackjack game application
"""

# Imports
import os
import random
from logo import cards, logo


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
    return sum(player_cards)


# Clear console
def clear():
    return os.system('clear')


# Game function
def game():
    # Show logo
    print(logo)

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

        # Verify blackjack rules
        if user_score == 21 or dealer_score == 21 or user_score > 21:
            game_over = True
        else:
            another_user_deal = input("\nType 'Yes' to get another card, type 'No' to pass\n").title()

            if another_user_deal == "Yes":
                user_cards.append(deal())
            elif another_user_deal == "No":
                game_over = True
            else:
                print('Invalid Response.')
                game_over = True

    # Make sure the dealer has over 16
    while dealer_score != 21 and dealer_score < 17:
        dealer_cards.append(deal())
        dealer_score = score(dealer_cards)

    print(
        f"\nYour final hand is: {user_cards} and final score is: {user_score}.\n"
        f"The dealer's final hand is: {dealer_cards} and final score is: {dealer_score}.\n")

    # Validating score
    if user_score == dealer_score:
        print("It's a draw. Yikes")
    elif dealer_score == 21:
        print("Dealer has a Blackjack, You lose.")
    elif user_score == 21:
        print("You have a Blackjack, You win.")
    elif user_score > 21:
        print("Dealer wins because you went over 21.")
    elif dealer_score > 21:
        print("You win because dealer went over 21.")
    elif user_score > dealer_score:
        print("You Win")
    else:
        print("Dealer Win.")


# The game application
game_start = True
while game_start:
    # Default displays
    print('\nHOUSE RULES:\nUnlimited deck size.\nThere are no Jokers.\nThe Jack,Queen and King counts as 10.\n'
          'Ace can count as either 1 or 11 depending on cards already drawn.\n'
          'Cards are not removed from the deck as they are drawn.\n'
          'The computer is the dealer.\n'
          'A Blackjack means exactly 21 points.\n'
          'If player or dealer has over 21 they automatically lose.')

    # User prompts
    user_start = input('\nReady to play a game of blackjack? Type "Yes" or "No"\n').title()

    # Validate response
    if user_start == "Yes":
        clear()
        game()
    elif user_start == "No":
        clear()
        print('When ever you are ready.')
        game_start = False
    else:
        clear()
        print('Invalid Response. Restarting the game...')
        game_start = True
