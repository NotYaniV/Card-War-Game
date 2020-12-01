

import card_war_game as cwg

player_one = cwg.Player("One")

player_two = cwg.Player("Two")

print(player_one.all_cards)

new_deck = cwg.Deck()

new_deck.shuffle()
#Split the Deck between players
#print(len(new_deck.all_cards)/2)
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


'''
print(len(player_one.all_cards))
print(len(player_two.all_cards)) 
'''

game_on = True
round = 0
while game_on:
    
    round += 1
    print(f"Round : {round}")
    
    if (len(player_one.all_cards) == 0):
        
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
    if (len(player_two.all_cards) == 0):
        
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
    
    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_one.remove_one())
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
            
        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
    
    
    