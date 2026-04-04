import pytest
import sys
from chapter6.TriangularNumbers import TriangularNumbers


def test_triangular_fails_at_1000_depth():
    triangularNumbers = TriangularNumbers()
    with pytest.raises(RecursionError) as excinfo:
        triangularNumbers.triangular(1000)
        assert "maximum recursion depth exceeded" in str(excinfo.value)


def test_triangular_iter_succeeds():
    triangularNumbers = TriangularNumbers()
    result = triangularNumbers.triangular_iter(1000)
    assert result == 500500


def test_triangular_tail_rec_fails_at_1000_depth():
    triangularNumbers = TriangularNumbers()
    with pytest.raises(RecursionError) as excinfo:
        triangularNumbers.triangular_tail_rec(1000)
        assert "maximum recursion depth exceeded" in str(excinfo.value)


def test_benchmark_triangular_numbers(benchmark):
    triangularNumbers = TriangularNumbers()
    sys.setrecursionlimit(2000)  # Increase the recursion limit for this test
    res = benchmark(triangularNumbers.triangular, 1500)
    assert res == 1125750  # Verify the result is correct


def test_benchmark_triangular_numbers_tail_rec(benchmark):
    triangularNumbers = TriangularNumbers()
    sys.setrecursionlimit(2000)  # Increase the recursion limit for this test
    res = benchmark(triangularNumbers.triangular_tail_rec, 1500)
    assert res == 1125750  # Verify the result is correct


def test_benchmark_triangular_numbers_iter(benchmark):
    triangularNumbers = TriangularNumbers()
    res = benchmark(
        triangularNumbers.triangular_iter, 1500
    )  # Benchmark the recursive version
    assert res == 1125750  # Verify the result is correct
    ## in python iterative is faster than recursive, so we expect the iterative version to be faster than the recursive version, even with tail recursion optimization
