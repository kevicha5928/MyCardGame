"""Testing suite for card_game.

tests:
1) new deck test
2) add player test
3) winner test
4) sort cards test
5) shuffle deck
6) draw cards test

  Typical usage example:

  pytest

"""
from mycardgame import __version__, card_game
import pytest


@pytest.fixture
def game():
  return card_game.Game()


def new_deck():
  """creates a fresh deck"""
  deck = []
  # four suits
  for suit in range(1, 5):
    # ranks from 2-14, ace high = 14
    for rank in range(2, 15):
      deck.append((suit, rank))
  return deck


def test_new_deck(game):
  """creates a fresh deck"""
  assert game.deck.deck == new_deck()


# Player add test. Only two players allowed
@pytest.mark.parametrize("players", [
    (["Chuck", "Bob"]),
    (["Chuck", "Bob", "Dave"])
])
def test_add_player(game, players):
  """creates a fresh deck"""
  for player in players:
    game.add_player(player)

  assert len(game.players) == 2


# two players, winner is either int 1: player 1, 2: player 2, or 3 for tie
@pytest.mark.parametrize("hand1,hand2,winner", [
    ([(4, 14), (4, 13), (4, 12)], [(4, 14), (4, 13), (3, 12)], 1),
    ([(4, 14), (4, 13), (4, 12)], [(4, 14), (4, 13), (4, 12)], 3),
    ([(3, 2), (1, 13), (2, 6)], [(4, 14), (4, 13), (4, 12)], 2)
])
def test_who_wins(game, hand1, hand2, winner):
  """creates a fresh deck"""
  game.add_player("Chuck")
  game.add_player("Bob")
  for i in range(3):
    game.players[0].add_card(hand1[i])
    game.players[1].add_card(hand2[i])
  if 1 <= winner <= 2:
    assert game.determine_winner()[0].uuid == game.players[winner-1].uuid
  else:
    assert len(game.determine_winner()) == 2


# Card sorting test
@pytest.mark.parametrize("scrambled", [
    ([(1, 14), (4, 13), (2, 12)]),
    ([(4, 14), (4, 13), (4, 12)]),
    ([(1, 2), (2, 8), (2, 9), (4, 14), (4, 13), (3, 12)]),
    ([(3, 3), (4, 14), (1, 2), (1, 13), (2, 5)])
])
def test_sort_cards(game, scrambled):
  """creates a fresh deck"""
  sorted_cards = sorted(scrambled, key=lambda x: [x[0], x[1]])
  print(scrambled, sorted_cards)
  assert game.deck.sort_cards(scrambled) == sorted_cards


# Test if the deck is shuffled by comparing to a new deck
def test_shuffle_deck(game):
  """creates a fresh deck"""
  game.deck.shuffle_deck()
  assert game.deck != new_deck()


@pytest.mark.parametrize("num_draws,expected", [
    (1, True),
    (52, True),
    (53, False),
    (100, False)
])
def test_draw_card(game, num_draws, expected):
  """creates a fresh deck"""
  # Empty the deck
  curr_card = None
  for _ in range(num_draws):
    curr_card = game.deck.get_top_card()
  # attempt to draw one more card
  if expected:
    assert curr_card
  else:
    assert type(curr_card) == IndexError
