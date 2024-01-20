import unittest

from SimpleGame import SimpleGame


class TestSimpleGame(unittest.TestCase):
    def setUp(self):
        self.game = SimpleGame(5, 5)

    def test_generate_board(self):
        self.game.generate_board()
        self.assertEqual(len(self.game.obstacles), min(self.game.rows * self.game.cols // 4, 5))
        self.assertNotEqual(self.game.start, self.game.stop)
        self.assertNotIn(self.game.start, self.game.obstacles)
        self.assertNotIn(self.game.stop, self.game.obstacles)

    def test_get_random_position(self):
        pos1 = self.game.get_random_position()
        pos2 = self.game.get_random_position()
        self.assertNotEqual(pos1, pos2)

    def test_move_valid(self):
        self.game.generate_board()
        initial_pos = self.game.start
        self.assertTrue(self.game.move('right'))
        self.assertNotEqual(initial_pos, self.game.start)

    def test_move_invalid(self):
        self.game.generate_board()
        while self.game.start[0] < self.game.rows - 1:
            self.game.move('down')
        initial_pos = self.game.start
        self.assertFalse(self.game.move('down'))
        self.assertEqual(initial_pos, self.game.start)

    def test_display_player(self):
        self.game.display_player()
        self.assertEqual(self.game.board[self.game.start[0]][self.game.start[1]], 'O')

if __name__ == '__main__':
    unittest.main()
