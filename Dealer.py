# THIS MODULE CONTROLS THE TABLE

import random

DECK_OF_CARDS = {'heart': ['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK'],
                 'diamonds': ['DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK'],
                 'clubs': ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK'],
                 'spades': ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK']}


def shuffle_deck() -> list:
    """
    Returns the values in the deck_of_cards dictionary shuffled together.
    """
    hearts = DECK_OF_CARDS['heart']
    diamonds = DECK_OF_CARDS['diamonds']
    clubs = DECK_OF_CARDS['clubs']
    spades = DECK_OF_CARDS['spades']
    entire_deck = hearts + diamonds + clubs + spades
    random.shuffle(entire_deck)
    return entire_deck


def number_of_cards() -> int:
    """
    Returns an empty list for each player symbolizing how many cards they have.
    """
    players = list(range(1, int(input('How many players are playing? \n \n: ')) + 1))
    for player in players:
        exec(f'player_{player} = []')




def deal(card_game: str) -> int:
    """
    Deals each card to each of the players.
    """
    deck = shuffle_deck()
    players = list(range(1, (number_of_players() + 1)))

   # if card_game == 'black jack':
    #    for player in players:

number_of_cards()