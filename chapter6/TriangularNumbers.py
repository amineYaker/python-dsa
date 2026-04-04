class TriangularNumbers(object):
    """A class to compute triangular numbers"""

    def __init__(self):
        pass

    def triangular(self, n: int) -> int:
        """Returns the nth triangular number"""
        if n == 0:  ## base case
            return 0
        else:
            return n + self.triangular(n - 1)

    def triangular_iter(self, n: int) -> int:
        """Returns the nth triangular number using iteration"""
        result = 0
        for i in range(1, n + 1):
            result += i
        return result

    def triangular_tail_rec(self, n: int, accumulator: int = 0) -> int:
        """Returns the nth triangular number using tail recursion"""
        if n == 0:  ## base case
            return accumulator
        else:
            return self.triangular_tail_rec(n - 1, accumulator + n)


if __name__ == "__main__":
    triangularNumbers = TriangularNumbers()
    for i in range(10):
        print(f"Triangular number {i} is {triangularNumbers.triangular(i)}")
