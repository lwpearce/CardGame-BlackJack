import Deck
import Hand
import Chips

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print('Please provide an integer.')
        else:
            if chips.bet > chips.total:
                print(f'sorry, you do not have enough chips. You have: {chips.total} chips.')
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s: ')
        if x[0].lower() == 'h' or x[0].upper() == 'H':
            hit(deck, hand)
        elif x[0].lower() == 's' or x[0].upper() == 'S':
            print('Player stands, Dealers Turn')
            playing = False
        else:
            print('Please enter h or s only!')
            continue
        break

def show_some(player, dealer):
    # show 1 dealer card from hand 
    print("\n Dealer's hand: ")
    print("First card hidden.")
    print(dealer.cards[1])   # prints the 2nd card in dealer's hand

    # show all of player's cards:
    print("\nPlayer's hand:\n")
    for card in player.cards:
        print(card)
    print(f"\nValue of Player's hand: {player.value}")

def show_all(player, dealer):
    # show all the dealer's card and all player's cards
    # display value for dealer's cards and player's cards
    print("\nDealer's hand:\n")
    for card in dealer.cards:
        print(card)
    print(f"\nValue of Dealer's hand is: {dealer.value}")
    

    print("\nPlayer's hand:",*player.cards, sep='\n')  # this does the same thing as the for loop and prints out the whole collection of the cards object.
    # for card in player.cards:
    #     print(card)
    print(f"\nValue of Player's hand is: {player.value}")

def player_busts(player, dealer, chips):
    print("Player BUST")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer BUST - Player WINS!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer WINS!")
    chips.lose_bet()

def push():
    # neither player nor dealer won
    print("Dealer and Player tied. PUSH")

game_on = True
playing = True
first_time_through = True

while game_on:
    print("Welcome to BLACKJACK! ")
    # set up deck
    deck = Deck.Deck()
    deck.shuffle_deck()
    # set up player and deal 2 cards
    player_hand = Hand.Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    # set up dealer and deal 2 cards
    dealer_hand = Hand.Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    # set up the player's chips
    if first_time_through:
        player_chips = Chips.Chips()        
    else:
        player_chips = Chips.Chips(player_chips.total)
    print(f"\n Player's total chips: {player_chips.total}")

    # prompt the player for their bet
    take_bet(player_chips)
    # show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # prompt for player to hit or stand
        hit_or_stand(deck, player_hand)
        # show cards( but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # if player's had excees 21, run player_busts() and brek out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # if player busted, play Dealer's hand until dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # show all cards
        show_all(player_hand, dealer_hand)
        # run different winning scenarios:
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push()
    # inform the player of their total chips:
    print(f"\n Player's total chips: {player_chips.total}")
    # ask if want to play again:
    new_game = input("Would you like to play another hand? y/n: ")
    if new_game[0].lower() == 'y' or new_game[0].upper() == 'Y':
        playing = True
        game_on = True
        first_time_through = False
        #continue
    else:
        print('Thank you for playing')        
        game_on = False
        #break
