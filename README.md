# MyCardGame

This project uses poetry as a package/virtual env managers
https://python-poetry.org/
install poetry then run teh following in the command line
poetry install
poetry shell

Assumptions:

1. a new game is instantiated with a fresh unsorted deck.
2. cards are ranked from lowest to highest with the following scheme
   Suits:
   Spades = 1
   Diamonds = 2
   Hearts = 3
   Clubs = 4
   Cards:
   2-10 -> 2-10
   Jack = 11
   Queen = 12
   King = 13
   Ace = 14
3. players will not remove cards from their hands
4. if two players get the same score, its a tie
