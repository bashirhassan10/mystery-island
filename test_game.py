import unittest
from main import create_player, take_action


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        self.player = create_player()

    def test_starting_energy(self):
        self.assertEqual(self.player["energy"], 5)

    def test_starting_location(self):
        self.assertEqual(self.player["location"], "Beach")

    def test_starting_inventory(self):
        self.assertFalse(self.player["has_rope"])
        self.assertFalse(self.player["has_lantern"])

    def test_collect_rope_once(self):
        take_action(self.player, "5")
        take_action(self.player, "5")
        self.assertTrue(self.player["has_rope"])
        self.assertEqual(self.player["energy"], 5)

    def test_valid_move_costs_energy(self):
        take_action(self.player, "2")
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_invalid_move_does_not_cost_energy(self):
        take_action(self.player, "8")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_bridge_requires_rope(self):
        take_action(self.player, "2")
        take_action(self.player, "3")
        take_action(self.player, "6")
        self.assertEqual(self.player["location"], "Cave")
        self.assertEqual(self.player["energy"], 3)

    def test_bridge_with_rope(self):
        for choice in ("5", "2", "3", "6"):
            take_action(self.player, choice)
        self.assertEqual(self.player["location"], "Old Bridge")
        self.assertEqual(self.player["energy"], 2)

    def test_collect_lantern_in_cave(self):
        take_action(self.player, "2")
        take_action(self.player, "3")
        take_action(self.player, "7")
        self.assertTrue(self.player["has_lantern"])

    def test_lighthouse_requires_lantern(self):
        for choice in ("5", "2", "3", "6", "8"):
            take_action(self.player, choice)

        messages, outcome = take_action(self.player, "9")

        self.assertIsNone(outcome)
        self.assertIn(
            "You need a lantern to activate the Lighthouse.",
            messages
        )

    def test_win(self):
        for choice in ("5", "2", "3", "7", "6", "8"):
            take_action(self.player, choice)

        _, outcome = take_action(self.player, "9")

        self.assertEqual(outcome, "win")
        self.assertEqual(self.player["energy"], 1)

    def test_game_over_and_replay_reset(self):
        outcome = None

        for choice in ("2", "1", "2", "1", "2"):
            _, outcome = take_action(self.player, choice)

        self.assertEqual(outcome, "lose")
        self.assertEqual(self.player["energy"], 0)

        new_player = create_player()

        self.assertEqual(new_player["energy"], 5)
        self.assertEqual(new_player["location"], "Beach")
        self.assertFalse(new_player["has_rope"])
        self.assertFalse(new_player["has_lantern"])


if __name__ == "__main__":
    unittest.main()