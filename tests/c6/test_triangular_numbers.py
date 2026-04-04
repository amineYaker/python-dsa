from chapter6 import TriangularNumbers as tn


class TestTriangularNumbers:
    def test_triangular(self):
        triangularNumbers = tn.TriangularNumbers()
        assert triangularNumbers.triangular(0) == 0
        assert triangularNumbers.triangular(1) == 1
        assert triangularNumbers.triangular(2) == 3
        assert triangularNumbers.triangular(3) == 6
        assert triangularNumbers.triangular(4) == 10
        assert triangularNumbers.triangular(5) == 15

    def test_triangular_iter(self):
        triangularNumbers = tn.TriangularNumbers()
        assert triangularNumbers.triangular_iter(0) == 0
        assert triangularNumbers.triangular_iter(1) == 1
        assert triangularNumbers.triangular_iter(2) == 3
        assert triangularNumbers.triangular_iter(3) == 6
        assert triangularNumbers.triangular_iter(4) == 10
        assert triangularNumbers.triangular_iter(5) == 15

    def test_triangular_tail_rec(self):
        triangularNumbers = tn.TriangularNumbers()
        assert triangularNumbers.triangular_tail_rec(0) == 0
        assert triangularNumbers.triangular_tail_rec(1) == 1
        assert triangularNumbers.triangular_tail_rec(2) == 3
        assert triangularNumbers.triangular_tail_rec(3) == 6
        assert triangularNumbers.triangular_tail_rec(4) == 10
        assert triangularNumbers.triangular_tail_rec(5) == 15
