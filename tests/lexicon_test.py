import unittest

from character import *
from item import *
from location import *
from lexicon import *


class TestLexicon(unittest.TestCase):
    paths = ["north", "south", "east", "west"]
    verbs = ["look", "show", "take", "use", "move", "pick"]
    ignores = ["the", "in", "at", "of"]
    lexicon = Lexicon(paths, verbs, ignores)

    def test_lexicon_init(self):

        self.assertEqual(len(self.lexicon.vocab), 14)
        self.assertTrue(self.lexicon.vocab.get('north'), 'path')
        self.assertFalse("cat" in self.lexicon.vocab)
        self.assertTrue("look" in self.lexicon.vocab)
        self.assertTrue("north" in self.lexicon.vocab)

    def test_paths(self):
        self.assertEqual(self.lexicon.get_action_from_sentence("north"), [('path', 'north')])
        result = self.lexicon.get_action_from_sentence("nOrth south EAst")
        self.assertEqual(result, [('path', 'north'), ('path', 'south'), ('path', 'east')])

    def test_verbs(self):
        self.assertEqual(self.lexicon.get_action_from_sentence("move"), [('verb', 'move')])
        result = self.lexicon.get_action_from_sentence("look use pick")
        self.assertEqual(result, [('verb', 'look'), ('verb', 'use'), ('verb', 'pick')])

    def test_ignores(self):
        self.assertEqual(self.lexicon.get_action_from_sentence("the"), [('ignore', 'the')])
        result = self.lexicon.get_action_from_sentence("the in Of")
        self.assertEqual(result, [('ignore', 'the'), ('ignore', 'in'), ('ignore', 'of')])

    def test_numbers(self):
        self.assertEqual(self.lexicon.get_action_from_sentence("1234"), [('number', 1234)])
        result = self.lexicon.get_action_from_sentence("3 91234")
        self.assertEqual(result, [('number', 3), ('number', 91234)])

    def test_errors(self):
        self.assertEqual(self.lexicon.get_action_from_sentence("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
        result = self.lexicon.get_action_from_sentence("take IAS")
        self.assertEqual(result, [('verb', 'take'), ('error', 'IAS')])
