from chapter4.SimpleStack import Stack


class TowerOfHanoi(object):
    """The Tower of Hanoi is a mathematical puzzle where the objective is to move a stack of disks from one spindle to another,
    following specific rules. The rules are as follows:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
    or on an empty spindle.
    3. No disk may be placed on top of a smaller disk.
    The puzzle starts with all disks stacked in ascending order of size on one spindle,
    and the goal is to move the entire stack to another spindle, following the rules mentioned above.
    The minimum number of moves required to solve the Tower of Hanoi puzzle with n disks is 2^n - 1."""

    def __init__(self, nDisks=3):
        self.__stacks = [None] * 3
        self.__labels = ["L", "M", "R"]
        self.__nDisks = nDisks
        self.reset()

    def reset(self):
        for spindle in range(3):
            self.__stacks[spindle] = Stack(self.__nDisks)
            if spindle == 0:
                for disk in range(self.__nDisks, 0, -1):
                    self.__stacks[spindle].push(disk)

    def label(self, spindle):
        return self.__labels[spindle]

    def height(self, spindle):
        return len(self.__stacks[spindle])

    def topDisk(self, spindle):
        if not self.__stacks[spindle].isEmpty():
            return self.__stacks[spindle].peek()

    def __str__(self):
        result = ""
        for spindle in range(3):
            if len(result) > 0:
                result += "\n"
            result += self.label(spindle) + ": " + str(self.__stacks[spindle])
        return result

    def move(self, source, to, show=False):
        if self.__stacks[source].isEmpty():
            raise Exception("Cannot move from empty spindle " + self.label(source))
        if not self.__stacks[to].isEmpty() and self.topDisk(source) > self.topDisk(to):
            raise Exception(
                "Cannot move disk "
                + str(self.topDisk(source))
                + " on top of disk "
                + str(self.topDisk(to))
            )
        self.__stacks[to].push(self.__stacks[source].pop())

        if show:
            print(
                "Move disk",
                self.topDisk(to),
                "from spindle",
                self.label(source),
                "to",
                self.label(to),
            )

    def solve(self, nDisks=None, start=0, goal=2, spare=1, show=False):
        """
        Recursion is 3-step process:
        1. Move n-1 disks from start to spare with goal as spare
        2. Move nth disk from start to goal
        3. Move n-1 disks from spare to goal with start as spare
        The base case is when nDisks is 0, in which case there is nothing to
        move and the function simply returns.
        The recursive case is when nDisks is greater than 0, in which case the
        function performs the three steps outlined above to move the disks
        from the start spindle to the goal spindle, using the spare spindle as
        needed.
        The function also includes error handling to ensure that the moves are
        valid according to the rules of the Tower of Hanoi puzzle,
        and it can optionally print the state of the puzzle after each move if
        the show parameter is set to True.
        """

        if nDisks is None:  # Defaut number of disks to move
            nDisks = self.height(start)  # is all the disks on start

        if nDisks <= 0:  ## if no request to move disks
            return  # there is nothing to do

        if (
            self.height(start) < nDisks
        ):  ## if there are fewer disks to move than requested ...
            raise Exception(
                "Not enough disks ("
                + str(nDisks)
                + ") on starting spindle "
                + self.label(start)
            )

        self.solve(
            nDisks - 1, start, spare, goal, show
        )  ## Move n-1 from start to spare with goal as spare
        self.move(start, goal, show)  # Move nth from start to goal
        if show:  ## show puzzle state after move
            print(self)

        self.solve(
            nDisks - 1, spare, goal, start, show
        )  ## then move n-1 from spare to goal with start as spare
        if nDisks == self.__nDisks and show:  ## were all disks moved ?
            print("Puzzle complete")
