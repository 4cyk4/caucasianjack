# This code defines a basic version of the game where you can play against the dealer. The player starts with $100, and each time they win or lose, their money is updated accordingly. The player can choose how much to bet each round, and the game continues until the player decides to quit or runs out of money.

import random

class Player:
    def __init__(self, name, money=100):
        self.name = name
        self.money = money

    def win(self, amount):
        self.money += amount

    def lose(self, amount):
        self.money -= amount

def deal_card():
    return random.randint(1, 11)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def play_game(player):
    while True:
        print(f"\n{player.name}'s Money: ${player.money}")
        bet = int(input("How much do you want to bet? "))
        if bet > player.money:
            print("You don't have enough money.")
            continue

        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card()]

        while True:
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)

            print(f"\nYour cards: {player_cards}, current score: {player_score}")
            print(f"Dealer's cards: {dealer_cards[0]}")

            if player_score == 0:
                print("Blackjack! You win!")
                player.win(bet)
                break
            elif player_score > 21:
                print("Busted! You lose.")
                player.lose(bet)
                break

            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                player_cards.append(deal_card())
            elif choice == 's':
                break

        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f"\nYour final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

        if dealer_score == 0:
            print("Dealer has Blackjack! You lose.")
            player.lose(bet)
        elif dealer_score > 21 or player_score > dealer_score:
            print("You win!")
            player.win(bet)
        elif player_score < dealer_score:
            print("Dealer wins!")
            player.lose(bet)
        else:
            print("It's a draw!")

        print(f"{player.name}'s Money: ${player.money}")

        if player.money == 0:
            print("You're out of money. Game over.")
            break

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

def main():
    player_name = input("Enter player's name: ")
    player = Player(player_name)

    play_game(player)

if __name__ == "__main__":
    main()
