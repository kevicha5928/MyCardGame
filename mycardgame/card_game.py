"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  new_game = Game()
  new_game.add_player("Bob")
  new_game.add_player("Chuck")
  new_game.run_game()

"""
from random import shuffle
from typing import Tuple
from uuid import uuid4


class Player:
  """Player Object

  Keeps track of player, identity, hand, and score

  Attributes:
      name: a string representing player name
      score: an int for player score
  """

  def __init__(self, name: str):
    self.name = name
    self.uuid = uuid4()
    self.__hand = []
    self.score = 0

  def add_card(self, card: Tuple[int, int]) -> None:
    """Adds a card to the player's current hand.
    Args:
        card: a tuple representing a card

    """
    self.__hand.append(card)
    self.score += card[0]*card[1]

  def reset_hand(self) -> None:
    """Empty the player's hand"""
    self.__hand = []
    self.score = 0

  def print_score(self):
    """Prints out the player's score"""
    print(f"{self.name}'s score is {self.score}")


class Deck:
  """A class for creating a new deck of cards

  Creates a new deck on instantiation.
  Assumptions:
  Suit order from lowest to highest: Spades, Diamonds, Hearts, Clubs
  Suits are assigned values 1-spades, 2-diamonds, 3-hearts, 4-clubs
  Ranks range from 2-14 ace high. Ace-14, King-13, Queen-12, Jack-11


  Attributes:
      deck: an array with all the cards in a deck
  """

  def __init__(self):
    self.deck = []
    self.new_deck()

  def new_deck(self) -> None:
    """creates a fresh deck"""
    self.deck = []
    # four suits 1-4
    for suit in range(1, 5):
      # ranks from 2-14, ace high = 14
      for rank in range(2, 15):
        self.deck.append((suit, rank))

  def shuffle_deck(self) -> None:
    """Shuffles the deck"""
    shuffle(self.deck)
    return self.deck

  @staticmethod
  def sort_cards(deck) -> None:
    """Sorts the deck from lowest to highest. Suits first, then rank"""
    return sorted(deck, key=lambda card: [card[0], card[1]])

  def get_top_card(self) -> Tuple[int, int]:
    """Retrieves the top card from the deck

    Returns:
        a tuple representing a card
    """
    try:
      return self.deck.pop()

    except IndexError as error:
      print("No cards left in deck.")
      return error


class Game:
  """Game Class

  Assumptions:
  1) A deck is not provided, we use a new deck on game creation
  2) only 2 players will play the game
  3) there are only 3 turns, each player draws once per turn
  4) score is calculated via (suit value) * (rank)


  Attributes:
      deck: deck class representing a deck of cards
      players: a list of players in the game (currently only using 2 players)
  """

  def __init__(self, players: int = 2, turns: int = 3):
    self.deck = Deck()
    self.players = []
    self.__num_players = players
    self.__num_turns = turns
    self.__current_turn = 0
    self.__suit_ref = {
        1: "Spades",
        2: "Diamonds",
        3: "Hearts",
        4: "Clubs"
    }
    self.__rank_ref = {
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }

  def add_player(self, player_name: str) -> None:
    """Add a player to the game

    Args:
        player_name: it is what it is

    """
    if len(self.players) >= self.__num_players:
      print("Maximun number of players already in game.")
    elif isinstance(player_name, str):
      self.players.append(Player(player_name))
    else:
      print("Invalid Input.")

  def new_game(self, new_deck: bool = False) -> None:
    """Resets current game with current players

    Args:
        new_deck: option for resetting the deck to a fresh unsorted deck


    """
    if new_deck:
      self.deck.new_deck()
    for player in self.players:
      player.reset_hand()

  def determine_winner(self):
    """declares the winner of the game

    Returns:
        a list with the winners. 1 winner = 1 list elem
        multiple winners = multiple list elems, representing a tie

    """
    winner = []
    curr_max_score = 0
    for player in self.players:
      if player.score > curr_max_score:
        winner = []
        winner.append(player)
        curr_max_score = player.score
      elif player.score == curr_max_score:
        winner.append(player)
    for player in self.players:
      player.print_score()
    if len(winner) == 1:
      print(f"{winner[0].name} wins with a score of {winner[0].score}")
      return winner

    print("Its a tie!")
    return winner

  def run_game(self):
    """run current game"""
    if len(self.players) <= 1:
      print("Not Enough Players.")
      return None

    else:
      game_valid = True
      self.deck.shuffle_deck()
      for _ in range(self.__num_turns):
        if len(self.deck.deck) < 2:
          print("Not enough remaining cards to continue the game.")
          game_valid = False
          break
        for player in self.players:
          card = self.deck.get_top_card()
          player.add_card(card)
          print(
              f"Player {player.name} draws the " +
              f"{self.__rank_ref[card[1]]} of {self.__suit_ref[card[0]]}")
      if game_valid:
        return self.determine_winner()
