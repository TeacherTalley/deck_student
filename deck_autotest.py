#!/usr/bin/env python
# ----------------------------------------------------------------------
# Programmer: Michelle Talley
# Copyright (c) 2025 Michelle Talley
# ----------------------------------------------------------------------

"""
Unit tests for the Deck class.

This module contains unit tests for the Deck class defined in the deck.py module.
The tests cover initialization, string representation, building, shuffling,
drawing, resetting, and dealing cards.
"""

import unittest
from deck import Deck
from card import Card
# from hand import Hand

class TestDeck(unittest.TestCase):
    """
    Unit test class for testing the Deck class.
    """

    def setUp(self):
        """
        Sets up the test case with a Deck object.
        """
        self.deck = Deck()

    def test_init(self):
        """
        Tests the initialization of Deck objects.
        """
        self.assertEqual(len(self.deck.cards), 54)

    def test_str(self):
        """
        Tests the string representation of Deck objects.
        """
        self.assertTrue(isinstance(str(self.deck), str))

    def test_repr(self):
        """
        Tests the repr representation of Deck objects.
        """
        self.assertTrue(isinstance(repr(self.deck), str))

    def test_build(self):
        """
        Tests the build method of Deck objects.
        """
        self.deck.cards = []
        self.deck.build()
        self.assertEqual(len(self.deck.cards), 54)

    def test_shuffle(self):
        """
        Tests the shuffle method of Deck objects.
        """
        original_order = self.deck.cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, original_order)

    def test_draw(self):
        """
        Tests the draw method of Deck objects.
        """
        card = self.deck.draw()
        self.assertTrue(isinstance(card, Card))
        self.assertEqual(len(self.deck.cards), 53)

    def test_reset(self):
        """
        Tests the reset method of Deck objects.
        """
        self.deck.draw()
        self.deck.reset()
        self.assertEqual(len(self.deck.cards), 54)

    def test_deal(self):
        """
        Tests the deal method of Deck objects.
        """
        hands = self.deck.deal()
        self.assertEqual(len(hands), 4)
        self.assertTrue(all(len(hand) == 9 for hand in hands))
        self.assertEqual(len(self.deck.cards), 18)
        """
        Tests that all cards dealt to the 4 hands are unique and not found in the remaining deck.
        """
        self.deck.reset()
        hands = self.deck.deal()
        # Flatten all cards in hands into a single list
        dealt_cards = [card for hand in hands for card in hand]
        # Use string representation for uniqueness check
        dealt_card_strs = [str(card) for card in dealt_cards]
        self.assertEqual(len(dealt_card_strs), len(set(dealt_card_strs)))
        # Check none of the dealt cards are in the remaining deck
        remaining_deck_card_strs = set(str(card) for card in self.deck.cards)
        for card_str in dealt_card_strs:
            self.assertNotIn(card_str, remaining_deck_card_strs)
        
        

if __name__ == '__main__':
    unittest.main()
