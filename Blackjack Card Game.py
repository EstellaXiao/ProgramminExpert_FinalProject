# Project description: https://www.programmingexpert.io/projects/blackjack-card-game

import random

# Def int teller
def int_teller(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

# Card set value teller
def value_teller(lst):
    valuelist = []
    replace = ["T","J","Q","K"]
    for i in lst:
        valuelist.append(i[0])
    valuelist_final = ["10" if i in replace else i for i in valuelist]
    # print(valuelist_final)
    if "A" not in valuelist_final:
        sum = 0
        for i in valuelist_final:
            sum += int(i)
    else:
        number_of_a = valuelist_final.count("A")
        sum = 0
        for i in range(len(valuelist_final)-1,-1,-1):
            if valuelist_final[i] == "A":
                valuelist_final.remove("A")
        for i in valuelist_final:
            sum += int(i)
        if sum + 10 + number_of_a > 21:
            sum = sum + number_of_a
        else:
            sum = sum + 11 + (number_of_a - 1)
    return sum

# Round result teller
def result_teller(value_player,value_dealer):
    if value_player > 21:
        return "player bust"
    elif value_dealer > 21:
        return "dealer bust"
    elif value_player > value_dealer:
        return "player"
    elif value_player < value_dealer:
        return "dealer"
    else:
        return "tie"


# Define Deck Class and build related card storing + hitting + pushing functions
class Deck:
    suit = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"] #diamond,heart,club,space
    cardnum = ["A",2,3,4,5,6,7,8,9,"T","J","Q","K"]

    def __init__(self):
        self.card_deck = []
        for suit in Deck.suit:
            for num in Deck.cardnum:
                card = f"{num}{suit}"
                self.card_deck.append(card)

    def shuffle(self):
        random.shuffle(self.card_deck)

    def hit(self,n):
        if n > len(self.card_deck):
            raise ValueError("the hit number shouldn't go over the overall card number!")
        else:
            hit_card = self.card_deck[:n]
            for i in range(n):
                self.card_deck.pop(0)
            return hit_card

class Game:
    deposit = 500

    def __init__(self):
        print("\nWelcome to Blackjack!")
        self.game = Deck()
        self.game.shuffle()
        self.Player = []
        self.Dealer = []
        self.result = None

    def startgame(self,result):
        self.start_game = input(f"You are starting with ${500 + result}. Would you like to play a hand? (Enter yes to start, otherwise exit) ")
        if self.start_game.lower() != "yes":
            print("See you next time!")
            exit()
        else:
            pass

    def bet(self):
        while True:
            self.bet = input("Please place your bet: ")
            if int_teller(self.bet) != True:
                print("Bet Failed: Please place your bet in numbers.")
            elif int(self.bet) < 1:
                print("Bet Failed: The minimum bet is $1.")
            elif int(self.bet) > self.deposit:
                print("Bet Failed: You do not have sufficient funds.")
            else:
                break

    def player_round(self):
        for i in self.game.hit(2):
            self.Player.append(i)
        for i in self.game.hit(2):
            self.Dealer.append(i)
        print(f"You are dealt: {self.Player[0]},{self.Player[1]}")
        print(f"The dealer is dealt: {self.Dealer[0]},Unknown")

        if value_teller(self.Player) == 21:
            if value_teller(self.Dealer) == 21:
                self.result = "tie"
            else:
                self.result = "Player Blackjack win"
        else:
            while True:
                player_decision = input("Would you like to hit or stay? ")
                if player_decision.lower() not in ["hit", "stay"]:
                    print("Invalid input: Please enter hit or stay.")
                if player_decision.lower() == "hit":
                    for i in self.game.hit(1):
                        self.Player.append(i)
                        print(f"You are dealt: {i}")
                        card = ",".join(self.Player)
                        print(f"You now have: {card}")
                if player_decision.lower() == "stay":
                    break
                if result_teller(value_teller(self.Player), value_teller(self.Dealer)) == "player bust":
                    self.result = result_teller(value_teller(self.Player), value_teller(self.Dealer))
                    break

    def dealer_round(self):
        if self.result == "player bust":
            pass
        elif self.result == "Player Blackjack win" or self.result == "tie":
            card = ",".join(self.Dealer)
            print(f"The dealer has: {card}")
            pass
        else:
            # Enter dealer_round with player holding unbusted cards
            card = ",".join(self.Dealer)
            print(f"The dealer has: {card}")
            while value_teller(self.Dealer) <= 16:
                for i in self.game.hit(1):
                    self.Dealer.append(i)
                    print(f"The dealer hits and is dealt: {i}")
                    card = ",".join(self.Dealer)
                    print(f"The dealer has: {card}")
            print("The dealer stays.")

            self.result = result_teller(value_teller(self.Player),value_teller(self.Dealer))
            return self.result


    def result_teller(self):
        if self.result == "player bust":
            print(f"Your hand value is over 21 and you lose ${self.bet} :(")
            result = int(self.bet) * -1

            return result
        elif self.result == "Player Blackjack win":
            print(f"Blackjack! You win ${self.bet * 1.5} :)")
            result = int(self.bet) * 1.5
            return result
        elif self.result == "tie":
            print(f"You tie. Your bet has been returned.")
            result = 0
            return result
        elif self.result == "dealer bust":
            print(f"The dealer busts, you win ${self.bet} :)")
            result = int(self.bet)
            return result
        elif self.result == "player":
            print(f"You win ${self.bet} :)")
            result = int(self.bet)
            return result
        elif self.result == "dealer":
            print(f"The dealer wins, you lose ${self.bet} :(")
            result = int(self.bet) * -1
            return result
        else:
            return 0


initial_result = 0
while True:
    game = Game()
    game.startgame(initial_result)
    game.bet()
    game.player_round()
    game.dealer_round()
    initial_result += game.result_teller()





# def end_game(self):


# Start game + initial deposit
# deposit = 500
#
# print("\nWelcome to Blackjack!")
# start_game = input(f"You are starting with ${deposit}. Would you like to play a hand? (Enter yes to start, otherwise exit) ")
#
# if start_game.lower() != "yes":
#     print("See you next time!")
#     exit()
# else:
#     game = Deck()
#     game.shuffle()
#
#
# # Input bet
# while True:
#     bet = input("Please place your bet: ")
#     if int_teller(bet) != True:
#         print("Bet Failed: Please place your bet in numbers.")
#     elif int(bet) < 1:
#         print("Bet Failed: The minimum bet is $1.")
#     elif int(bet) > deposit:
#         print("Bet Failed: You do not have sufficient funds.")
#     else:
#         break

# game = Deck()
# game.shuffle()
#
# # 1st Round of Cards
# Dealer = []
# Player = []
# game_result = None
#
# for i in game.hit(2):
#     Player.append(i)
# for i in game.hit(2):
#     Dealer.append(i)
# print(f"You are dealt: {Player[0]},{Player[1]}")
# print(f"The dealer is dealt: {Dealer[0]},Unknown")
#
# # 1st Round BlackJack Checks
# player_result = value_teller(Player)
# dealer_result = value_teller(Dealer)
#
# if player_result == 21:
#     if dealer_result == 21:
#         game_result = "tie"
#     else:
#         game_result = "Player Blackjack win"
# pass
#
#
# # Player Round
# while True:
#     player_decision = input("Would you like to hit or stay? ")
#     if player_decision.lower() not in ["hit","stay"]:
#         print("Invalid input: Please enter hit or stay.")
#     if player_decision.lower() == "hit":
#         for i in game.hit(1):
#             Player.append(i)
#             print(f"You are dealt: {i}")
#             card = ",".join(Player)
#             print(f"You now have: {card}")
#     if player_decision.lower() == "stay":
#         break
#     if result_teller(value_teller(Player), value_teller(Dealer)) == "player bust":
#         game_result = result_teller(player_result, dealer_result)
#         break
#

# print(Player,Dealer)
# print(player_result,dealer_result)
# print(game_result)






