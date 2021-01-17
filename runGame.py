from mycardgame.card_game import Game

new_game = Game()
# curr = None
# for i in range(53):

#   curr = new_game.deck.get_top_card()
# print(type(curr))

new_game.add_player("Bill")
new_game.add_player("Carl")
new_game.run_game()
