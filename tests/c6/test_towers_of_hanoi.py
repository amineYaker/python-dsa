from chapter6.TowerOfHanoi import TowerOfHanoi


class TestTowersOfHanoi:
    def test_towers_of_hanoi(self):
        towersOfHanoi = TowerOfHanoi(3)
        initial_state_str = "L: [3, 2, 1]" + "\n" + "M: []" + "\n" + "R: []"
        assert str(towersOfHanoi) == initial_state_str

    def test_move(self):
        towersOfHanoi = TowerOfHanoi(3)
        towersOfHanoi.move(0, 2)
        towersOfHanoi.move(0, 1)
        towersOfHanoi.move(2, 1)
        state_str = "L: [3]" + "\n" + "M: [2, 1]" + "\n" + "R: []"
        assert str(towersOfHanoi) == state_str

    def test_illegal_move(self):
        towersOfHanoi = TowerOfHanoi(3)
        try:
            towersOfHanoi.move(0, 1)
            towersOfHanoi.move(0, 1)
            assert False, "Expected an exception for illegal move"
        except Exception as e:
            assert str(e) == "Cannot move disk 2 on top of disk 1"

    def test_illegal_move_from_empty(self):
        towersOfHanoi = TowerOfHanoi(3)
        try:
            towersOfHanoi.move(1, 0)
            assert False, "Expected an exception for moving from empty spindle"
        except Exception as e:
            assert str(e) == "Cannot move from empty spindle M"

    def test_solve(self):
        towersOfHanoi = TowerOfHanoi(3)
        towersOfHanoi.solve()
        final_state_str = "L: []" + "\n" + "M: []" + "\n" + "R: [3, 2, 1]"
        assert str(towersOfHanoi) == final_state_str
