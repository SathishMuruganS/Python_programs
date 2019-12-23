'''
Game Play
To play a hand of Blackjack the following steps must be followed:

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again
'''


import random

# Create a deck of 52 cards

card_faces = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

card_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

card_actual_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king' : 10, 'ace' : 11}

cards = [[x,y] for x in card_faces for y in card_value]

seq_card_no = 0

class Account():
    def __init__(self, acc_balance):
        self.acc_no = random.randrange(1000,5000)
        self.acc_balance = acc_balance

    def withdraw(self, amount):
        if self.acc_balance > amount:
            self.acc_balance -= amount

    def deposit(self, amount):
        self.acc_balance += amount

    def account_balance(self):
        return self.acc_balance


class Player(Account):
    def __init__(self, acc_balance):
        self.acc = Account(acc_balance)
        self.player_cards = []
        self.card_value_count = 0
        self.bet_amount = 0

    def add_card(self, new_card):
        print(new_card)
        self.player_cards.append(new_card)
        if card_actual_value[new_card[1]] == 11:
            if self.card_value_count + 11 > 21:
                self.card_value_count += 1
            else:
                self.card_value_count += 11
        else:
            self.card_value_count += card_actual_value[new_card[1]]

        if self.card_value_count > 21:
            return 'bust'
        else:
            return 'no_bust'

    def display_card(self):
        for i in self.player_cards:
            print(i,end='')
        print()
        print('Player Card Value: {}'.format(self.card_value_count))

    def verify_bet_amount(self, amount):
        if self.acc.account_balance() < amount:
            return False
        else:
            self.bet_amount = amount
            return True

    def result_init(self):
        self.player_cards = []
        self.card_value_count = 0
        self.bet_amount = 0

    def deduct_bet_amount(self):
        self.acc.withdraw(self.bet_amount)
        self.result_init()

    def prize_amount(self, amount):
        self.acc.deposit(amount)
        self.result_init()

    def display_account_balance(self):
        print('Player Account balance :{}'.format(self.acc.account_balance()))


class Dealer():
    def __init__(self):
        self.dealer_cards = []
        self.card_value_count = 0

    def add_card(self, initial_flag):
        if initial_flag:
            new_card = draw_card()
            self.dealer_cards.append(new_card)
            # print(new_card)
            # print(card_actual_value[new_card[1]])
            if card_actual_value[new_card[1]] == 11:
                if self.card_value_count + 11 > 21:
                    self.card_value_count += 1
                else:
                    self.card_value_count += 11
            else:
                self.card_value_count += card_actual_value[new_card[1]]

            if self.card_value_count > 21:
                return 'bust'
            else:
                return 'no_bust'
        else:
            if self.card_value_count < 17:
                drawn_card = draw_card()
                self.dealer_cards.append(drawn_card)
                if card_actual_value[drawn_card[1]] == 11:
                    if self.card_value_count + 11 > 21:
                        self.card_value_count += 1
                    else:
                        self.card_value_count += 11
                else:
                    self.card_value_count += card_actual_value[drawn_card[1]]

                if self.card_value_count > 21:
                    return 'bust'
                else:
                    return 'no_bust'
            else:
                return 'reach_17'

    def result_init(self):
        self.dealer_cards = []
        self.card_value_count = 0

    def display_card(self, dealer_show_status):
        if dealer_show_status == True:
            for i in self.dealer_cards:
                print(i, end='')
            print()
            print('Dealer Card Value: {}'.format(self.card_value_count))
        else:
            print(self.dealer_cards[0])


def draw_card():
    global seq_card_no
    if seq_card_no > 51:
        return -1
    n = cards[seq_card_no]
    seq_card_no += 1
    return n


def initial_card_status():
    for _ in range(2):
        dealer.add_card(True)
        player.add_card(draw_card())


def check_result():
    if player.card_value_count > dealer.card_value_count:
        return 'player'
    else:
        return 'dealer'


while True:
    acc_balance = input('Enter the player account balance')
    if not acc_balance.isdigit():
        print('Wrong value... Please enter again...')
        continue
    break

dealer = Dealer()
player = Player(float(acc_balance))

while True:
    val = input('Do you want to continue the game (Y/N):')
    if val.lower() == 'n':
        print('Good bye...')
        break

    player_hit_status = True

    # Shuffle the deck
    random.shuffle(cards)

    seq_card_no = 0

    # Ask the Player for their bet
    player.display_account_balance()
    bet_amount = input('Enter Player bet amount')
    if not bet_amount.isdigit():
        print('Wrong value... Please enter again...')
        continue

    if player.verify_bet_amount(int(bet_amount)) == False:
        print('Account balance is less...')
        break

    # Deal two cards to the Dealer and two cards to the Player
    initial_card_status()

    # print(player.player_cards)
    # print(dealer.dealer_cards)

    # Show only one of the Dealer's cards, the other remains hidden
    print('Dealer:', end='')
    dealer.display_card(False)
    # Show both of the Player's cards
    print('Player:', end='')
    player.display_card()
    win_status_flag = True
    while win_status_flag:
        if player_hit_status:
            # Ask the Player if they wish to Hit, and take another card
            # If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
            val1 = input('Please select Hit(1) or Stand (2)')
            if val1.isdigit():
                if int(val1) != 2 and int(val1) != 1:
                    print('Wrong value... try again...')
                    continue
            else:
                print('Wrong value... try again...')
                continue

            val3 = int(val1)
            if val3 == 1:
                player_hit_status = True
                drawn_card = draw_card()
                status = player.add_card(drawn_card)
                player.display_card()
                if 'bust' == status:
                    print('Player bust...')
                    print('Dealer won....')
                    player.deduct_bet_amount()
                    dealer.result_init()
                    win_status_flag = False
                    break

            elif val3 == 2:
                player_hit_status = False
                continue

        else:
            # If a Player Stands, play the Dealer's hand. The dealer will always
            # Hit until the Dealer's value meets or exceeds 17
            dealer.display_card(True)
            while True:
                status = dealer.add_card(False)
                dealer.display_card(True)
                player.display_card()
                if status == 'reach_17':
                    winner = check_result()
                    win_status_flag = False
                    dealer.result_init()
                    if winner == 'player':
                        print('Player won...')
                        player.prize_amount(float(bet_amount)*2)
                        break
                    else:
                        print('Dealer won...')
                        player.deduct_bet_amount()
                        break
                elif status == 'bust':
                    print('Dealer bust...')
                    print('Player won...')
                    dealer.result_init()
                    player.prize_amount(float(bet_amount) * 2)
                    win_status_flag = False
                    break
