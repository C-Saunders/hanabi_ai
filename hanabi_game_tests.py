import unittest
from playgame import HanabiGame
from argparse import Namespace

def prep_args():
    args = Namespace()
    args.seed = 0
    args.variant = 0
    args.players = ["ai.example_discarder.Discarder", "ai.example_discarder.Discarder"]
    return args

class HanabiGameTests(unittest.TestCase):

    def setUp(self):
        args = prep_args()
        self.game = HanabiGame(args)
        self.well_formed_play = {'play_type':'play', 'card':0}
        self.malformed_play = {'play_type':'play'}
        self.well_formed_discard = {'play_type':'discard', 'card':0}
        self.malformed_discard = {}
        self.well_formed_color_disclose = {'play_type':'disclose', 'player':0, 'disclose_type':'color', 'color':'R'}
        self.malformed_color_disclose = {'play_type':'disclose', 'player':0, 'disclose_type':'color', 'color':'S'}
        self.well_formed_rank_disclose = {'play_type':'disclose', 'player':0, 'disclose_type':'rank', 'rank':2}
        self.malformed_rank_disclose = {'play_type':'disclose', 'player':0, 'disclose_type':'RANK', 'rank':7}
    
    def test_is_valid_move(self):
        self.game.table.disclose_rank(0,0)
        self.assertTrue(self.game.is_valid_move(self.well_formed_play))
        self.assertFalse(self.game.is_valid_move(self.malformed_play))
        self.assertTrue(self.game.is_valid_move(self.well_formed_discard))
        print("compare")
        self.assertFalse(self.game.is_valid_move(self.malformed_discard))
        print("compare")
        self.assertTrue(self.game.is_valid_move(self.well_formed_color_disclose))
        self.assertFalse(self.game.is_valid_move(self.malformed_color_disclose))
        self.assertTrue(self.game.is_valid_move(self.well_formed_rank_disclose))
        self.assertFalse(self.game.is_valid_move(self.malformed_rank_disclose))

    def test_is_valid_play_move(self):
        self.assertTrue(self.game.is_valid_play_move(self.well_formed_play))
        self.assertFalse(self.game.is_valid_play_move(self.malformed_play))
        self.assertFalse(self.game.is_valid_play_move(self.well_formed_discard))

    def test_is_valid_discard_move(self):
        self.assertFalse(self.game.is_valid_discard_move(self.well_formed_discard))
        self.game.table.disclose_rank(0,0)
        self.game.table.disclose_rank(0,0)
        self.game.table.disclose_rank(0,0)
        self.assertTrue(self.game.is_valid_discard_move(self.well_formed_discard))
        self.assertFalse(self.game.is_valid_discard_move(self.malformed_discard))
        self.assertFalse(self.game.is_valid_discard_move(self.well_formed_play))

    def test_is_valid_disclose_move(self):
        self.assertTrue(self.game.is_valid_disclose_move(self.well_formed_color_disclose))
        self.assertTrue(self.game.is_valid_disclose_move(self.well_formed_rank_disclose))
        self.assertFalse(self.game.is_valid_disclose_move(self.malformed_color_disclose))
        self.assertFalse(self.game.is_valid_disclose_move(self.malformed_rank_disclose))
        self.assertFalse(self.game.is_valid_disclose_move(self.well_formed_discard))

    def test_is_valid_disclose_color(self):
        self.assertTrue(self.game.is_valid_disclose_color(self.well_formed_color_disclose))
        self.assertFalse(self.game.is_valid_disclose_color(self.malformed_color_disclose))
        self.assertFalse(self.game.is_valid_disclose_color(self.well_formed_rank_disclose))

    def test_is_valid_disclose_rank(self):
        self.assertTrue(self.game.is_valid_disclose_rank(self.well_formed_rank_disclose))
        self.assertFalse(self.game.is_valid_disclose_rank(self.malformed_rank_disclose))
        self.assertFalse(self.game.is_valid_disclose_rank(self.well_formed_color_disclose))