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


def number_of_players() -> dict:
    """
    Returns a dictionary of the number of players playing as keys and zero as values assigned to them
    symbolizing not having any cards.
    """
    players = list(range(1, int(input('How many players are playing? \n \n: ')) + 1))
    dict_of_players = {}
    for player in players:
        dict_of_players.update({'player_' + str(player): 0})
    return dict_of_players

def deal():
    """
    I want this to deal each player the cards and add the total to the value in the dictionary
    """