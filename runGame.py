from mycardgame.card_game import Game

new_game = Game()
new_game.add_player("Bill")
new_game.add_player("Carl")
new_game.run_game()
print(new_game.deck.sort_cards([(3, 3), (4, 14), (1, 2), (1, 13), (2, 5)]))
